

from io import UnsupportedOperation
import os
import random
import time
import tkinter
from math import *
from tkinter import font


from tkinter import *
from tkinter.font import names 
TK_SILENCE_DEPRECATION=1

def clear():
    for widgets in fenetre.winfo_children():
      widgets.destroy()

def submit(var,reading_style,username,password,sexe,age):
    global liste_readers
    global liste_livre
    global liste_like
    rating=[]
    labels=[]
    note = []
    rdiobutton = []
    liste_like=[]
    exemple = {}
    print(var)
    for i in range(len(var)):
        if var[i].get()==1:
            liste_like.append(i)
            print(liste_like)
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
    
    img_nbr = 1
    Submit=Button(top,text="Confirmer",highlightbackground='#3E4149',command=lambda: [clear(),notation(username,age,sexe,img_nbr,liste_like,reading_style,rating),fenetremain()])
    Submit.grid(row=10,column=0)

def notation(username,age,sexe,img_nbr,liste_like,reading_style,rating):
    liste_note = []
    for i in range(len(rating)):
        liste_note.append(rating[i].get())  
    ajouter_readers(username,age,sexe,img_nbr,liste_like,reading_style,liste_note)

def fenetremain():    
    fenetre.title("Library Efrei")
    fenetre.geometry("800x500")
    
    
    
    
    #Label
    
    label = Label(fenetre, text="Bienvenue sur EfreiLibrary")
    label.config(font=("Arial", 16))
    label.pack(side=TOP)
    
    #gestion de l'image
    logo = PhotoImage(file="t.gif")
    can = Canvas(fenetre,width="400",height="400")
    can.create_image(200,200,image=logo)
    can.image = logo
    can.pack()
    #inscription boutton
    
    inscription=Button(fenetre,text="S'inscrire",command=lambda: [clear(),sceneprofile()])
    inscription.pack(side=LEFT,expand=YES)
    #profile boutton
    profile = Button(fenetre,text="Acceder aux profiles existants",command=lambda: [clear(),scene_readers()])
    profile.pack(side=LEFT,expand=YES)
    #add livre boutton
    addlivre = Button(fenetre,text="Ajouter un livre",command=lambda: [clear(),scenelivre()])
    addlivre.pack(side=LEFT,expand=YES)
    #Recommandation boutton
    recommandation = Button(fenetre,text="Acceder aux recommandations",command=lambda: [clear(),scenerecommandation()])
    recommandation.pack(side=LEFT,expand=YES)
    fenetre.mainloop()  

def scenerecommandation():
    pseudo = StringVar()
    Label(fenetre,text="Entrez votre pseudo").grid(row=0,column=0)
    Entry(fenetre,textvariable=pseudo).grid(row=0,column=1)
    Button(fenetre,text="Valider",command=lambda:[]).grid(row=0,column=2)
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()]).grid(row=1,column=0)

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
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()])
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
    global liste_livre
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
    var = []
    liste_like=[]
    check = []
    j=0
    k=4
    for i in range(len(liste_livre)):
        
        var.append(IntVar())
        check.append(Checkbutton(fenetre,text=liste_livre[i],variable=var[i],offvalue=0,onvalue=1))
        check[i].grid(row=(k),column=j)
        j+=1
        if j > 2 :
            j=0
            k +=1
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
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()])
    hub.grid(row=20,column=0)
    #Convertir en str
    #Sumbit button
    number= 1
    img_nbr = 3
    #
    Submit=Button(fenetre,text="S'inscrire",command=lambda: [clear(),submit(var,reading_style,username.get(),password.get(),sexe.get(),age.get())])
    Submit.grid(row=10,column=1)

def popup(y):
    global liste_livre
    top = Toplevel(fenetre)
    nouveau_nom=StringVar()
    top.geometry("250x250")
    top.title("Modification")
    Label(top,text="Entrez le nouveau nom").pack(side=TOP)
    Entry(top,textvariable=nouveau_nom).pack(side=LEFT)
    Button(top,text="Confirmer",command=lambda:[modifier_livre(liste_livre[y],nouveau_nom.get()),top.destroy(),scenelivre()]).pack(side=LEFT)
      
def scenelivre():
    global liste_livre
    liste_livre = initialized_liste_livre()
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
    k=0
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()]).grid(row=1,column=3)
    for i in range(len(liste_livre)):
        if j ==16 or j ==32:
            c +=3
            j=0
        if liste_livre[i]!="":
            
            labels.append(Label(fenetre,text=liste_livre[i]))
            labels[k].grid(row=1*(j+2),column=c)
                
            edit.append(Button(fenetre,text="Edit",command=lambda y=i: [popup(y)]))
            edit[k].grid(row=1*(j+2),column=c+1)
                
                
            delete.append(Button(fenetre,text="Delete",command= lambda  x=i , z=k:[ delete_book(liste_livre[x]),suppr(z,delete,edit)]))
            delete[k].grid(row=1*(j+2),column=c+2)
            j+=1
            k+=1
        else:
            i+=1
def suppr(x,delete,edit):
    delete[x].grid_forget()
    edit[x].grid_forget()
    clear()
    scenelivre()
    
def ajouter_readers(name, age, genre, img_nbr, liste_like, reading_style,liste_note):
    global liste_readers
    liste_readers.append({"name":name,"sexe":genre,"age":age,"img_picture":img_nbr,"reading_style":reading_style,"favorite_book":"Narnia"})
    fichier = open("readers.txt", "a")
    fichier.write("\n" + name + "," + str(genre) + "," + str(age) + "," + str(reading_style))
    fichier2 = open("booksread.txt", "a")
    fichier2.write("\n" + name)
    for a in liste_like:
        fichier2.write("," + str(a))
    fichier2.write("%")
    for a in range (0,len(liste_note)):
        fichier2.write(str(a))
        if liste_note.index(liste_note[a]) != liste_note.index(liste_note[-1]):
            fichier2.write(",")

    print("Ce lecteur a été ajouté")

    return liste_readers

def ajouter_livre(nom_livre):
    global liste_livre
    str(nom_livre)
   
    fichier = open("books.txt", "r")
    for line in fichier:
        if line == nom_livre:
            print("Ce bouquin existe déja")
            break
    else : 


            fichier = open("books.txt", "a")
            fichier.write("\n" + nom_livre +"\n" )
            liste_livre.append(nom_livre)

            print("Ce bouquin a été ajouté")
    
    fichier.close

    return liste_livre

def modifier_livre(nom_livre,nom_modify):
    nom_modify=  str(nom_modify)
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

    with open("booksread.txt") as fichier2:
        cpt = 0
        for line in fichier2:
            if cpt == index_readers:
                a = line
                break
            else :
                cpt += 1
        print(a)

    with open("booksread.txt","r") as fichier2:
            t2 = fichier2.read()
        
    with open("booksread.txt", "w") as fichier2:
        fichier2.write(t2.replace(a,str("\n")))

    liste_readers[index_readers] = None
    return liste_readers

def matrice_generator(liste_readers):
    matrice = []
    with open('books.txt') as f:
        b = sum(1 for _ in f)
    
    for a in range (0,b):
        matrice.append([])
        for c in range (0,len(liste_readers)):
            matrice[a].append(0)

    for lecteur in range  (0,len(liste_readers)):
        cpt = 0
        for livre_lu in liste_readers[lecteur]["booksread"]:
            # print("lecteur",lecteur,"livre_lu",livre_lu,"coordonnées",int(livre_lu)-1," + ",lecteur,"note ajoutée",liste_readers[lecteur]["note"][cpt],"cpt",cpt)

            matrice[int(livre_lu)-1][lecteur] = int(liste_readers[lecteur]["note"][cpt])

            cpt += 1
 
    # #0 = pas lu 5 = excellent
    # print (matrice)


    return matrice

def note(liste_readers):
    with open('booksread.txt') as fichier:
        a = sum(1 for _ in fichier)
    with open('booksread.txt') as fichier:
        cpt = 0
        cpt2 = 0
        for line in fichier:
            c = line.split("%")
            if cpt2 < a-1:
                c[-1] = c[-1][0:-1]
 
            liste_readers[cpt]["note"] = c[1].split(",")
            
            b = c[0].split()
            b = b[0]
            b = b.split(",")
            liste_readers[cpt]["booksread"] = b[1:]
    
            cpt += 1
            cpt2 += 1
            if cpt == len(liste_readers):
                break
            
    return liste_readers
    
def similarity_matrice(liste_readers,matrice):
    matrice_sim=[]
    for a in range (0,len(liste_readers)):
        matrice_sim.append([])
        for b in range (0,len(liste_readers)):
            matrice_sim[a].append(0)

        
    # a1xb1 +a2 * b2 + a3*b3 jusqu à  n (nombre de livres)
    # divisé par racine de (a1²) + racine de (b1²) +....jusqu à n nombre de livres
    return matrice_sim

def similarity_btw_readers(liste_readers,matrice,matrice_sim):

    # for b in range (0,len(matrice)):
    #     print ("=",matrice[b])
    
    for b in range (0,len(matrice_sim)):
        for c in range (0,len(matrice_sim[b])):
            # #lecteur 1 et 3
            val1,val2,val3 = 0,0,0
            for a in range (0,len(matrice)):
                val1 += matrice[a][b]*matrice[a][c]
                val2 += matrice[a][b]**2
                val3 += matrice[a][c]**2
            val4 = val1/(sqrt(val2)*sqrt(val3))
            val4 = round(val4,2)
            matrice_sim[b][c] = val4

    # for b in range (0,len(matrice_sim)):
    #     print (":",matrice_sim[b])
    return matrice_sim

def modifier_reader(liste_readers,index,name,age,genre,img_nbr,liste_like,reading_style):
    with open("readers.txt","r") as fichier:
        t = fichier.read()

    with open("readers.txt", "w") as fichier:
        fichier.write(t.replace(liste_readers[index]["name"] + "," + str(liste_readers[index]["sexe"]) + "," + str(liste_readers[index]["age"]) + "," + str(liste_readers[index]["reading_style"]),name + "," + str(genre) + "," + str(age) + "," + str(reading_style)))
        print(liste_readers[index]["name"] + "," + str(liste_readers[index]["sexe"]) + "," + str(liste_readers[index]["age"]) + "," + str(liste_readers[index]["reading_style"]))
        print(name + "," + str(genre) + "," + str(age) + "," + str(reading_style))
    liste_readers[index] = {"name":name,"sexe":genre,"age":age,"img_picture":img_nbr,"reading_style":reading_style,"favorite_book":"Narnia"} 

    return liste_readers

def recommandation(liste_readers,index_lecteur):
    liste_readers = note(liste_readers)
    matrice = matrice_generator(liste_readers)
    matrice_sim = similarity_matrice(liste_readers,matrice)
    matrice_sim  = similarity_btw_readers(liste_readers,matrice,matrice_sim)
    copie = matrice_sim[index_lecteur]
    copie[index_lecteur] = 0
    maxi = max(copie)
    index_maxi = copie.index(maxi)
    a = max([len(liste_readers[index_lecteur]["booksread"]),len(liste_readers[index_maxi]["booksread"])])
    liste_reco = []
    key_list = []
    note_list = []
    for b in range(0,len(liste_readers[index_maxi]["booksread"])):
        if liste_readers[index_maxi]["booksread"][b] not in liste_readers[index_lecteur]["booksread"]:
            liste_reco.append(liste_readers[index_maxi]["booksread"][b])
            key_list.append(liste_readers[index_maxi]["booksread"].index(liste_readers[index_maxi]["booksread"][b]))
    
    for c in key_list:
        note_list.append(liste_readers[index_maxi]["note"][c])
        note_max = note_list.index(max(note_list))

    livre_recommandation = liste_reco[note_max]

    return liste_readers,matrice,matrice_sim,livre_recommandation

def initialized_liste_livre():
    global liste_livre
    liste_livre = []
    fichier = open("books.txt", "r")
    for line in fichier:
        liste_livre.append(line[0:-1])
    return liste_livre

def initialized_liste_readers():
    fichier = open("readers.txt", "r")
    liste_readers = []
    for line in fichier:
        c = line.split(",")
        if '\n' in c[-1][-2:]:
            c[-1] = c[-1][0:-1]
        liste_readers.append({"name":c[0],"sexe":int(c[1]),"age":int(c[2]),"img_picture":4,"reading_style":int(c[3]),"favorite_book":"Narnia"})

        
    return liste_readers
    

    
if __name__ == "__main__":
    global liste_readers
    global liste_livre

    # liste_readers = [
    #     {"name":"Gilbert","sexe":1,"age":3,"img_picture":4,"reading_style":6,"favorite_book":"Narnia"},
    #     {"name":"William","sexe":3,"age":3,"img_picture":4,"reading_style":7,"favorite_book":"Narnia"},
    #     {"name":"AlienRoXoR17","sexe":2,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
    #     {"name":"anonyme","sexe":3,"age":3,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
    #     {"name":"Lecteur_assidu","sexe":1,"age":1,"img_picture":4,"reading_style":3,"favorite_book":"Narnia"},
    #     {"name":"haripoteur","sexe":3,"age":2,"img_picture":4,"reading_style":5,"favorite_book":"Narnia"},
    #     {"name":"Lili","sexe":2,"age":2,"img_picture":4,"reading_style":2,"favorite_book":"Narnia"},
    #     {"name":"ArchiBald_fx","sexe":1,"age":3,"img_picture":4,"reading_style":4,"favorite_book":"Narnia"}
    #     ]

    liste_readers = initialized_liste_readers()
    liste_livre = initialized_liste_livre()




    
    liste_readers,matrice,matrice_sim,livre_recommandation = recommandation(liste_readers,8) #livre à recommandé pour lecteur 9 d'index 8 dans liste_readers
    print("le livre à lire est le livre",livre_recommandation)

    # for a in range(0,len(liste_readers)):
    #     print(liste_readers[a])
    # liste_readers = ajouter_readers( 3, "Mathieu", 18, 1, 3, [1,3,4],1 ,[5,4,2])
    fenetre= Tk()
    username = StringVar()
    sexe = StringVar()
    age = IntVar()
    style = StringVar()
    
    
    fenetremain()





    # ajouter_livre("Le Hobbit")
    # modifier_livre("Le Hobbit","Narnia")
