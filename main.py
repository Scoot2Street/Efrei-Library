import os
import random
import time
import tkinter

from Profile import *

from tkinter import *
from tkinter.font import names 


def clear():
    for widgets in fenetre.winfo_children():
      widgets.destroy()


def validatelogin():
    fichier=open("login-password.txt","r")

def fenetremain():    
    fenetre.title("Library Efrei")
    fenetre.geometry("800x500")
    #Boutton Profile 
    Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Frame1.pack(side=LEFT, padx=30, pady=30)
    Label(Frame1).pack(padx=10, pady=10)
    label = Label(fenetre, text="Texte par défaut", bg="yellow")
    label.pack()
    profile=Button(Frame1,text="Acceder aux profiles",highlightbackground='#3E4149',command=lambda: [clear(),sceneprofile()])
    profile.pack(padx=10, pady=10)
    fenetre.mainloop()  

def sceneprofile():
    #Username
    username = StringVar() 
    usernameLabel = Label(fenetre,text="Pseudo").grid(row=0, column=0)
    usernameentry = Entry(fenetre, textvariable=username, width=30).grid(row=0, column=1)
    #Password
    password = StringVar()
    passwordLabel = Label(fenetre,text="Mot de passe").grid(row=1,column=0)
    passwordentry = Entry(fenetre,textvariable=password,show='*',width=30).grid(row=1,column=1)
    #gender
    sexe=StringVar()
    sexeOption = ["Homme", 
                  "Femme",
                  "Non Déterminé"]
    sexe.set(sexeOption[0])
    gender = OptionMenu(fenetre,sexe, *sexeOption)
    gender.grid(row=2,column=1)
    sexeLabel = Label(fenetre,text="Sexe").grid(row=2,column=0)
    
    #Age
    age = IntVar()
    ageLabel = Label(fenetre,text="Age").grid(row=3,column=0)
    ageentry = Entry(fenetre,textvariable=age,width=30).grid(row=3,column=1)
    
    #Style de Lecture
    styleoption= ["sci-fi",
                  "Biography",
                  "Horror",
                  "Romance",
                  "Fable",
                  "History",
                  "Comedy"
                  ]
    style = StringVar()
    style.set(styleoption[0])
    w = OptionMenu(fenetre,style,*styleoption)
    w.grid(row=4,column=1)
    lectureLabel = Label(fenetre,text="style préferé").grid(row=4,column=0)
    #Choisir livre lues 
    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    var10 = IntVar()

    Long_Walk_to_Freedom = Checkbutton(fenetre,text="Long Walk to Freedom",variable=var1, onvalue=1, offvalue=0).grid(row=6,column=0)
    Things_I_Did_and_Things_I_Think_I_Did = Checkbutton(fenetre,text="Things I Did and Things I Think I Did",variable=var2, onvalue=1, offvalue=0).grid(row=6,column=1)
    The_Bloody_Chamber = Checkbutton(fenetre,text="The Bloody Chamber",variable=var3, onvalue=1, offvalue=0).grid(row=6,column=2)
    The_Memoirs_of_an_Amnesiac = Checkbutton(fenetre,text="The Memoirs of an Amnesic",variable=var4, onvalue=1, offvalue=0).grid(row=6,column=3)
    The_Silence_of_the_Lambs = Checkbutton(fenetre,text="The Silence of the Lamb",variable=var5, onvalue=1, offvalue=0).grid(row=7,column=0)
    The_Hunger = Checkbutton(fenetre,text="The Hunger",variable=var6, onvalue=1, offvalue=0).grid(row=7,column=1)
    Wild_Eyes = Checkbutton(fenetre,text="Wild eyes",variable=var7, onvalue=1, offvalue=0).grid(row=7,column=2)
    White_Teeth = Checkbutton(fenetre,text="White Teeth",variable=var8, onvalue=1, offvalue=0).grid(row=7,column=3)
    The_Resisters = Checkbutton(fenetre,text="The Resisters",variable=var9, onvalue=1, offvalue=0).grid(row=8,column=0)
    The_Power = Checkbutton(fenetre,text="The Power",variable=var10, onvalue=1, offvalue=0).grid(row=8,column=1)

    #Bouton retourner au hub
    hub=Button(fenetre,text="Acceder aux hub",highlightbackground='#3E4149',command=lambda: [clear(),fenetremain()])
    hub.grid(row=9,column=2)
    
    
    
    #Ecrire et Lire dans fichier txt
    #fichier= open("login-password.txt","w")
    #fichier.write(username)
    #fichier.write(password)
    #fichier.close()

def ajouter_readers(liste_readers, number, name, age, genre, img_nbr, liste_like, reading_style):
    liste_readers.append({"name":name,"sexe":genre,"age":age,"img_picture":img_nbr,"reading_style":reading_style,"favorite_book":"Narnia"})
    fichier = open("readers.txt", "a")
    fichier.write("\n" + name + "," + str(genre) + "," + str(age) + "," + reading_style)
    fichier2 = open("booksread.txt", "a")
    fichier2.write("\n" + name)
    for a in liste_like:
        fichier2.write("," + str(a))
    print("Ce lecteur a été ajouté")

    return liste_readers


def ajouter_livre(nom_livre):
    fichier = open("books.txt", "r")
    for line in fichier:
        if line == nom_livre:
            print("Ce bouquin existe déja")
            break
    else : 


            fichier = open("books.txt", "a")
            fichier.write("\n" + nom_livre)
            print("Ce bouquin a été ajouté")
    fichier.close

def modifier_livre(nom_livre,nom_modify):
    with open("books.txt","r") as fichier:
        t = fichier.read()
    
    
 
    with open("books.txt", "w") as fichier:
        fichier.write(t.replace(nom_livre,nom_modify))

def delete_book(nom_livre):
    with open("books.txt","r") as fichier:
            t = fichier.read()
        
        
    
    with open("books.txt", "w") as fichier:
        fichier.write(t.replace(nom_livre,str()))

def delete_readers(index_readers,liste_readers):
    with open("readers.txt","r") as fichier:
            t = fichier.read()
        
        
    
    with open("readers.txt", "w") as fichier:
        fichier.write(t.replace(liste_readers[index_readers]["name"] + "," + str(liste_readers[index_readers]["sexe"]) + "," + str(liste_readers[index_readers]["age"]) + "," + str(liste_readers[index_readers]["reading_style"]),str()))


    print(liste_readers[index_readers]["name"] + "," + str(liste_readers[index_readers]["sexe"]) + "," + str(liste_readers[index_readers]["age"]) + "," + str(liste_readers[index_readers]["reading_style"]))

    liste_readers[index_readers] = None
    return liste_readers
    
if __name__ == "__main__":
    liste_readers = [
        {"name":"Gilbert","sexe":1,"age":3,"img_picture":4,"reading_style":6,"favorite_book":"Narnia"},
        {"name":"William","sexe":3,"age":2,"img_picture":4,"reading_style":7,"favorite_book":"Narnia"},
        {"name":"AlienRoXoR17","sexe":2,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
        {"name":"anonyme","sexe":3,"age":3,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
        {"name":"Lecteur_assidu","sexe":1,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
        {"name":"haripoteur","sexe":3,"age":2,"img_picture":4,"reading_style":5,"favorite_book":"Narnia"},
        {"name":"Lili","sexe":2,"age":2,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
        {"name":"ArchiBald_fx","sexe":1,"age":3,"img_picture":4,"reading_style":4,"favorite_book":"Narnia"}
        ]


    # liste_readers = ajouter_readers(liste_readers, 3, "Mathieu", 18, 1, 3, [1,3,4], "Narnia")  
    liste_readers = delete_readers(2,liste_readers)
    fenetre= Tk()
    fenetremain()
    # ajouter_livre("Le Hobbit")
    # modifier_livre("Le Hobbit","Narnia")