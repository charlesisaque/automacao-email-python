# Automação de Envio de Emails com Python
Este projeto permite enviar emails automaticamente a partir de uma planilha Excel contendo os endereços e mensagens.

## 🚀 Tecnologias usadas
- Python 3
- smtplib
- email
- pandas

## 📂 Estrutura do Projeto
- `enviar_email.py` → Script principal
- `contatos.xlsx` → Planilha com colunas `Nome`, `Email`, `Mensagem`

## ⚙️ Como usar
1. Ative a **verificação em 2 etapas** do Gmail.
2. Gere uma **Senha de App** no [Google Account](https://myaccount.google.com/apppasswords).
3. Instale as dependências:
   ```bash
   pip install pandas openpyxl
4. Coloque sua senha de app no código:
`senha = "SUA_SENHA_DE_APP_AQUI"`

6. Execute o script no terminal: 
`python enviar_email.py`

## 📌 Exemplo de Uso
- Enviar mensagens personalizadas em massa.
- Automatizar respostas para clientes.
- Disparar comunicados internos.
