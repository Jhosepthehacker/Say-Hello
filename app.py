from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/home', tags=["Home"])
def home(response: Response):
    client_ip = response.client_host

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
          </body>
        </html>
      """
    )
