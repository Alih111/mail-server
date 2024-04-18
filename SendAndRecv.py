from GUI import GUI
import Recv
import Send

screen=GUI()
test=True
if not test:
    screen.firstScreen()
screen.recieve=True
# connect to serverTCP
if screen.recieve:
    Recv.Recv(screen,test)
else:
    Send.send(screen,test)
