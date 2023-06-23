import smtplib

# Set up the proxy server
proxy_server = 'localhost'
proxy_port = 8080

# Configure email settings
sender = 'sender@example.com'
receiver = 'receiver@example.com'
subject = 'Subject: Intercepted Email'
message = 'This is the intercepted email message.'

# Connect to the SMTP server via proxy
smtp_proxy = smtplib.SMTP(proxy_server, proxy_port)
smtp_proxy.ehlo()

# Send the intercepted email
smtp_proxy.sendmail(sender, receiver, f'{subject}\n\n{message}')

# Close the proxy connection
smtp_proxy.quit()
