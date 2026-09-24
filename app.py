from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

client_ip = None

app = FastAPI()

@app.get('/home', tags=["Home"])
def home(request: Request):  # Cambiado por claridad
    global client_ip
    client_ip = request.client.host if request.client else "Desconocida"

    return HTMLResponse(
      """
      <!DOCTYPE html>
        <html lang="es">
          <head>
            <title>Say Hello</title>
              <meta charset="utf-8">
                <meta name="description" content="This server say Hello">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
          </head>
          <body>
            <h1>Hola Prima</h1>
          </body>
        </html>
      """
    )

@app.get('/bounty', tags=["Bounty Logs"])
def bounty():
    return HTMLResponse(
        f"""
        <!DOCTYPE html>
        <html lang="es">
          <head><title>Bounty Logs</title></head>
          <body>
            <div id="log-container"></div>
            <script>
              const add_ip = () => {{
                // 1. Las comillas alrededor de la variable de Python son obligatorias en JS
                const new_ip = "{client_ip}";
                
                // 2. Buscamos el contenedor real en el DOM y cerramos bien las comillas
                const container = document.getElementById("log-container");
                container.innerHTML = "<ul><li>" + new_ip + "</li></ul>";
              }};
              add_ip();
            </script>
          </body>
        </html>
        """
    )
