from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = "clave_secreta_2026"

# Datos de acceso
USUARIO_CORRECTO = "admin"
CONTRASENA_CORRECTA = "admin2026"

# --- INTERFAZ HTML ---
INDEX_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema RRP | Lector</title>
    <script src="https://unpkg.com/html5-qrcode"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { 
            margin: 0; 
            font-family: 'Segoe UI', sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            min-height: 100vh; 
            position: relative;
        }
        .card { 
            background: rgba(255, 255, 255, 0.95); 
            padding: 2.5rem; 
            border-radius: 20px; 
            box-shadow: 0 15px 35px rgba(0,0,0,0.2); 
            width: 100%; 
            max-width: 380px; 
            text-align: center; 
            backdrop-filter: blur(10px);
        }
        .icon-header {
            background: #4f46e5;
            color: white;
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            margin: 0 auto 1.5rem;
        }
        h2 { color: #1f2937; margin: 0 0 1rem; font-size: 1.5rem; }
        input { 
            width: 100%; 
            padding: 14px; 
            margin: 10px 0; 
            border: 2px solid #e5e7eb; 
            border-radius: 10px; 
            box-sizing: border-box;
            transition: border-color 0.3s;
        }
        input:focus { border-color: #4f46e5; outline: none; }
        button { 
            width: 100%; 
            padding: 14px; 
            background: #4f46e5; 
            color: white; 
            border: none; 
            border-radius: 10px; 
            font-weight: bold; 
            cursor: pointer; 
            margin-top: 15px;
            font-size: 1rem;
        }
        button:hover { background: #4338ca; }
        #reader { width: 100%; margin-top: 20px; border-radius: 12px; overflow: hidden; }
        
        /* Estilo para los datos escaneados */
        .tabla-resultados {
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
            font-size: 0.9rem;
            background: #f9fafb;
            border-radius: 8px;
            overflow: hidden;
            text-align: left;
        }
        .tabla-resultados th { background: #e5e7eb; padding: 8px; color: #4b5563; text-align: center; }
        .tabla-resultados td { padding: 12px; border-top: 1px solid #f3f4f6; color: #111827; }
        .dato-item { margin-bottom: 4px; }
        .dato-label { font-weight: bold; color: #4f46e5; text-transform: uppercase; font-size: 0.75rem; display: block; }

        .rrp-brand {
            position: fixed;
            bottom: 20px;
            right: 20px;
            font-weight: 900;
            font-size: 2rem;
            color: rgba(255, 255, 255, 0.3);
            letter-spacing: 2px;
            pointer-events: none;
        }
        .logout-btn { display: inline-block; margin-top: 20px; color: #ef4444; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>

    <div class="rrp-brand">RRP</div>

    {% if session.get("logged_in") %}
        <div class="card">
            <div class="icon-header"><i data-lucide="scan-barcode"></i></div>
            <h2>Escanear Producto</h2>
            <div id="reader"></div>
            
            <table class="tabla-resultados">
                <thead>
                    <tr>
                        <th>Información Detectada</th>
                    </tr>
                </thead>
                <tbody id="lista-codigos">
                    <tr>
                        <td style="color: #9ca3af; text-align: center;">Esperando escaneo...</td>
                    </tr>
                </tbody>
            </table>

            <a class="logout-btn" href="{{ url_for('logout') }}">Salir del sistema</a>
        </div>
    {% else %}
        <form class="card" method="post">
            <div class="icon-header"><i data-lucide="lock"></i></div>
            <h2>Iniciar Sesión</h2>
            <input type="text" name="user" placeholder="Nombre de usuario" required>
            <input type="password" name="pass" placeholder="Contraseña" required>
            <button type="submit">Ingresar al Portal</button>
            {% if error %}<p style="color: #dc2626; margin-top: 10px;">{{ error }}</p>{% endif %}
        </form>
    {% endif %}

    <script>
        lucide.createIcons();

        {% if session.get("logged_in") %}
        function procesarCadena(rawText) {
            // Si es un formato de WIFI
            if (rawText.startsWith("WIFI:")) {
                const ssid = rawText.match(/S:(.*?);/);
                const pass = rawText.match(/P:(.*?);/);
                
                return `
                    <div class="dato-item"><span class="dato-label">Red Wi-Fi</span>${ssid ? ssid[1] : 'No detectada'}</div>
                    <div class="dato-item"><span class="dato-label">Contraseña</span>${pass ? pass[1] : 'Sin contraseña'}</div>
                `;
            } 
            // Si es cualquier otro texto o código
            else {
                return `<div class="dato-item"><span class="dato-label">Contenido</span>${rawText}</div>`;
            }
        }

        function onScan(code) {
            const lista = document.getElementById('lista-codigos');
            
            if (lista.innerText.includes("Esperando")) {
                lista.innerHTML = "";
            }

            const contenidoLimpio = procesarCadena(code);
            const nuevaFila = `<tr><td>${contenidoLimpio}</td></tr>`;
            
            // Ponemos el nuevo arriba
            lista.innerHTML = nuevaFila + lista.innerHTML;

            fetch('/guardar_codigo', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ codigo: code })
            });
        }
        
        let scanner = new Html5QrcodeScanner("reader", { 
            fps: 15, 
            qrbox: 250,
            rememberLastUsedCamera: true
        });
        scanner.render(onScan);

        // Traducción de botones
        setTimeout(() => {
            const btns = {
                "Request Camera Permissions": "Permitir Cámara",
                "Stop Scanning": "Detener",
                "Start Scanning": "Escanear",
                "Choose Image": "Elegir Imagen"
            };
            document.querySelectorAll('button').forEach(b => {
                if(btns[b.innerText]) b.innerText = btns[b.innerText];
            });
        }, 500);
        {% endif %}
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("user")
        password = request.form.get("pass")
        if user == USUARIO_CORRECTO and password == CONTRASENA_CORRECTA:
            session["logged_in"] = True
            return redirect(url_for("index"))
        return render_template_string(INDEX_HTML, error="Datos incorrectos")
    return render_template_string(INDEX_HTML)

@app.route("/guardar_codigo", methods=["POST"])
def guardar_codigo():
    data = request.json
    print(f"¡CÓDIGO RECIBIDO!: {data.get('codigo')}")
    return jsonify({"status": "ok"})

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000, ssl_context='adhoc')