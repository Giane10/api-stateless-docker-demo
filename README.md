# 🚀 API Stateless & Cloud Migration Demo

Este projeto é um protótipo funcional desenvolvido para o **Demo Day da 🚀 squad-3 (Curso Avanti)**. Ele demonstra a transição de uma infraestrutura física instável para uma arquitetura resiliente em nuvem.

## 📋 Sobre o Projeto
O objetivo é validar a eficácia da conteinerização e dos princípios REST na resolução de problemas críticos de TI, como o tempo de inatividade (downtime) e custos elevados de manutenção.

### Tecnologias Utilizadas:
* **Python & FastAPI**: Para a criação de uma API de alto desempenho e arquitetura Stateless (sem retenção de lixo no servidor).
* **Docker & Docker Compose:**: Utilizado como "Receita Universal" para padronização, isolamento e portabilidade do ambiente.
* **GitHub Actions:**: : Esteira de CI/CD para automação de build, testes e entrega contínua.
* **HTML/JavaScript**: Interface interativa para simulação de falhas e recuperação em tempo real.

---

## 🏗️ Como a Solução Funciona

### 🔴 O Problema (Legado)
Servidores físicos são pontos únicos de falha. Se o hardware falha, o serviço é interrompido, gerando prejuízos financeiros e operacionais.

### 🟢 A Solução (Modernização)

### Conteinerização:
O código é empacotado via **Dockerfile**, permitindo que o servidor seja recriado em segundos em qualquer provedor de nuvem.
### Resiliência (Self-healing):
O sistema utiliza políticas de reinicialização automática.
### Cloud Ready: 
A arquitetura permite que a AWS escale a aplicação horizontalmente conforme a demanda.

---

## 🛠️ Como Executar a Demonstração
Para rodar este projeto localmente e ver a "mágica" acontecer:

### 1. Pré-requisitos
Docker e Docker Compose instalados.

### 2. Subindo a infraestrutura
Basta um comando para construir a imagem e iniciar o serviço:

```bash
docker-compose up --build
```

### 3. Acessando o Dashboard
Abra o navegador em: http://localhost:8000

---

###     Guia de Teste:
Simular Falha Física:
Altera o estado da API para "Unhealthy" e muda a interface para o modo crítico (🚨).
Restaurar via Cloud:
Simula a recuperação automática do ambiente Docker, devolvendo a estabilidade ao sistema (✅).

---

### ⚙️ Esteira de CI/CD
O projeto conta com um workflow automatizado via GitHub Actions que executa:

### 1. Build & Test:
Valida o código Python e as dependências.

### 2. Docker Delivery:
Realiza o login no Docker Hub, gera a imagem oficial e faz o push automaticamente para o repositório da squad.

---

## 📈 Impacto no Negócio

### Alta Disponibilidade: 
Sistema imune a falhas de hardware local.
### Escalabilidade: 
A arquitetura permite atender milhares de requisições simultâneas. 
### Segurança Operacional: 
Garantia de que apenas códigos validados pela esteira de CI/CD cheguem ao ambiente de produção.

---