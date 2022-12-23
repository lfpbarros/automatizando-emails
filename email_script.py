from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('senha', 'r').read()
email_origem = ''

email_destino = ('')

assunto = 'Orçamento de produtos'
body = open('corpo_email.txt', 'r').read()

mensagem = EmailMessage()

mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto

mensagem.set_content(body)

safe = ssl.create_default_context()
# garente que o email seja criptografado com tecnologia ssl

# quando abrimos alguma conexão com o python, precisamos, fechá-la
# o with é uma estrutura do python que permite a abertura de conexões e ao final dela, essa conexão é encerrada 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
