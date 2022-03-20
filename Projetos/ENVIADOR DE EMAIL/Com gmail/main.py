"""
Projeto de iniciante - Enviador de emails
Objetivo:
    Enviar email simples utilizando python
Passos: 
    - Ative a opção de acesso a apps menos seguros na aba de 
      segurança da sua conta google Acesso
    - preencha as variáveis de entrada  
"""
from support import regulate, envelop
from best_support import adapt_message
import yagmail

#* VARIÁVEIS DE ENTRADA
user_email = 'example@gmail.com' # email

password = 'password' # senha

addressee_emails = ['recipient@gmail.com']# destinatários

cc = [''] # Cópia de email - OPCIONAL

bcc = [''] # Cópia oculta de email - OPCIONAL

subject = 'test' # Assunto 

 # corpo do email
email_body = \
'''
message
'''
# O corpo do email aceita personalização html e corpo python

attachments=[''] # anexos - OPCIONAL

#* PROGRAMA
sender = yagmail.SMTP(user=user_email, password=password)
sender.send(to= addressee_emails, subject=subject,
            contents=envelop(email_body),
            attachments=regulate(attachments),
            cc=regulate(cc), bcc=regulate(bcc)
)
