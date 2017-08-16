from appJar import gui
from logic import *

app = gui()
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.go()