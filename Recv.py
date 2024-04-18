import imaplib
import email
from smtplib import SMTPAuthenticationError
from plyer import notification
import time
def Recv(screen,test):
    """
                    Receive emails from the inbox.

                    Args:
                    - screen (GUI): GUI object for displaying messages.
                    - test (bool): Indicates whether to use test credentials."""
    notified=[]
    if test:
        myEmail, password = "alih11221@outlook.com", ".m?ai7mo"
    else:
        myEmail, password = screen.getEmailAndpass()
    #make connection with imap server
    imap = imaplib.IMAP4_SSL("outlook.office365.com")
    print('succesful connection')
    # login to the account
    imap.login(myEmail, password)
    print('succesful login')
    # choose from where to get the message
    imap.select('Inbox')
    while True:
        try:

            # return number of each message in a list
            _,messages=imap.search(None,"UNSEEN")
            # separte email ids and put them in a list
            a=messages[0].split()
            print(a)
            #check if there is unseen emails
            if a:
                # get last message ID
                lastMsg=a[-1]
                #checks if i was notified about this email before or not
                # notify me only if i wasnot notified before
                if lastMsg not in notified:

                    # Fetch the whole message  using the IMAP protocol
                    _,whole=imap.fetch(lastMsg,"RFC822")

                    #get information of last message
                    message=email.message_from_bytes(whole[0][1])
                    message_body=""
                    for part in message.walk():
                        if part.get_content_type() == "text/plain":
                            message_body += part.get_payload(decode=True).decode(part.get_content_charset())

                    notification_title = f"New Email from {message['From']}"
                    notification_text = f" {message['Subject']}"
                    notification.notify(
                        title=notification_title,
                        message="subject " + notification_text,
                        app_icon=None,  # You can specify an icon path here
                        timeout=10,  # Notification will disappear after 10 seconds
                    )
                    # add email id to notified emails
                    notified.append(lastMsg)
                    # Mark the message as unseen
                    imap.store(lastMsg, '-FLAGS', '\\Seen')

        except SMTPAuthenticationError:  # catch incorrect mail or password
            print("Login failed. Please check your email and password.")
        except Exception as e:
            print("An error occurred:", e)
    # delay before checking again
        time.sleep(10)