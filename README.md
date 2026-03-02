# 🚀 API Stateless & Cloud Migration Demo

Este projeto é um protótipo funcional desenvolvido para o **Demo Day da 🚀 squad-3 (Curso Avanti)**. Ele demonstra a transição de uma infraestrutura física instável para uma arquitetura resiliente em nuvem.

## 📋 Sobre o Projeto
O objetivo é validar a eficácia da conteinerização e dos princípios REST na resolução de problemas críticos de TI, como o tempo de inatividade (downtime) e custos elevados de manutenção.

### Tecnologias Utilizadas:
* **Python & FastAPI**: Para a criação de uma API de alto desempenho e arquitetura Stateless (sem retenção de lixo no servidor).
* **Docker**: Utilizado como "Receita Universal" para garantir a padronização e portabilidade do ambiente
* **HTML/JavaScript**: Interface interativa para simulação de falhas e recuperação em tempo real.

---

## 🏗️ Como a Solução Funciona
### O Problema (Legado)
Servidores físicos são frágeis. Se o hardware falha, o negócio para.
### A Solução (Docker): 
O código é empacotado em um container. O **Dockerfile** permite recriar o servidor inteiro em segundos caso ocorra um erro.
### Resiliência na Nuvem:
Através da simulação, demonstramos como a **AWS** e a elasticidade permitem que o sistema volte ao ar instantaneamente após uma falha.

---

### 🛠️ Como Executar a Demonstração
Para rodar este projeto localmente e ver a "mágica" acontecer:

1. Certifique-se de ter o Docker instalado.

#### Opção 1: Via Docker Compose (Recomendado)
Basta um comando para subir a infraestrutura completa:

```bash
docker-compose up --build
```

#### Opção 2: Via Docker Manual
Caso prefira os comandos individuais:

```bash
docker build -t api-stateless-demo .
docker run -p 8000:8000 api-stateless-demo
```

3. Acesse no navegador: http://localhost:8000

---

## 📈 Impacto no Negócio

### Alta Disponibilidade: 
O sistema se torna imune a falhas de hardware local. 
### Escalabilidade Horizontal: 
A arquitetura permite atender milhares de requisições simultâneas. 
### Entrega Contínua (CI/CD): 
Preparado para esteiras de automação que garantem segurança antes da produção.

---