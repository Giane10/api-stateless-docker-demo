from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
        <head>
            <title>Simulador de Migração - Avanti</title>
            <style>
                body { font-family: 'Segoe UI', sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; transition: 0.5s; }
                .card { background: white; padding: 2.5rem; border-radius: 20px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); text-align: center; width: 400px; }
                .btn { padding: 10px 20px; margin: 10px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; color: white; transition: 0.3s; }
                .btn-error { background-color: #f44336; }
                .btn-success { background-color: #4CAF50; }
                .btn:hover { opacity: 0.8; transform: scale(1.05); }
                #status-icon { font-size: 50px; margin-bottom: 10px; }
            </style>
        </head>
        <body id="bg">
            <div class="card">
                <div id="status-icon">✅</div>
                <h1 id="titulo">Sistema na Nuvem</h1>
                <p id="msg">A migração para Docker/AWS foi concluída com sucesso.</p>
                <hr style="border: 0.5px solid #eee; margin: 20px 0;">
                <p><strong>Simular Cenários:</strong></p>
                <button class="btn btn-error" onclick="simularErro()">Simular Falha Física</button>
                <button class="btn btn-success" onclick="simularSucesso()">Restaurar via Cloud</button>
            </div>

            <script>
                function simularErro() {
                    document.getElementById('bg').style.backgroundColor = '#ffebee';
                    document.getElementById('status-icon').innerText = '🚨';
                    document.getElementById('titulo').innerText = 'Servidor Físico OFFLINE';
                    document.getElementById('titulo').style.color = '#d32f2f';
                    document.getElementById('msg').innerText = 'O hardware antigo falhou. Sistema inacessível sem a nuvem.';
                }
                function simularSucesso() {
                    document.getElementById('bg').style.backgroundColor = '#f0f2f5';
                    document.getElementById('status-icon').innerText = '✅';
                    document.getElementById('titulo').innerText = 'Sistema na Nuvem';
                    document.getElementById('titulo').style.color = '#333';
                    document.getElementById('msg').innerText = 'A migração para Docker/AWS foi concluída com sucesso.';
                }
            </script>
        </body>
    </html>
    """