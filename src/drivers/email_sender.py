import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "fyzt45ch2plk5rcj@ethereal.email"
    login = "fyzt45ch2plk5rcj@ethereal.email"
    password = "6rrUx4ynMZdj8x6mVU"

    msg = MIMEMultipart()
    msg['From'] = "viagens_confirmar@email.com"
    msg['To'] = ", ".join(to_addrs)

    msg['Subject'] = "Confirmação de Viagem"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()