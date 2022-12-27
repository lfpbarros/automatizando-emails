from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

email_senha = open('senha', 'r').read()
email_origem = ''

email_destino = ('')

assunto = 'Orçamento de produtos'
body = open('corpo_email_html.txt', 'r', encoding='utf-8').read()
# o encoding é muito importante para corrigir a questão da acentuação.

mensagem = EmailMessage()

mensagem['From'] = email_origem
mensagem['To'] = email_destino
mensagem['Subject'] = assunto

anexo_path = 'imagem.jpg'
mime_type, mime_subtype = mimetypes.guess_type(anexo_path)[0].split('/') # carregando a imagem, o caminho precisa ser possível do python entender, daí há o split do primeiro valor e o atribuímos a duas variáveis

mensagem.set_content(body, subtype='html')

safe = ssl.create_default_context()
# garente que o email seja criptografado com tecnologia ssl

with open(anexo_path, 'rb') as ap:
    mensagem.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=anexo_path)
    # adicionado o anexo a mensagem

# quando abrimos alguma conexão com o python, precisamos, fechá-la
# o with é uma estrutura do python que permite a abertura de conexões e ao final dela, essa conexão é encerrada 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
