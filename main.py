

from io import UnsupportedOperation
import os
import random
import time
import tkinter

from Profile import *

from tkinter import *
from tkinter.font import names 
TK_SILENCE_DEPRECATION=1

def clear():
    for widgets in fenetre.winfo_children():
      widgets.destroy()

def submit(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,reading_style,username,password,sexe,age):
    global liste_readers
    global liste_livre
    global liste_like
    rating=[]
    labels=[]
    note = []
    rdiobutton = []
    liste_like=[]
    exemple = {}
    if var1.get() == 1:
        liste_like.append(0)
    if var2.get() == 1:
        liste_like.append(1)
    if var3.get() == 1:
        liste_like.append(2)
    if var4.get() == 1:
        liste_like.append(3)
    if var5.get() == 1:
        liste_like.append(4)
    if var6.get() == 1:
        liste_like.append(5)
    if var7.get() == 1:
        liste_like.append(6)
    if var8.get() == 1:
        liste_like.append(7)
    if var9.get() == 1:
        liste_like.append(8)
    if var10.get() == 1:
        liste_like.append(9)
    if sexe == "Homme":
        sexe=1
    elif sexe=="Femme":
        sexe=2
    elif sexe=="Non Déterminé":
        sexe=3 
    top = Toplevel(fenetre)
    top.geometry("500x500")
    top.title("Rating")    
    for h in range(1,6):
        note.append(Label(top,text=h))
        note[h-1].grid(row=0,column=h)
            
    for i in range(len(liste_like)):
        temp = liste_like[i]
        check = IntVar()
        rating.append(check)
        Label(top,text="Evaluer les livres que vous avez lues : ").grid(row=0,column=0)
        
        for j in range(5):
            rdiobutton.append(Radiobutton(top,variable=rating[i],value=j+1))
            print(j)
            rdiobutton[j+(i*5)].grid(row=i+1,column=j+1)
            
        
        labels.append(Label(top,text=liste_livre[temp]))
        labels[i].grid(row=(i+1),column=0)
        exemple[liste_livre[i]] = rating[i].get()
    
    
    Submit=Button(top,text="Confirmer",highlightbackground='#3E4149',command=lambda: [clear(),notation(rating),fenetremain()])
    Submit.grid(row=10,column=0)
        
    print(liste_like)
    number=1
    img_nbr = 1
    ajouter_readers(number,username,age,sexe,img_nbr,liste_like,reading_style)

def notation(rating):
    global liste_like
    dict_note = {}
    for i in range(len(liste_like)):
        dict_note[liste_like[i]] = rating[i].get()
        print(dict_note)


def fenetremain():    
    fenetre.title("Library Efrei")
    fenetre.geometry("800x500")
   #Label
    
    label = Label(fenetre, text="Texte par défaut", bg="yellow")
    label.pack(side=TOP)
    #inscription boutton
    inscription=Button(fenetre,text="S'inscrire",highlightbackground='#3E4149',command=lambda: [clear(),sceneprofile()])
    inscription.pack(side=LEFT)
    #profile boutton
    profile = Button(fenetre,text="Acceder aux profiles existants",command=lambda: [clear(),scene_readers()])
    profile.pack(side=LEFT)
    #add livre boutton
    addlivre = Button(fenetre,text="Aouter un livre",command=lambda: [clear(),scenelivre()])
    addlivre.pack(side=LEFT)
    fenetre.mainloop()  

def scene_readers():
    global liste_readers
    labels = []
    edit = []
    delete = []
    
    myFrame = Frame(fenetre).place(x=50, y=100)
    
    j=0
    l = []
    
    for i in liste_readers: 
        if i != None:
            labels.append(Label(fenetre,text=i["name"]+" "+str(i["sexe"]) + " " + str(i["age"]) + " " + str(i["img_picture"]) + " " + str(i["reading_style"]) + " " + i["favorite_book"]))
            labels[j].grid(row=1*j,column=0)
            
            edit.append(Button(fenetre,text="Edit",command=lambda y=j: [a(y),clear(),sceneprofile()]))
            edit[j].grid(row=1*j,column=1)
            
            
            delete.append(Button(fenetre,text="Delete",command= lambda  x=j :[ delete_readers(x),scene_readers()]))
            delete[j].grid(row=1*j,column=2)
            
            j+=1
    hub=Button(fenetre,text="Acceder aux hub",highlightbackground='#3E4149',command=lambda: [clear(),fenetremain()])
    hub.grid(row=j+1,column=0)       
def a(y):
    global liste_readers
    global username
    global sexe
    global age
    global style
    
    username.set(liste_readers[y]["name"])
    sexe.set(liste_readers[y]["sexe"])
    age.set(liste_readers[y]["age"])
    style.set(liste_readers[y]["reading_style"])
    if style.get() == "sci-fi":
        reading_style=1
    elif style.get() == "Biography":
        reading_style=2
    elif style.get() == "Horror":
        reading_style=3
    elif style.get()== "Romance":
        reading_style=4       
    elif style.get() == "Fable":
        reading_style=5
    elif style.get()=="History":
        reading_style=6
    elif style.get() == "Comedy":
        reading_style=7   
    
    
    
def sceneprofile():
    global liste_readers
    global username
    global sexe
    global age
    global style
    
    #Username
    
   
    usernameLabel = Label(fenetre,text="Pseudo").grid(row=0, column=0)
    usernameentry = Entry(fenetre, textvariable=username, width=30).grid(row=0, column=1)
    #Password
    password = StringVar()
    passwordLabel = Label(fenetre,text="Mot de passe").grid(row=1,column=0)
    passwordentry = Entry(fenetre,textvariable=password,show='*',width=30).grid(row=1,column=1)
    #gender
    
    sexeOption = ["Homme", 
                  "Femme",
                  "Non Déterminé"]
    sexe.set(sexeOption[0])
    gender = OptionMenu(fenetre,sexe, *sexeOption)
    gender.grid(row=2,column=1)
    sexeLabel = Label(fenetre,text="Sexe").grid(row=2,column=0)
    
    #Age
    
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
    if style.get() == "":
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
    liste_like=[]
    Long_Walk_to_Freedom = Checkbutton(fenetre,text="Long Walk to Freedom",variable=var1, onvalue=1, offvalue=0,).grid(row=6,column=1)
    Things_I_Did_and_Things_I_Think_I_Did = Checkbutton(fenetre,text="Things I Did and Things I Think I Did",variable=var2, onvalue=1, offvalue=0).grid(row=6,column=2)
    The_Bloody_Chamber = Checkbutton(fenetre,text="The Bloody Chamber",variable=var3, onvalue=1, offvalue=0).grid(row=6,column=3)
    The_Memoirs_of_an_Amnesiac = Checkbutton(fenetre,text="The Memoirs of an Amnesic",variable=var4, onvalue=1, offvalue=0).grid(row=7,column=0)
    The_Silence_of_the_Lambs = Checkbutton(fenetre,text="The Silence of the Lamb",variable=var5, onvalue=1, offvalue=0).grid(row=7,column=1)
    The_Hunger = Checkbutton(fenetre,text="The Hunger",variable=var6, onvalue=1, offvalue=0).grid(row=7,column=2)
    Wild_Eyes = Checkbutton(fenetre,text="Wild eyes",variable=var7, onvalue=1, offvalue=0).grid(row=7,column=3)
    White_Teeth = Checkbutton(fenetre,text="White Teeth",variable=var8, onvalue=1, offvalue=0).grid(row=8,column=0)
    The_Resisters = Checkbutton(fenetre,text="The Resisters",variable=var9, onvalue=1, offvalue=0).grid(row=8,column=1)
    The_Power = Checkbutton(fenetre,text="The Power",variable=var10, onvalue=1, offvalue=0).grid(row=8,column=2)
    livre = Label(fenetre,text="Livre lus").grid(row=6,column=0)
    #Ajout des livres lues a liste_like


    #Convertir reading style en int
    reading_style=1
    if style.get() == "sci-fi":
        reading_style=1
    elif style.get() == "Biography":
        reading_style=2
    elif style.get() == "Horror":
        reading_style=3
    elif style.get()== "Romance":
        reading_style=4       
    elif style.get() == "Fable":
        reading_style=5
    elif style.get()=="History":
        reading_style=6
    elif style.get() == "Comedy":
        reading_style=7           
        
    
    #Bouton retourner au hub
    hub=Button(fenetre,text="Acceder aux hub",highlightbackground='#3E4149',command=lambda: [clear(),fenetremain()])
    hub.grid(row=20,column=0)
    #Convertir en str
    #Sumbit button
    number= 1
    img_nbr = 3
    #
    Submit=Button(fenetre,text="S'inscire",highlightbackground='#3E4149',command=lambda: [clear(),submit(var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,reading_style,username.get(),password.get(),sexe.get(),age.get())])
    Submit.grid(row=10,column=1)
    
    #Ecrire et Lire dans fichier txt
    #fichier= open("login-password.txt","w")
    #fichier.write(username)
    #fichier.write(password)
    #fichier.close()
def popup(y):
    global liste_livre
    top = Toplevel(fenetre)
    nouveau_nom=StringVar()
    top.geometry("250x250")
    top.title("Modification")
    Label(top,text="Entrez le nouveau nom").pack(side=TOP)
    Entry(top,textvariable=nouveau_nom).pack(side=LEFT)
    Button(top,text="Confirmer",command=lambda:[modifier_livre(liste_livre[y],nouveau_nom.get(),top.destroy())]).pack(side=LEFT)
    
    
def scenelivre():
    print("test")
    livre = StringVar()
    add_livre = Label(fenetre,text="Entrez le nom du livre que vous souhaitez ajouter")
    livreentry = Entry(fenetre,textvariable=livre)
    entrer = Button(fenetre,text="Entrer",command=lambda:[ajouter_livre(livre.get()),livre.set(""),scenelivre()])
    add_livre.grid(row=0,column=0)
    livreentry.grid(row=1,column=0)
    entrer.grid(row=1,column=1)
    labels,edit,delete = [],[],[]
    j=0
    c=0
    for i in range(len(liste_livre)):
        if j ==16 or j ==32:
            c +=3
            j=0
        labels.append(Label(fenetre,text=liste_livre[i]))
        labels[i].grid(row=1*(j+2),column=c)
            
        edit.append(Button(fenetre,text="Edit",command=lambda y=i: [popup(y)]))
        edit[i].grid(row=1*(j+2),column=c+1)
            
            
        delete.append(Button(fenetre,text="Delete",command= lambda  x=i :[ delete_book(liste_livre[x]),scenelivre()]))
        delete[i].grid(row=1*(j+2),column=c+2)
        j+=1
    
    
    
def ajouter_readers( number, name, age, genre, img_nbr, liste_like, reading_style):
    global liste_readers
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
    str(nom_livre)
   
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
    nom_modify=  str(nom_modify)
    print(nom_modify,nom_livre)
    with open("books.txt","r") as fichier:
        t = fichier.read()
    
    
 
    with open("books.txt", "w") as fichier:
        fichier.write(t.replace(nom_livre,nom_modify))

def delete_book(nom_livre):
    with open("books.txt","r") as fichier:
            t = fichier.read()
        
        
    
    with open("books.txt", "w") as fichier:
        fichier.write(t.replace(nom_livre,str()))
def delete_readers(index_readers):
    global liste_readers
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
    global liste_readers
    global liste_livre
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
    liste_livre=["Débuter la programmation Java",
    "Apprendre Python",
    "Les Citations du Président Mao Tse-Toung",
    "Don Quichotte de la Manche",
    "Un conte de deux villes",
    "Le Seigneur des Anneaux",
    "Le Petit Prince",
    "Harry Potter à l’école des sorciers",
    "Dix Petits Nègres",
    "Le rêve dans le Pavillon rouge",
    "Le Lion, la Sorcière blanche et l’Armoire magique",
    "Elle – She : a history of Adventure",
    "The Da Vinci Code",
    "Réfléchissez et devenez riche",
    "Harry Potter et le Prince de Sang mêlé",
    "L’Alchimiste",
    "Harry Potter et la Chambre des Secrets",
    "L’attrape-cœurs, The Catcher in the Rye",
    "Narnia"]

    # liste_readers = ajouter_readers(liste_readers, 3, "Mathieu", 18, 1, 3, [1,3,4], "Narnia")  

    fenetre= Tk()
    username = StringVar()
    sexe = StringVar()
    age = IntVar()
    style = StringVar()
    
    
    fenetremain()





    # ajouter_livre("Le Hobbit")
    # modifier_livre("Le Hobbit","Narnia")