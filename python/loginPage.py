from Tkinter import *
#import homePage
#from homePage import *
import MySQLdb

class LoginPage:
    def __init__(self, master):
        self.master = master
        master.title("Login Page")

        #Database Connection
        db = MySQLdb.connect(host = "localhost", user="root", db="HERO" ) # I don't have a password for mysql
        curr = db.cursor()

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
        self.loginButton = Button(master, text = "login", command = lambda: self.login(entryUsername.get(), entryPassword.get(), curr))
        self.loginButton.grid(row = 2, column = 0)

        self.closeButton = Button(master, text = "close", command = self.closeWindow)
        self.closeButton.grid(row = 2, column = 1)


    def login(self, username, password, curr):

        print username
        print password

        curr.execute("SELECT * FROM User WHERE Username = %s AND Password = SHA1(%s)", (username, password,))
        result = curr.fetchone()

        if result is not None: # if the result isn't None then there is a user/password combination match
            user_type = result[2] # this is the type of user i.e. admininistrator, manager, regular
            print "You logged in"
            print "User Type is " + user_type
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
