# HTMX `hx-swap-oob` (Out Of Band - OOB) - Ejemplo con Python y Flask

Este es un ejemplo simple de cómo usar **hx-swap-oob** con Flask para
actualizar partes de la página que están fuera del contenedor original
del `hx-get`.

### Resultado Final 😲
![Resultado Final](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/refs/heads/master/evento-hx-swap-oob.gif)

## Qué es `hx-swap-oob`

- **OOB = Out Of Band (fuera de banda)**.
- Permite actualizar partes de la página que **no forman parte** del
  elemento donde hiciste el `hx-get`.
- Normalmente HTMX reemplaza **SOLO** el `div` donde le pusiste
  `hx-swap`.
- Con `hx-swap-oob="true"`, puedes incluir en tu respuesta HTML
  **otros elementos** que se actualizarán "por ID" en la página,
  aunque no estén dentro del contenedor original.

## Referencia

https://htmx.org/attributes/hx-swap-oob/


## Cómo funciona

1.  La página carga el contador en `0`.
2.  Haces clic en el botón `Sumar +1` que hace una petición `hx-get` a
    `/sumar`.
3.  El servidor responde con:
    - Un párrafo nuevo que se inserta en `#result`.
    - Un `<span>` con `hx-swap-oob="true"` que reemplaza el contenido
      de `#contador` directamente.
4.  El contador se actualiza **sin necesidad de recargar toda la página**.


## Cómo correrlo

1.  Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

2.  Ejecuta el servidor:

```bash
python app.py
```

3.  Abre <http://127.0.0.1:5000> en tu navegador.

## 🙌 Cómo puedes apoyar 📢:

✨ **Comparte este proyecto** con otros desarrolladores para que puedan beneficiarse 📢.

☕ **Invítame un café o una cerveza 🍺**:
   - [Paypal](https://www.paypal.me/iamdeveloper86) (`iamdeveloper86@gmail.com`).

### ⚡ ¡No olvides SUSCRIBIRTE a la [Comunidad WebDeveloper](https://www.youtube.com/WebDeveloperUrianViera?sub_confirmation=1)!


#### ⭐ **Déjanos una estrella en GitHub**:
   - Dicen que trae buena suerte 🍀.
**Gracias por tu apoyo 🤓.**