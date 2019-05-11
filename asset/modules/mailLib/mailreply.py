from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 

def shootMail(details): 
    # create message object instance
    msg = MIMEMultipart()
    message = details['Message']
    
    # setup the parameters of the message
    password = details['Password']
    msg['From'] = details['Sender']
    msg['To'] = details['Receiver']
    msg['Subject'] = details['Subject']
 
 
    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    try:
    # Login Credentials for sending the mail
        server.login(msg['From'], password)
    except:
        print("Error")
        return "Password Mismatch Try Again"
 
 
    msg.attach(MIMEText(message, 'plain'))
    server.sendmail(msg['From'], msg['To'], msg.as_string())
 
    server.quit()
 
    print("successfully sent email to %s:" % (msg['To']))
    return "Success"