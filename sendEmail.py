import smtplib, ssl, socket

port = 465  # For SSL
password = input("Type your password and press enter: ")
sender_email = "animeonveoh@gmail.com"
receiver_email = "cynthiavu@gmail.com"
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
message = """\
Subject: Hi there

The name is: """ + hostname + "\n" + "The current IP address is: " + IPAddr

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, "mscynthiavu@gmail.com", message)