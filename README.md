# Ejemplo: HTMX `hx-swap-oob` (Out Of Band)

Este es un ejemplo simple de cómo usar **hx-swap-oob** con Flask para
actualizar partes de la página que están fuera del contenedor original
del `hx-get`.

## Qué es `hx-swap-oob`

- **OOB = Out Of Band (fuera de banda)**.
- Permite actualizar partes de la página que **no forman parte** del
  elemento donde hiciste el `hx-get`.
- Normalmente HTMX reemplaza **SOLO** el `div` donde le pusiste
  `hx-swap`.
- Con `hx-swap-oob="true"`, puedes incluir en tu respuesta HTML
  **otros elementos** que se actualizarán "por ID" en la página,
  aunque no estén dentro del contenedor original.

---

## Referencia

https://htmx.org/attributes/hx-swap-oob/

## Estructura de archivos

    .
    ├── app.py
    ├── templates/
    │   ├── index.html
    │   └── snippet.html

---

## Código

### app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

contador = 0

@app.route("/")
def index():
    return render_template("index.html", contador=contador)

@app.route("/sumar")
def sumar():
    global contador
    contador += 1
    return render_template("snippet.html", contador=contador)

if __name__ == "__main__":
    app.run(debug=True)
```

### templates/index.html

```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <title>Ejemplo OOB</title>
    <script src="https://unpkg.com/htmx.org@1.9.12"></script>
  </head>
  <body>
    <h1>Contador con OOB</h1>
    <p>Contador: <span id="contador">{{ contador }}</span></p>

    <button hx-get="/sumar" hx-target="#result" hx-swap="innerHTML">
      Sumar +1
    </button>

    <div id="result"></div>
  </body>
</html>
```

### templates/snippet.html

```html
<span id="contador" hx-swap-oob="true">{{ contador }}</span>
<p>Sumaste un número. Valor actual: {{ contador }}</p>
```

---

## Cómo funciona

1.  La página carga el contador en `0`.
2.  Haces clic en el botón `Sumar +1` que hace una petición `hx-get` a
    `/sumar`.
3.  El servidor responde con:
    - Un párrafo nuevo que se inserta en `#result`.
    - Un `<span>` con `hx-swap-oob="true"` que reemplaza el contenido
      de `#contador` directamente.
4.  El contador se actualiza **sin necesidad de recargar toda la página**.

---

## Cómo correrlo

1.  Instala Flask:

```bash
pip install flask
```

2.  Ejecuta el servidor:

```bash
python app.py
```

3.  Abre <http://127.0.0.1:5000> en tu navegador.
