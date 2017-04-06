from Tkinter import *
#import homePage
#from homePage import *

class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Login Page")

        #self.label = Label(master, text = "Welcome!")
        #self.label.pack()

        labelUsername = Label(master, text = "Username")
        #labelUsername.pack(side = LEFT)
        labelUsername.grid(row = 0, column = 0)

        entryUsername = Entry(master, bd = 5)
        #entryUsername.pack(side = RIGHT)
        entryUsername.grid(row = 0, column = 1)

        labelPassword = Label(master, text = "Password")
        #labelPassword.pack(side = LEFT)
        labelPassword.grid(row = 1, column = 0)

        entryPassword = Entry(master, bd = 5, show = "*")
        #entryPassword.pack(side = RIGHT)
        entryPassword.grid(row = 1, column = 1)

        """These are the Buttons for the page"""

        # need to set things as callbacks so they dont get called immediately, so lambda
        self.loginButton = Button(master, text = "login", command = lambda: self.login(entryUsername.get(), entryPassword.get()))
        self.loginButton.grid(row = 2, column = 0)

        self.closeButton = Button(master, text = "close", command = self.closeWindow)
        self.closeButton.grid(row = 2, column = 1)


    def login(self, username, password):

        print username
        print password

        userInfo = {
            "user": "pass",
            "jerm": "pass"
        }

        if ((username in userInfo) & (password in userInfo.values())):
            print "You logged in"
            self.newWindow = Tk()
            #self.app = HomePage(self.newWindow)
            self.master.destroy()

        else:
            print "either password or username was incorrect, try again"

        #DBusername = call SQL command to get username
        #DBPassword = call SQL command to get password

        """
        need SQL statements to go here 
        this will get the username (key) and password from the DB

        #if (SQL.username ==  username & SQL.password == password)

        if (username.exists() && password.exists()):
            print "You logged in"

            #want to make a new window and go to that (home page) on successful login
            #how do I link it to a new file???? --> want to call homePage.py basically

            self.newWindow = Tk()
            self.app = HomePage(self.newWindow)
            self.master.destroy()

        #for an unsuccessful login, print error message
        else:
            print "Sorry, either your username or password did not match, please try again"
        """

        

    def closeWindow(self):
        self.master.destroy()


master = Tk()
my_gui = LoginPage(master)
master.mainloop()