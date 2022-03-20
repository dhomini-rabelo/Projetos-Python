"""
Projeto de iniciante - Enviador de emails
Descrição:
    Este é um programa baseado no main.py, porém melhor com 
    filtragens otimizadas para emails
Objetivo:
    Enviar emails em escala usando python com opção de 
    personalização para o corpo do email com uso de arquivo csv 
Passos: 
    - Ative a opção de acesso a apps menos seguros na aba de 
      segurança da sua conta google Acesso
    - preencha as variáveis de entrada 
    - manipule o csv
    - crie filtragens
    - envie o email
"""
from csvhelper import CsvHelper
from support import regulate, envelop
from best_support import *
import yagmail


#* VARIÁVEIS DE ENTRADA
user_email = 'example@gmail.com' # email

password = 'your password' # senha

addressee_emails = ['recipient@gmail.com'] # destinatários

cc = [''] # Cópia de email - OPCIONAL

bcc = [''] # Cópia oculta de email - OPCIONAL


subject = 'Sla' # Assunto

email_body = \
'''
Write your message here
''' # corpo do email
# O corpo do email aceita personalização html e/ou python
attachments=[''] # anexos - OPCIONAL


#* CSV VARIÁVEIS DE ENTRADA
csv_name = 'escola'
headers = []
field1 =[]
field2 = []

#* MANIPULANDO CSV
# tips
csvfile = CsvHelper(csv_name)
csvfile.create(headers)
csvfile.fill(field1, field2)
csvfile.view()
db = csvfile.read() # dados da tabela o indice 0 é o header


#* ENVIANDO EMAILS
sender = yagmail.SMTP(user=user_email, password=password)
check_dinamic_email_objects(len(db)-1, addressee_emails)
for id_, field1, field2 in db[1:]: # id_ é obrigatório
    cp = int(id_) - 1 # count process
    # <br> serve para pular a linha na renderização do email
    base_message = f'''\
        write yor message here
    '''
    sender.send(to= regulate(addressee_emails[cp]),
                subject=subject,
                contents=envelop(base_message),
                attachments=regulate(attachments),
                cc=regulate(cc),
                bcc=regulate(bcc))