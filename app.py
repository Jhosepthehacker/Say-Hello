from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

client_ip = None

app = FastAPI()

@app.get('/home', tags=["Home"])
def home(response: Request):
    global client_ip
    client_ip = response.client.host

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
          <body>
            <script>
              // const parche_vulnerability_xss = undefined;
              const add_ip = () => {
                const new_ip = {client_ip};

                containerHTML = "<ul><br><li>${new_ip}</li></ul>
              }
            </script>
        """
    )
