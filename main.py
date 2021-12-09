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
    sexe=tkinter.StringVar()
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
    
    
    
    #Ecrire et Lire dans fichier txt
    #fichier= open("login-password.txt","w")
    #fichier.write(username)
    #fichier.write(password)
    #fichier.close()

def ajouter_readers(liste_readers, number, name, age, genre, img_nbr, liste_like, reading_style):
    liste_readers.append({"name":name,"sexe":genre,"age":age,"img_picture":img_nbr,"reading_style":reading_style,"favorite_book":"Narnia"})
    fichier = open("readers.txt", "a")
    fichier.write("\n" + name + "," + str(genre) + "," + str(age) + "," + str(reading_style))
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

def modifier_reader(liste_readers,index,number,name,age,genre,img_nbr,liste_like,reading_style):
    with open("readers.txt","r") as fichier:
        t = fichier.read()

    with open("readers.txt", "w") as fichier:
        fichier.write(t.replace(liste_readers[index]["name"] + "," + str(liste_readers[index]["sexe"]) + "," + str(liste_readers[index]["age"]) + "," + str(liste_readers[index]["reading_style"]),name + "," + str(genre) + "," + str(age) + "," + str(reading_style)))
        print(liste_readers[index]["name"] + "," + str(liste_readers[index]["sexe"]) + "," + str(liste_readers[index]["age"]) + "," + str(liste_readers[index]["reading_style"]))
        print(name + "," + str(genre) + "," + str(age) + "," + str(reading_style))
    liste_readers[index] = {"name":name,"sexe":genre,"age":age,"img_picture":img_nbr,"reading_style":reading_style,"favorite_book":"Narnia"} 

    return liste_readers

if __name__ == "__main__":
    liste_readers = [
        {"name":"Gilbert","sexe":1,"age":3,"img_picture":4,"reading_style":6,"favorite_book":"Narnia"},
        {"name":"William","sexe":3,"age":3,"img_picture":4,"reading_style":7,"favorite_book":"Narnia"},
        {"name":"AlienRoXoR17","sexe":2,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
        {"name":"anonyme","sexe":3,"age":3,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
        {"name":"Lecteur_assidu","sexe":1,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
        {"name":"haripoteur","sexe":3,"age":2,"img_picture":4,"reading_style":5,"favorite_book":"Narnia"},
        {"name":"Lili","sexe":2,"age":2,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
        {"name":"ArchiBald_fx","sexe":1,"age":3,"img_picture":4,"reading_style":4,"favorite_book":"Narnia"}
        ]
        
    fenetre= Tk()
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


    # liste_readers = ajouter_readers(liste_readers, 3, "Mathieu", 18, 1, 3, [1,3,4], "Narnia")  
    # liste_readers = modifier_reader(liste_readers,1,2,"MathieuRAZR",2,2,4,[1,2,3],2)



    fenetre.mainloop()

    # ajouter_livre("Le Hobbit")
    # modifier_livre("Le Hobbit","Narnia")