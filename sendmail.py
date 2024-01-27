import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Email Account Infos 
def sendmail(recepients,body):
    email_sender_account = ""
    email_sender_username = "" # you can use just example@mail.com instead of account name and username 
    email_sender_password = ""
    email_smtp_server = "smtp.gmail.com"
    email_smtp_port = 587
    # Email Content
    email_recepients = recepients
    email_subject = "Very important message"
    email_body = body

    # login to email server
    server = smtplib.SMTP(email_smtp_server, email_smtp_port)
    server.starttls()
    server.login(email_sender_username, email_sender_password)
    for receipent in email_recepients:
        print(f"Sending email to {receipent}")
        message = MIMEMultipart("alternative") #to use account name and username
        message['From'] = email_sender_account
        message['To'] = receipent
        message['Subject'] = email_subject
        message.attach(MIMEText(email_body, 'html'))
        text = message.as_string()
        server.sendmail(email_sender_account,receipent, text)

    server.quit()
    
if __name__=="__main__":
    recepients=["example@mail.com"]
    sendmail(recepients,body="I am trying something with python")