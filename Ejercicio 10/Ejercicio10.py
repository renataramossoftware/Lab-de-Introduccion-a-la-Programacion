from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- DISEÑO EN UN SOLO STRING (HTML + CSS + JS) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Ejercicios | Python</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #0f172a; color: white; font-family: 'Segoe UI', sans-serif; }
        .glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.1); }
        .neon-border { border-left: 4px solid #22d3ee; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
    </style>
</head>
<body class="p-4 md:p-10">
    <div class="max-w-6xl mx-auto">
        <header class="mb-10 text-left border-b border-slate-800 pb-6">
            <h1 class="text-3xl font-extrabold text-cyan-400 tracking-tight">PYTHON <span class="text-white">LAB</span></h1>
            <p class="text-slate-400 mt-1">Selecciona, ingresa datos y ejecuta en tiempo real.</p>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
            <div class="lg:col-span-4 space-y-3">
                <h2 class="text-sm font-bold uppercase text-slate-500 mb-4 tracking-widest">Lista de Ejercicios</h2>
                <div class="grid grid-cols-1 gap-2 overflow-y-auto max-h-[500px] pr-2">
                    <button onclick="configForm('1', 'Repetir Palabra', 'Escribe una palabra')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">1. Repetir 10 veces</button>
                    <button onclick="configForm('2', 'Años cumplidos', 'Ingresa tu edad')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">2. Contador de Años</button>
                    <button onclick="configForm('3', 'Números Impares', 'Hasta qué número')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">3. Serie Impares</button>
                    <button onclick="configForm('4', 'Cuenta Regresiva', 'Número inicial')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">4. Regresivo a 0</button>
                    <button onclick="configForm('5', 'Inversión', '')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">5. Calculadora Financiera</button>
                    <button onclick="configForm('6', 'Triángulo Asteriscos', 'Altura del triángulo')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">6. Dibujar Triángulo</button>
                    <button onclick="configForm('10', 'Verificador de Primos', 'Número a evaluar')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">10. ¿Es Número Primo?</button>
                    <button onclick="configForm('12', 'Contador de Letras', '')" class="text-left p-3 rounded-lg glass hover:bg-cyan-500/20 transition-all duration-300">12. Buscar Letra</button>
                </div>
            </div>

            <div class="lg:col-span-8 space-y-6">
                <div class="glass p-8 rounded-2xl neon-border">
                    <h3 id="form-title" class="text-2xl font-bold mb-6 text-cyan-300 italic">Bienvenido al Lab</h3>
                    <form method="POST" class="space-y-5">
                        <input type="hidden" name="ejercicio_id" id="ejercicio_id">
                        <div id="dynamic-inputs" class="space-y-4">
                            <p class="text-slate-500">Haz clic en un ejercicio del panel izquierdo para empezar.</p>
                        </div>
                        <button type="submit" id="btn-submit" class="hidden w-full md:w-auto bg-cyan-600 hover:bg-cyan-500 px-8 py-3 rounded-xl font-bold transition shadow-lg shadow-cyan-900/20">EJECUTAR</button>
                    </form>
                </div>

                {% if resultado %}
                <div class="bg-black/40 border border-slate-700 p-6 rounded-2xl font-mono">
                    <div class="flex items-center justify-between mb-4 border-b border-slate-800 pb-2">
                        <span class="text-xs text-slate-500 font-bold uppercase">Consola de Salida</span>
                        <div class="flex gap-2 text-slate-600">
                             <span class="w-3 h-3 rounded-full bg-red-500/50"></span>
                             <span class="w-3 h-3 rounded-full bg-yellow-500/50"></span>
                             <span class="w-3 h-3 rounded-full bg-green-500/50"></span>
                        </div>
                    </div>
                    <div class="text-emerald-400 space-y-1">
                        {% for linea in resultado %}
                            <p class="leading-relaxed"><span class="text-slate-600 mr-2">$</span> {{ linea }}</p>
                        {% endfor %}
                    </div>
                </div>
                {% endif %}
            </div>
        </div>
    </div>

    <script>
        function configForm(id, title, placeholder) {
            const container = document.getElementById('dynamic-inputs');
            const titleEl = document.getElementById('form-title');
            const idInput = document.getElementById('ejercicio_id');
            const btn = document.getElementById('btn-submit');
            
            idInput.value = id;
            titleEl.innerText = title;
            btn.classList.remove('hidden');
            container.innerHTML = '';

            if (id === '1') {
                container.innerHTML = `<input type="text" name="val1" placeholder="${placeholder}" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none" required>`;
            } else if (['2', '3', '4', '6', '10'].includes(id)) {
                container.innerHTML = `<input type="number" name="val1" placeholder="${placeholder}" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none" required>`;
            } else if (id === '5') {
                container.innerHTML = `
                    <input type="number" step="0.01" name="val1" placeholder="Monto a invertir" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none mb-2" required>
                    <input type="number" name="val2" placeholder="Interés % anual" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none mb-2" required>
                    <input type="number" name="val3" placeholder="Años" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none" required>
                `;
            } else if (id === '12') {
                container.innerHTML = `
                    <input type="text" name="val1" placeholder="Ingresa la frase" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none mb-2" required>
                    <input type="text" name="val2" maxlength="1" placeholder="Letra a buscar" class="w-full bg-slate-900 p-3 rounded-lg border border-slate-700 focus:border-cyan-500 outline-none" required>
                `;
            }
        }
    </script>
</body>
</html>
"""

# --- LÓGICA DEL SERVIDOR ---
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = []
    if request.method == 'POST':
        eid = request.form.get('ejercicio_id')
        v1 = request.form.get('val1')
        v2 = request.form.get('val2')
        v3 = request.form.get('val3')

        try:
            if eid == "1":
                resultado = [v1 for _ in range(10)]
            elif eid == "2":
                resultado = [str(a) for a in range(1, int(v1) + 1)]
            elif eid == "3":
                resultado = [str(i) for i in range(1, int(v1) + 1) if i % 2 != 0]
            elif eid == "4":
                resultado = [str(i) for i in range(int(v1), -1, -1)]
            elif eid == "5":
                cap = float(v1)
                inte = float(v2) / 100
                for a in range(1, int(v3) + 1):
                    cap += cap * inte
                    resultado.append(f"Año {a}: ${cap:,.2f}")
            elif eid == "6":
                resultado = ["*" * i for i in range(1, int(v1) + 1)]
            elif eid == "10":
                n = int(v1)
                primo = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
                resultado = [f"El {n} {'ES PRIMO' if primo else 'NO ES PRIMO'}"]
            elif eid == "12":
                resultado = [f"La letra '{v2}' aparece {v1.count(v2)} veces"]
        except:
            resultado = ["Error: Verifica que los datos sean correctos."]

    return render_template_string(HTML_TEMPLATE, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)