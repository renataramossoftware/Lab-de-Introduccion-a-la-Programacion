from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
app.secret_key = "nueva_clave_2026"

# ==========================================
# MEMORIA DEL SISTEMA
# ==========================================
inventario = {}

catalogo = {
    "779123455001": {"nombre": "Aceite Premium 1L", "sku": "ACE-001", "precio": 16.00, "icono": "🛢️"},
    "779123455002": {"nombre": "Pasta Orgánica 500g", "sku": "PAS-002", "precio": 3.80, "icono": "🍜"},
    "779123455003": {"nombre": "Detergente Ultra Clean", "sku": "DET-003", "precio": 13.50, "icono": "🧽"},
    "779123455004": {"nombre": "Cereal Miel Natural", "sku": "CER-004", "precio": 7.20, "icono": "🥣"},
    "779123455005": {"nombre": "Café Intenso Molido", "sku": "CAF-005", "precio": 19.00, "icono": "☕"}
}

# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NovaMarket - Panel</title>

<style>
:root {
    --bg: #0f172a;
    --card: #1e293b;
    --text: #e2e8f0;
    --accent: #22c55e;
    --danger: #ef4444;
}

body {
    margin: 0;
    font-family: Arial;
    background: var(--bg);
    color: var(--text);
}

h1 {
    text-align: center;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: auto;
}

.card {
    background: var(--card);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}

button {
    background: var(--accent);
    border: none;
    padding: 10px;
    border-radius: 8px;
    cursor: pointer;
    color: black;
    font-weight: bold;
}

button:hover {
    opacity: 0.8;
}

input {
    padding: 10px;
    border-radius: 6px;
    border: none;
    width: 100%;
    margin-bottom: 10px;
}

.total {
    font-size: 20px;
    text-align: right;
}
</style>
</head>

<body>

<h1>🛒 NovaMarket - Punto de Venta</h1>

<div class="container">

<div class="card">
<input type="text" id="codigo" placeholder="Escanea o escribe código">
<button onclick="agregar()">Agregar Producto</button>
</div>

<div id="lista" class="card"></div>

<div class="card total">
Total: $<span id="total">0.00</span>
</div>

</div>

<script>

async function agregar() {
    const codigo = document.getElementById("codigo").value;

    const res = await fetch("/agregar", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({codigo})
    });

    actualizar();
}

async function actualizar() {
    const res = await fetch("/estado");
    const data = await res.json();

    let html = "";
    let total = 0;

    for (let c in data) {
        let p = data[c];
        total += p.precio * p.cantidad;

        html += `
        <div>
            ${p.icono} ${p.nombre} x${p.cantidad} - $${p.precio}
        </div>`;
    }

    document.getElementById("lista").innerHTML = html;
    document.getElementById("total").innerText = total.toFixed(2);
}

setInterval(actualizar, 1000);

</script>

</body>
</html>
"""

# ==========================================
# RUTAS
# ==========================================
@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/agregar", methods=["POST"])
def agregar():
    data = request.json
    codigo = data["codigo"]

    if codigo in catalogo:
        if codigo not in inventario:
            inventario[codigo] = {**catalogo[codigo], "cantidad": 1}
        else:
            inventario[codigo]["cantidad"] += 1

    return jsonify({"ok": True})

@app.route("/estado")
def estado():
    return jsonify(inventario)

# ==========================================
# EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)