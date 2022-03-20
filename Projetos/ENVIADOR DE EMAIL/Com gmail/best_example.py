"""
Exemplo de uso do best.py
O exemplo mostra o envio de mensagens aos responsáveis
sobre a situação final dos alunos
A pasta result mostra os resultados desse programa
"""
from support import regulate, envelop
from best_support import (salutation, adapt_situation, adapt_gender,
adapt_result, check_dinamic_email_objects)
from csvhelper import CsvHelper
from best_support import *
import yagmail
import os


#* VARIÁVEIS DE ENTRADA
user_email = 'example@gmail.com' # email
password = 'password' # senha
addressee_emails = ['example0001@gmail.com', 'example0002@gmail.com', 'example0003@gmail.com'] # destinatários
cc = [''] # Cópia de email - OPCIONAL
bcc = [''] # Cópia oculta de email - OPCIONAL
subject = 'Resultado final escolar - 2021' # Assunto
attachments=['boletim000.png', 'boletim001.jpg', 'boletim002.jpg'] 


#* CSV VARIÁVEIS DE ENTRADA
csv_name = 'escola'
headers = ['Nome', 'Situação', 'Nota', 'Gênero','Responsável']
# as informações abaixo devem ter a mesma quantidade de dados
nomes = ['Rafael', 'Miguel', 'Marcela']
situacoes = ['a', 'a', 'r'] # r = reprovado , a = aprovado
generos = ['m', 'm', 'f'] # m = masculino, f = feminino
notas = ['9.5', '7.5', '6.0']
responsaveis = ['Francisca', 'Raimundo', 'Maria']


#* MANIPULANDO CSV
csvfile = CsvHelper(csv_name)
csvfile.create(headers)
csvfile.fill(nomes, situacoes, notas, generos, responsaveis)
csvfile.view()
db = csvfile.read() # dados da tabela

#* ENVIANDO EMAILS
sender = yagmail.SMTP(user=user_email, password=password)
check_dinamic_email_objects(len(db)-1, addressee_emails, attachments)
for id_, nome, situacao, nota, genero, responsavel in db[1:]: # id_ é obrigatório
    cp = int(id_) - 1 # count process
    # <br> serve para pular a linha na renderização do email
    base_message = f'''\
   {salutation()} {responsavel}, {adapt_gender(genero)} {nome}
está {adapt_situation(situacao)}, pois sua nota final é {nota.replace('.', ',')}. {adapt_result(nota)}
<br>Ass: Diretor
'''
    sender.send(to= regulate(addressee_emails[cp]),
                subject=subject,
                contents=envelop(base_message),
                attachments=regulate(attachments[cp]),
                cc=regulate(cc),
                bcc=regulate(bcc))
    