import tkinter as tk
import re
class GUI():
    def __init__(self):
        self.email_entry = None
        self.password_entry = None
        self.root = None
        self.email=None
        self.password=None
        self.to_entry=None
        self.subject_entry=None
        self.msg_entry=None
        self.to=None
        self.subject=None
        self.msg=None
        self.recieve=False

    def validate_email(self,email):
        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)
    def show_error_message(self,error_msg):
        error_window = tk.Tk()
        error_window.title("Error")
        error_window.geometry("300x100")
        error_label = tk.Label(error_window, text=error_msg, foreground="red",font=("Arial", 12))
        error_label.pack(padx=20, pady=20)


    def show_mail(self, error_msg):
        error_window = tk.Tk()
        error_window.title("mail")
        error_window.geometry("600x300")
        error_label = tk.Label(error_window, text=error_msg, foreground="blue", font=("Arial", 12))
        error_label.pack(padx=20, pady=20)
        error_window.mainloop()
    def on_submit1(self):
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        changeScreen=True
        if self.email == '' or self.password == '' :
            self.show_error_message("please enter your information")
            changeScreen=False
        if not self.validate_email(self.email) and changeScreen:
            changeScreen = False
            self.show_error_message("please enter a valid email")
        if changeScreen:
            self.root.destroy()
            self.secondScreen()
        else:
            self.firstScreen()
    def firstScreen(self):
        if self.root is None:
            self.root=tk.Tk()
            self.root.title("login")
            email_label = tk.Label(self.root, text="Email:")
            email_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

            # Create an entry widget for email
            self.email_entry = tk.Entry(self.root,width=40)
            self.email_entry.grid(row=0, column=1, padx=5, pady=5)

            # Create a label for password
            password_label = tk.Label(self.root, text="Password:")
            password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

            # Create an entry widget for password
            self.password_entry = tk.Entry(self.root, show="*",width=40)  # donnot show text when writing password
            self.password_entry.grid(row=1, column=1, padx=5, pady=8)

        # Create a submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.on_submit1)
        submit_button.grid(row=2, columnspan=2, padx=5, pady=5)
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.root.mainloop()
    def closeWindow(self):
        self.root.destroy()
        exit(1)
    def on_submit2(self):
        self.recieve=False
        changeScreen=True
        self.to = self.to_entry.get()
        self.subject = self.subject_entry.get()
        self.msg = self.msg_entry.get("1.0", "end-1c")
        if self.to == '' or self.subject == '' or self.msg == '':
            self.show_error_message("please enter valid data")
            changeScreen=False
        if not self.validate_email(self.to) and changeScreen :
            self.show_error_message("please enter a valid email")
            changeScreen = False
        if changeScreen:
            self.root.destroy()
    def on_submit3(self):
        self.recieve=True
        self.root.destroy()
    def secondScreen(self):
        self.root = tk.Tk()
        self.root.title("send email")
        self.root.geometry("620x300")  # set window size

        # Create labels and entry widgets
        to_label = tk.Label(self.root, text="To:")
        to_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.to_entry = tk.Entry(self.root, width=60)  # Increase width and set font
        self.to_entry.grid(row=0, column=1, padx=5, pady=5)

        subject_label = tk.Label(self.root, text="Subject:")
        subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.subject_entry = tk.Entry(self.root, width=60)
        self.subject_entry.grid(row=1, column=1, padx=5, pady=5)

        msg_label = tk.Label(self.root, text="Message:")
        msg_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.msg_entry = tk.Text(self.root, width=60, height=10)
        self.msg_entry.grid(row=2, column=1, padx=5, pady=10)

        # create submit button
        submit_button = tk.Button(self.root, text="send", command=self.on_submit2)
        submit_button.grid(row=3, column=1, padx=5, pady=5)
        recieve_button = tk.Button(self.root, text="recieve", command=self.on_submit3)
        recieve_button.grid(row=0, column=2, padx=10, pady=5)
        #close window action
        self.root.protocol("WM_DELETE_WINDOW", self.closeWindow)
        # show screen
        self.root.mainloop()
    def getatt(self):
        if None in (self.email, self.password, self.to, self.subject, self.msg):
            return None
        if not self.validate_email(self.email):
            return None
        if not self.validate_email(self.to):
            return None
        return self.email,self.password,self.to,self.subject,self.msg
    def getEmailAndpass(self):
        if None in (self.email, self.password):
            return None
        return self.email,self.password







