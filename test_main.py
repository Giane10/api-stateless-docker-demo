from fastapi.testclient import TestClient
from main import app

# Criamos um cliente de teste que simula o navegador acedendo à API
client = TestClient(app)

def test_status_inicial_saudavel():
    """Valida se a API inicia no estado saudável (Nuvem OK)"""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "Sistema operando na AWS" in response.json()["mensagem"]

def test_fluxo_de_falha_e_recuperacao():
    """Testa o ciclo completo: Erro -> Status Offline -> Restauro -> Status Online"""
    
    # 1. Simula a falha física
    client.post("/simular-erro")
    response_erro = client.get("/status")
    assert response_erro.json()["status"] == "unhealthy"
    
    # 2. Restaura via Cloud
    client.post("/restaurar")
    response_ok = client.get("/status")
    assert response_ok.json()["status"] == "healthy"

def test_dashboard_acessivel():
    """Garante que a interface HTML está a ser servida corretamente"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Projeto Resiliência - Avanti" in response.text
