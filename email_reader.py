from imbox import Imbox
from datetime import datetime
import pandas as pd

username = ''
password = open('senha', 'r').read() # modo de leitura: r; modo de edição: w; modo de edição de bytes: wb
host = 'imap.gmail.com' # provedor de email, servidor imap

# é a classe imbox que instanciada, vai montar a conexão com o servidor imap e daí vamos conseguir a conexão
mail = Imbox(host, username=username, password=password, ssl=True) # o ssl garante a conexão segura
messages = mail.messages(unread=True)
# o parâmetro unread é um filtro sem ele todos os emails seriam lidos, temos o parâmetro flagged, unflagged, emails sent_from, sent_to, por datas com date__lt(lower then, abaixo de) ou date__gt(greater then), também poderia ser por assunto

# len(messages)

for (uid, message) in messages: # o iterável retorna uma tupla, assim precisamos desempacotar
    message.subject # pegando o assunto da mensagem
    message.body # retorna o corpo da mensagem em html
    message.sent_from # quem enviou
    message.sent_to # para quem foi enviado
    message.cc # quem foi cópia
    message.headers # cabeçalho
    message.date # quando foi enviada
    message.attachments # anexo
    if len(message.attachments) > 0:
        # esse loop baixaria todos os anexos do meu email
        for attach in message.attachments:
            file = open('anexos/invite.ics', 'wb') # modo de escrever com bytes
            attach['content'].seek(0) # reseta o ponteiro
            file.write(attach['content'].read()) # escreve a leitura do content do anexo
            file.close() # finaliza o file
        break