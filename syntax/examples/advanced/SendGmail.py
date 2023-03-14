import smtplib
import email.message

corpo_email = """
<p>...Texto a ser enviado...</p>
<p>Essa parte em HTML requer os P no inicio e final de cada paragráfo</p>
"""

msg = email.message.Message()
msg['Subject'] = "Teste Python 1" # Asssunto do email
msg['From'] = 'Remetente'
msg['To'] = 'Destinatario'
password = 'senhaGmail'
msg.add_header('Content-Type', 'text/html')
msg.get_payload(corpo_email)

s = smtplib.SMTP('smtp.gmail.com: 587')
s.starttls()
#login
s.login(msg[['From'], password])
s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
print('Email enviado\n')