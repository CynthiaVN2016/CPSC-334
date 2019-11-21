import smtplib, ssl, socket, sys

port = 465  # For SSL
password = 
sender_email = "animeonveoh@gmail.com"
receiver_email = "cynthiavu@gmail.com"
IPAddr = sys.argv[2]
message = """\
Subject: Hi there

The current IP address is: """ + IPAddr

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, "mscynthiavu@gmail.com", message)