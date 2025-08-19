import pandas as pd
import smtplib
from email.message import EmailMessage

# Lê os dados da planilha
tabela = pd.read_excel("emails.xlsx")

# Seu e-mail e senha de app (se for Gmail, veja abaixo como gerar a senha)
meu_email = "SEUEMAIL"
senha = "SUASENHADEAPP"

# Configura o servidor do Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(meu_email, senha)

# Envia os e-mails da planilha
for i, linha in tabela.iterrows():
    nome = linha["Nome"]
    email_destino = linha["Email"]
    mensagem = linha["Mensagem"]

    email = EmailMessage()
    email['From'] = meu_email
    email['To'] = email_destino
    email['Subject'] = f"Olá {nome}, mensagem automática"
    email.set_content(mensagem)

    server.send_message(email)
    print(f"✅ Mensagem enviada para {nome} ({email_destino})")

server.quit()
