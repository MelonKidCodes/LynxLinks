from tkinter import *
from tkinter.font import BOLD, Font
from functions import *
from math import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

def updatebuttons():
    root.after(100, updatebuttons)
    if openprograminput["foreground"] == "grey":
        openprogrambutton["state"] = DISABLED
    else:
        if canuselink(openprograminput.get(1.0,"end-1c")):
            openprogrambutton["state"] = ACTIVE
        else:
            openprogrambutton["state"] = DISABLED
    
    if createshortcutinput[0]["foreground"] == "grey" or createshortcutinput[1]["foreground"] == "grey":
        createshortcutbutton["state"] = DISABLED
    else:
        if createshortcutinput[0].get(1.0,"end-1c") == "" or createshortcutinput[1].get(1.0,"end-1c") == "":
            createshortcutbutton["state"] = DISABLED
        else:
            if canuselink(createshortcutinput[0].get(1.0,"end-1c")):
                createshortcutbutton["state"] = DISABLED
            else:
                createshortcutbutton["state"] = ACTIVE

def updateshortcutslist():
    global shortcutslist
    array = json.load(returnarray())

    for item in shortcutslist:
        item[0].destroy()
        item[1].destroy()
        item[2].destroy()

    counter = 0
    shortcutslist = []
    for item in array:
        height = ceil(len(str(item["link"]))/32)
        shortcutslist.append([])
        shortcutslist[counter].append(Frame(shortcutslistframe, bg = "#90DF90"))
        shortcutslist[counter].append(Text(shortcutslist[counter][0], width = 8, height = height))
        shortcutslist[counter][1].insert(0.0,str(item["shortcut"]))
        shortcutslist[counter].append(Text(shortcutslist[counter][0], width = 32, height = height))
        shortcutslist[counter][2].insert(0.0,str(item["link"]))
        shortcutslist[counter].append(Button(shortcutslist[counter][0], text = "Save", width = 4, height = height, bg = "#DDFFDD", command = lambda counter = counter: saveshortcutedit(counter)))
        shortcutslist[counter][3]["state"] = DISABLED
        shortcutslist[counter].append(Button(shortcutslist[counter][0], text = "Run", width = 4, height = height, bg = "#DDDDFF", command = lambda counter = counter: runshortcut(counter)))
        shortcutslist[counter].append(Button(shortcutslist[counter][0], text = "🗑", width = 2, height = height, bg = "#FFDDDD", command = lambda counter = counter: deleteshortcut(counter)))

        shortcutslist[counter][0].pack()
        shortcutslist[counter][1].pack(side="left")
        shortcutslist[counter][2].pack(side="left")
        shortcutslist[counter][3].pack(side="left")
        shortcutslist[counter][4].pack(side="left")
        shortcutslist[counter][5].pack(side="left")

        counter += 1

def updateshortcutlistsavebuttons():
    root.after(100, updateshortcutlistsavebuttons)
    global shortcutslist
    array = json.load(returnarray())

    counter = 0
    for item in array:
        if str(item["shortcut"]) == shortcutslist[counter][1].get(1.0,"end-1c") and str(item["link"]) == shortcutslist[counter][2].get(1.0,"end-1c"):
            shortcutslist[counter][3]["state"] = DISABLED
        else:
            counter2 = 0
            identicalshortcut = False
            for item2 in array:
                if shortcutslist[counter][1].get(1.0,"end-1c") == str(item2["shortcut"]) and counter2 != counter:
                    identicalshortcut = True
                    break
                counter2 += 1
            if identicalshortcut:
                shortcutslist[counter][3]["state"] = DISABLED
            else:
                shortcutslist[counter][3]["state"] = ACTIVE
        counter += 1

def updateshortcutlisttextboxheight():
    root.after(100, updateshortcutlisttextboxheight)
    global shortcutslist

    for item in shortcutslist:
        height = ceil(len(str(item[2].get(1.0,"end-1c")))/32)
        item[1]["height"] = height
        item[2]["height"] = height
        item[3]["height"] = height
        item[4]["height"] = height
        item[5]["height"] = height

def saveshortcutedit(counter):
    global shortcutslist
    editshortcut(counter, shortcutslist[counter][1].get(1.0, "end-1c").replace("\n",""), shortcutslist[counter][2].get(1.0, "end-1c").replace("\n",""), "url")

def runshortcut(counter):
    global shortcutslist
    uselinkfromlist(counter)

def deleteshortcut(counter):
    global shortcutslist
    removeshortcut(counter)
    updateshortcutslist()

def openprogram():
    uselink(openprograminput.get(1.0,"end-1c"))
    openprograminput.delete(0.0, "end")

def createshortcut():
    addnewlink(createshortcutinput[0].get(1.0,"end-1c").replace("\n",""),createshortcutinput[1].get(1.0,"end-1c").replace("\n",""),"url")
    #if urlorexe["text"] == "URL":
        #addnewlink(createshortcutinput[0].get(1.0,"end-1c").replace("\n",""),createshortcutinput[1].get(1.0,"end-1c").replace("\n",""),"url")
    #else:
        #addnewlink(createshortcutinput[0].get(1.0,"end-1c").replace("\n",""),createshortcutinput[1].get(1.0,"end-1c").replace("\n",""),"exe")
    createshortcutinput[0].delete(0.0, "end")
    createshortcutinput[1].delete(0.0, "end")
    updateshortcutslist()

def swapurlorexemode():
    if urlorexe["text"] == "URL":
        urlorexe["text"] = "EXE"
    else:
        urlorexe["text"] = "URL"

def openprograminputclickedon_callback(event):
    openprograminput.delete(0.0, "end")
    openprograminput["foreground"] = "black"
    openprograminput.unbind("<FocusIn>")
    return None

def createshortcutinputclickedon_callback1(event):
    createshortcutinput[0].delete(0.0, "end")
    createshortcutinput[0]["foreground"] = "black"
    createshortcutinput[0].unbind("<FocusIn>")
    return None

def createshortcutinputclickedon_callback2(event):
    createshortcutinput[1].delete(0.0, "end")
    createshortcutinput[1]["foreground"] = "black"
    createshortcutinput[1].unbind("<FocusIn>")
    return None

checkforfile()

root = Tk()
app = Window(root)
root.wm_title("Shortcuts Menu")
root.geometry("480x640")
root.configure(background = "#90DF90")

titlefont = [Font(root, size=48, weight=BOLD),Font(root, size=20, weight=BOLD)]
title = [Label(root, text = "Lynx Links", bg = "#90DF90", font = titlefont[0]), Label(root, text = "Coding Ninjas", bg = "#90DF90", font = titlefont[1])]
textboxes = [Label(root, text = "", bg = "#90DF90"),Label(root, text = "Open Shortcut", bg = "#90DF90"),Label(root, text = "", bg = "#90DF90"),Label(root, text = "Create new shortcut", bg = "#90DF90"),Label(root, text = "", bg = "#90DF90"),Label(root, text = "Your shortcuts:", bg = "#90DF90")]

openprograminputframe = Frame(root, bg = "#90DF90")
openprograminput = Text(openprograminputframe, height = 1, width = 32, fg = "grey")
openprograminput.insert(0.0, "Input shortcut ID here")
openprograminput.bind("<FocusIn>", openprograminputclickedon_callback)
openprogrambutton = Button(openprograminputframe, text = "Run", width = 6, bg = "#DDFFDD", command=openprogram)
openprogrambutton["state"] = DISABLED

shortcutinputframe = Frame(root, bg = "#90DF90")
createshortcutinput = [Text(shortcutinputframe, height = 1, width = 8, fg = "grey"),Text(shortcutinputframe, height = 1, width = 32, fg = "grey")]
createshortcutinput[0].insert(0.0, "ID")
createshortcutinput[0].bind("<FocusIn>", createshortcutinputclickedon_callback1)
createshortcutinput[1].insert(0.0, "Shortcut URL or filepath")
createshortcutinput[1].bind("<FocusIn>", createshortcutinputclickedon_callback2)
createshortcutbutton = Button(shortcutinputframe, text = "Add", width = 6, bg = "#DDFFDD", command=createshortcut)
createshortcutbutton["state"] = DISABLED
urlorexe = Button(shortcutinputframe, text = "URL", width = 6, command=swapurlorexemode)

shortcutslistframe = Frame(root, bg = "#90DF90")
shortcutslist = []

title[0].pack()
title[1].pack()

textboxes[0].pack()
textboxes[1].pack()
openprograminputframe.pack()
openprograminput.pack(side="left")
openprogrambutton.pack(side="left")
textboxes[2].pack()
textboxes[3].pack()
shortcutinputframe.pack()
createshortcutinput[0].pack(side="left")
createshortcutinput[1].pack(side="left")
#urlorexe.pack(side="left")
createshortcutbutton.pack(side="left")
textboxes[4].pack()
textboxes[5].pack()
shortcutslistframe.pack()

root.after(10, updatebuttons)
root.after(10, updateshortcutslist)
root.after(10, updateshortcutlistsavebuttons)
root.after(10, updateshortcutlisttextboxheight)

root.mainloop()