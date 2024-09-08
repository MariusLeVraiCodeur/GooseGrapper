import tkinter.messagebox
import requests
import bs4
import tkinter
import os
import winsound

os.system("cls")
print(" __    __   ______   __    __  __    __ ")
print("/  |  /  | /      \ /  \  /  |/  |  /  |")
print("$$ |  $$ |/$$$$$$  |$$  \ $$ |$$ | /$$/ ")
print("$$ |__$$ |$$ |  $$ |$$$  \$$ |$$ |/$$/  ")
print("$$    $$ |$$ |  $$ |$$$$  $$ |$$  $$<   ")
print("$$$$$$$$ |$$ |  $$ |$$ $$ $$ |$$$$$  \  ")
print("$$ |  $$ |$$ \__$$ |$$ |$$$$ |$$ |$$  \ ")
print("$$ |  $$ |$$    $$/ $$ | $$$ |$$ | $$  |")
print("$$/   $$/  $$$$$$/  $$/   $$/ $$/   $$/ ")
winsound.PlaySound("sound.wav", 0)

print("1. Console Mode")
print("\n2. Graphical Mode")
enter = input("\nEnter the mode of GooseGrapper > ")
if enter == "2":
    def Graphical():
        root = tkinter.Tk()
        root.iconbitmap("goose.ico")
        root.title("GooseGrapper")
        root.minsize(300, 200)
        root.maxsize(300, 200)

        url = tkinter.Entry(root, width=40)
        url.pack()
        url.insert(0, "http://example.com/")

        type = tkinter.Entry(root, width=40)
        type.place(x=28,y=30)
        type.insert(0, "h1")

        class_entry = tkinter.Entry(root, width=40)
        class_entry.place(x=28,y=60)
        class_entry.insert(0, "container")

        def main1():
            tkinter.messagebox.showinfo("Info", "The website was scraped successfully !")
            url_web = url.get()
            web = requests.get(url_web)
            soup = bs4.BeautifulSoup(web.text, "html.parser")
            texte = soup.findAll(type.get(), class_=class_entry.get())
            print(texte)
            for quote in texte:
                print("\n"+quote.text)
        def main2():
            tkinter.messagebox.showinfo("Info", "The website was scraped successfully !")
            url_web = url.get()
            web = requests.get(url_web)
            soup = bs4.BeautifulSoup(web.text, "html.parser")
            texte = soup.findAll(type.get(), class_=class_entry.get())
            os.system("cls")
            for quote in texte:
                os.system("title Vizualiser - "+url_web)
                print("\n"+quote.text)

        name = tkinter.Entry(root, width=40)
        name.place(x=28,y=220)
        name.insert(0, "index.html")
            
        button1 = tkinter.Button(root, text="Generate (html)", command=main1)
        button1.place(x=100, y=90)
        button = tkinter.Button(root, text="Generate (text)", command=main2)
        button.place(x=100, y=140)



        root.mainloop()
    Graphical()
if enter == "1":
    os.system("cls")
    print("1. Html")
    print("\n2. Text")
    type = input("\nEnter the type of the scrapping > ")
    if type == "1":
        url = input("Enter the url > ")
        web = requests.get(url)
        soup = bs4.BeautifulSoup(web.text, "html.parser")
        type_text = input("Enter the type > ")
        class_text = input("Enter the class > ")
        text = soup.findAll(type_text, class_=class_text)
        os.system("title Vizualiser -"+url)
        print(text)
    if type == "2":
        
        url = input("Enter the url > ")
        web = requests.get(url)
        soup = bs4.BeautifulSoup(web.text, "html.parser")
        type_text = input("Enter the type > ")
        class_text = input("Enter the class > ")
        text = soup.findAll(type_text, class_=class_text)
        os.system("title Vizualiser -"+url)
        for quote in text:
            print("\n"+quote.text)