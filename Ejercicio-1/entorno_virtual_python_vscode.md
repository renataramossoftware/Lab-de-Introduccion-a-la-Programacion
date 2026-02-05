# 🐍 Crear un Entorno Virtual en Python con Visual Studio Code

Guía paso a paso para crear y usar un entorno virtual en Python utilizando Visual Studio Code.
Este archivo está listo para subirse directamente a GitHub.

---

## 📌 Paso 1 — Abrir la carpeta del proyecto en VS Code

1. Abre **Visual Studio Code**.
2. Ve a **File → Open Folder**.
3. Selecciona la carpeta donde trabajarás tu proyecto.
4. Abre la terminal integrada con `Ctrl + \``.

📌 Aquí se creará el entorno virtual.

![Paso 1](https://raw.githubusercontent.com/renataramossoftware/Lab-de-Introduccion-a-la-Programacion/d278dd37bb67902169f28fe5131e3b6ef41798af/Ejercicio-1/Assets/1.png)

---

## 🔧 Paso 2 — Crear el entorno virtual

En la terminal de VS Code ejecuta:

```bash
python -m venv .venv
```

🔹 Esto crea una carpeta `.venv` con un Python aislado para tu proyecto.

![Paso 2](https://raw.githubusercontent.com/renataramossoftware/Lab-de-Introduccion-a-la-Programacion/d278dd37bb67902169f28fe5131e3b6ef41798af/Ejercicio-1/Assets/2.png)

---

## ▶️ Paso 3 — Activar el entorno virtual

### En Windows (PowerShell):

```powershell
.venv\Scripts\Activate
```

### En macOS / Linux:

```bash
source .venv/bin/activate
```

✔️ Cuando esté activo verás `(.venv)` en la terminal.

![Paso 3](https://raw.githubusercontent.com/renataramossoftware/Lab-de-Introduccion-a-la-Programacion/d278dd37bb67902169f28fe5131e3b6ef41798af/Ejercicio-1/Assets/3.png)

---

## 📦 Paso 4 — Usar el entorno virtual

Instalar paquetes:

```bash
pip install nombre_paquete
```

Ver paquetes instalados:

```bash
pip list
```

Ejecutar Python:

```bash
python archivo.py
```

---

## 🧹 Paso 5 — Desactivar el entorno virtual

```bash
deactivate
```

---

## ✅ Resumen

- Abrir carpeta del proyecto
- Crear entorno virtual
- Activarlo
- Trabajar con Python
- Desactivarlo al terminar

---

📌 **Archivo listo para GitHub**
