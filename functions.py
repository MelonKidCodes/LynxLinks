import json
import webbrowser
import subprocess

def addnewlink(a, b, c):
    diffkey = True
    if a == "" or b == "":
        diffkey = False
    else:
        array = json.load(returnarray())
        for item in array:
            if item["shortcut"] == a:
                diffkey = False
                break
        if diffkey == True:
            array.append({"shortcut":a,"link":b,"exe":c})
            savetoarray(json.dumps(array))
    return diffkey

def uselink(a):
    array = json.load(returnarray())
    for item in array:
        if item["shortcut"] == a:
            if item["exe"] == "url":
                webbrowser.open(item["link"],new=2,autoraise=True)
                break
            if item["exe"] == "exe":
                subprocess.call([item["link"]])
                break

def uselinkfromlist(num):
    array = json.load(returnarray())
    if array[num]["exe"] == "url":
        webbrowser.open(array[num]["link"],new=2,autoraise=True)
    if array[num]["exe"] == "exe":
        subprocess.call([array[num]["link"]])

def canuselink(a):
    array = json.load(returnarray())
    for item in array:
        if item["shortcut"] == a:
            return True
    return False

def editshortcut(num, a, b, c):
    array = json.load(returnarray())
    array[num] = {"shortcut":a,"link":b,"exe":c}
    savetoarray(json.dumps(array))

def removeshortcut(num):
    array = json.load(returnarray())
    if len(array) > 0:
        array.pop(num)
        savetoarray(json.dumps(array))

def returnarray():
    array = open("shortcuts.txt","r")
    return array

def savetoarray(array):
    file = open("shortcuts.txt","w")
    file.write(array)

def resetarray():
    file = open("shortcuts.txt","w")
    file.write("[]")

def checkforfile():
    try:
        file = open("shortcuts.txt","r")
    except FileNotFoundError:
        resetarray()
    
    try:
        file = json.load(returnarray())
    except json.decoder.JSONDecodeError:
        resetarray()

#print(json.load(returnarray()))

#addnewlink(input("1>"),input("2>"),input("3>"))
#while True:
    #uselink(input("> "))
