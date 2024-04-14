from GUI import GUI
from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
screen=GUI()
import smtplib
myEmail,password=screen.getEmailAndpass()
# connect to serverTCP
if screen.recieve:
    import imaplib
    import email
    try:
        imap=imaplib.IMAP4_SSL("outlook.office365.com")
        print('succesful connection')
        #login to the account
        imap.login(myEmail,password)
        print('succesful login')
        #choose from where to get the message
        imap.select('Inbox')
        # return number of each message in a list
        _,messages=imap.search(None,"ALL")
        #get last message ID
        a=messages[0].split()
        lastMsg=a[len(a)-1]
        # Fetch the whole message  using the IMAP protocol
        _,whole=imap.fetch(lastMsg,"RFC822")
        #get information of last message
        message=email.message_from_bytes(whole[0][1])
        message_body=""
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                message_body += part.get_payload(decode=True).decode(part.get_content_charset())
        screen.show_mail(f"From: {message.get("From")}\n"+
               f"to: {message.get("To")}\n"+
              f"Subject: {message.get("Subject")}\n" +
               f"body: {message_body}")
        exit(1)

    except SMTPAuthenticationError:  # catch incorrect mail or password
        print("Login failed. Please check your email and password.")
    except Exception as e:
        print("An error occurred:", e)

email,password,to,subject,text=screen.getatt()
try:
    server = smtplib.SMTP('smtp.office365.com', 587)
    print('succesful connection')
    # initiate connection
    server.starttls()
    server.ehlo()
    server.login(email,password)
    print('succesful login')
    msg = MIMEMultipart()
    msg['from'] = email
    msg['to'] = to
    msg['subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    # send the message
    server.sendmail(email, to, msg.as_string())
    print('msg sent')
    server.close()
except SMTPAuthenticationError:# catch incorrect mail or password
    print("Login failed. Please check your email and password.")
except Exception as e:
    print("An error occurred:", e)
# make the msg parts to send
