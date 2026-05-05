import os
import sqlite3
import csv
from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify, send_file

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

# Configuración de archivos
DB_NAME = "inventario.db"
CSV_NAME = "productos_registrados.csv"

# Datos de acceso
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "admin2026"

# --- BASE DE DATOS ---
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS productos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_producto TEXT NOT NULL,
                            codigo TEXT NOT NULL,
                            id_proveedor TEXT NOT NULL,
                            num_productos INTEGER NOT NULL)''')

def obtener_productos():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos ORDER BY id DESC")
        return cursor.fetchall()

# --- INTERFAZ HTML ACTUALIZADA ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestión de Inventario | RRP</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <style>
        body { 
            margin: 0; font-family: 'Segoe UI', sans-serif; 
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%); 
            min-height: 100vh; padding: 20px; color: #333;
        }
        .container { 
            display: flex; gap: 20px; max-width: 1200px; margin: 0 auto; 
            flex-wrap: wrap; justify-content: center; 
        }
        .card { 
            background: white; padding: 20px; border-radius: 20px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.3); width: 100%; 
        }
        .sidebar { max-width: 380px; flex: 1; }
        .main-content { max-width: 750px; flex: 2; }
        
        h2 { color: #1e40af; margin-top: 0; border-bottom: 2px solid #f3f4f6; padding-bottom: 10px; }
        .form-group { margin-bottom: 12px; text-align: left; }
        label { font-size: 0.8rem; font-weight: bold; color: #1e40af; display: block; margin-bottom: 4px; }
        input { width: 100%; padding: 10px; border: 1px solid #d1d5db; border-radius: 8px; box-sizing: border-box; }
        
        .btn { width: 100%; padding: 12px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; margin-top: 5px; font-size: 0.9rem; }
        .btn-primary { background: #1e40af; color: white; }
        .btn-success { background: #059669; color: white; text-decoration: none; display: block; text-align: center; margin-top: 10px; line-height: 2.5; }
        
        #reader { width: 100%; border-radius: 12px; overflow: hidden; background: #fafafa; border: 1px solid #eee; }
        
        .table-container { overflow-x: auto; margin-top: 10px; }
        table { width: 100%; border-collapse: collapse; background: white; }
        th, td { padding: 12px; border-bottom: 1px solid #eee; text-align: left; }
        th { background: #f8fafc; color: #1e40af; font-size: 0.8rem; text-transform: uppercase; }
        tr:hover { background: #f1f5f9; }

        .watermark { position: fixed; bottom: 15px; right: 20px; opacity: 0.4; color: white; font-weight: bold; font-size: 1.2rem; pointer-events: none; }
        .logout { color: #ef4444; text-decoration: none; font-size: 0.8rem; display: block; text-align: center; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="watermark">by Ren</div>

    {% if session.get("logged_in") %}
    <div class="container">
        <div class="sidebar">
            <div class="card">
                <h2>Captura</h2>
                <div id="reader"></div>
                <form id="productForm">
                    <div class="form-group"><label>Nombre del Producto</label><input type="text" id="nombre" required></div>
                    <div class="form-group"><label>Código Escaneado</label><input type="text" id="codigo" required></div>
                    <div class="form-group"><label>ID Proveedor</label><input type="text" id="proveedor" required></div>
                    <div class="form-group"><label>Cantidad</label><input type="number" id="cantidad" value="1" required></div>
                    <button type="submit" class="btn btn-primary">Guardar Producto</button>
                    <a href="/exportar" class="btn btn-success">Descargar CSV</a>
                </form>
                <a href="{{ url_for('logout') }}" class="logout">CERRAR SESIÓN</a>
            </div>
        </div>

        <div class="main-content">
            <div class="card">
                <h2>Gestión de Inventario</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Producto</th>
                                <th>Código</th>
                                <th>Proveedor</th>
                                <th>Stock</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for p in productos %}
                            <tr>
                                <td>{{ p['id'] }}</td>
                                <td><strong>{{ p['nombre_producto'] }}</strong></td>
                                <td><code>{{ p['codigo'] }}</code></td>
                                <td>{{ p['id_proveedor'] }}</td>
                                <td>{{ p['num_productos'] }}</td>
                            </tr>
                            {% endfor %}
                            {% if not productos %}
                            <tr><td colspan="5" style="text-align:center; color:#999;">No hay productos registrados</td></tr>
                            {% endif %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
    {% else %}
        <div class="card" style="max-width:350px; margin: 100px auto; text-align:center;">
            <h2 style="border:none;">Acceso RRP</h2>
            <form method="post">
                <input type="text" name="user" placeholder="Usuario" required style="margin-bottom:12px;">
                <input type="password" name="pass" placeholder="Contraseña" required style="margin-bottom:12px;">
                <button type="submit" class="btn btn-primary">Ingresar al Sistema</button>
            </form>
            {% if error %}<p style="color:#ef4444; font-weight:bold; margin-top:15px;">{{ error }}</p>{% endif %}
        </div>
    {% endif %}

    <script>
        {% if session.get("logged_in") %}
        // Configuración del Escáner
        const scanner = new Html5QrcodeScanner("reader", { 
            fps: 10, 
            qrbox: 250,
            aspectRatio: 1.0
        });
        
        scanner.render((text) => {
            document.getElementById('codigo').value = text;
            // Opcional: sonido o vibración aquí
        });

        // Envío del Formulario
        document.getElementById('productForm').onsubmit = async (e) => {
            e.preventDefault();
            const data = {
                nombre: document.getElementById('nombre').value,
                codigo: document.getElementById('codigo').value,
                proveedor: document.getElementById('proveedor').value,
                cantidad: document.getElementById('cantidad').value
            };

            const resp = await fetch('/guardar', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });

            const res = await resp.json();
            if(res.status === 'success') {
                location.reload(); // Recarga para actualizar la tabla
            } else {
                alert("Error: " + res.message);
            }
        };
        {% endif %}
    </script>
</body>
</html>
"""

# --- RUTAS ---
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")
        if user == USUARIO_CORRECTO and password == CONTRASENA_CORRECTA:
            session["logged_in"] = True
            return redirect(url_for("index"))
        return render_template_string(HTML_TEMPLATE, error="Credenciales Incorrectas")
    
    # Solo cargar productos si está logueado
    productos = obtener_productos() if session.get("logged_in") else []
    return render_template_string(HTML_TEMPLATE, productos=productos)

@app.route('/guardar', methods=['POST'])
def guardar():
    if not session.get("logged_in"): return jsonify({"status": "error", "message": "No autorizado"})
    data = request.json
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("INSERT INTO productos (nombre_producto, codigo, id_proveedor, num_productos) VALUES (?, ?, ?, ?)",
                         (data['nombre'], data['codigo'], data['proveedor'], data['cantidad']))
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/exportar')
def exportar():
    if not session.get("logged_in"): return redirect(url_for("index"))
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
    
    with open(CSV_NAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Nombre', 'Codigo', 'Proveedor', 'Cantidad'])
        writer.writerows(rows)
    
    return send_file(CSV_NAME, as_attachment=True)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# --- ARRANQUE SEGURO ---
if __name__ == "__main__":
    init_db()
    # Host 0.0.0.0 permite que otros dispositivos (celular) entren por tu IP
    # ssl_context='adhoc' activa el HTTPS necesario para la cámara
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context='adhoc')