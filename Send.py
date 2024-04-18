from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
def send(screen,test):
    try:
        """
           Send emails.

           Args:
           - screen (GUI): GUI object for getting email parameters.
           - test (bool): Indicates whether to use test credentials.
           """
        #
        if test:
        # test case
            email, password, to, subject, text = "alih11221@outlook.com", ".m?ai7mo", "alih96286@gmail.com", "lab3", "hardcodded test case"
        else:
            email, password, to, subject, text = screen.getatt()  # get paremeters from gui
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
