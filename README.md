# 💡 Sistema de Iluminação Automatizada (Simulador em Python)

Este projeto é um **simulador de automação residencial** focado no **controle automático de iluminação**.  
Foi desenvolvido em **Python**, pensado para rodar **apenas no Windows**, sem necessidade de sensores ou dispositivos físicos.

A ideia é demonstrar, de forma didática, **como funcionaria um sistema automatizado** que liga e desliga luzes com base em condições como **luminosidade ambiente**, **horário do dia** ou **presença de pessoas** — tudo simulado em console.

---

## 🎯 Objetivo

Simular um sistema de **iluminação inteligente** que:
- Liga as luzes automaticamente quando o ambiente está escuro;
- Desliga quando há luz suficiente;
- Permite alternar manualmente o estado das luzes;
- Exibe logs em tempo real para acompanhar o comportamento do sistema.

---

## 🧰 Tecnologias utilizadas

- **Python 3.10+**
- **Módulo `time`** (para simulação em tempo real)
- **Módulo `random`** (para gerar variações simuladas de luminosidade)
- **Sem dependências externas.**  
  — não é necessário instalar nada além do Python.

---

## 🗂️ Estrutura do projeto

```
iluminacao_automatica/ main.py # Código principal do simulador
├── config.py # Configurações de limiar e intervalo
├── requirements.txt # (opcional) lista de dependências
└── README.md # Documentação do projeto"

```

---

## ⚙️ Como executar no Windows

### 1️⃣ Instalar o Python
Baixe e instale o Python (versão 3.10 ou superior) pelo site oficial:  
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

Durante a instalação, **marque a opção “Add Python to PATH”**.

---

### 2️⃣ Baixar o projeto

Você pode:
- **Clonar o repositório** pelo Git:
  ```bash
  git clone https://github.com/seuusuario/iluminacao_automatica.git
