
#Program made by Julien Le Ber and Mathieu Roche (Aladdi group)

import os
import random
import time
import tkinter
from math import *
from tkinter import font


from tkinter import *
from tkinter.font import names 
TK_SILENCE_DEPRECATION=1

#Clear the window of all the widget
def clear():
    for widgets in fenetre.winfo_children(): #Take all of the widget in the window 
      widgets.destroy()                      #and destroy them all

#Submit all of the info entered in the inscription form
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
    for i in range(len(var)):           #for all of the books existing, if 
        if var[i].get()==1:             #the box was checked, add the following 
            liste_like.append(i)        #number i in liste_like
            print(liste_like)
    if sexe == "Homme":                 #Checking whether the user is a male,
        sexe=1                          #Female or else
    elif sexe=="Femme":
        sexe=2
    elif sexe=="Non Déterminé":
        sexe=3 
    styleoption= ["sci-fi",
                  "Biography",
                  "Horror",
                  "Romance",
                  "Fable",
                  "History",
                  "Comedy"
                  ]
    for i in range(len(styleoption)):
        if style.get() == styleoption[i]:           #Checking which style the user
            style.set(i)                            #love
 
    top = Toplevel(fenetre)             #Creating a popup to rate all of the books read
    top.geometry("500x500")
    top.title("Rating")    
    for h in range(1,6):
        note.append(Label(top,text=h))  #display all of the number from 1 to 5
        note[h-1].grid(row=0,column=h)  
            
    for i in range(len(liste_like)):
        temp = liste_like[i]
        check = IntVar()
        rating.append(check)
        Label(top,text="Evaluer les livres que vous avez lues : ").grid(row=0,column=0)
        
        for j in range(5):              
            rdiobutton.append(Radiobutton(top,variable=rating[i],value=j+1))            #Putting in a list all of the radio button
            print(j)                                                                    #To generate for a given number of books existing
            rdiobutton[j+(i*5)].grid(row=i+1,column=j+1)
            
        
        labels.append(Label(top,text=liste_livre[temp]))                                #Generating the Label with the tilte of each
        labels[i].grid(row=(i+1),column=0)                                              #book 
        exemple[liste_livre[i]] = rating[i].get()
    
    img_nbr = 1
    Submit=Button(top,text="Confirmer",command=lambda: [clear(),notation(username,age,sexe,img_nbr,liste_like,reading_style,rating),fenetremain()])
    Submit.grid(row=10,column=0)

#Putting in a list all of the note of a user
def notation(username,age,sexe,img_nbr,liste_like,reading_style,rating):
    liste_note = []
    for i in range(len(rating)):
        liste_note.append(rating[i].get())  
    ajouter_readers(username,age,sexe,img_nbr,liste_like,reading_style,liste_note)

#The hub/main window
def fenetremain():    
    fenetre.title("Library Efrei")
    fenetre.geometry("800x500")         #The option of the window
    
    #Title
    
    label = Label(fenetre, text="Bienvenue sur EfreiLibrary")          
    label.config(font=("Arial", 16))
    label.pack(side=TOP)
    
    #Adding an image to the hub
    logo = PhotoImage(file="t.gif")
    can = Canvas(fenetre,width="400",height="400")
    can.create_image(200,200,image=logo)
    can.image = logo
    can.pack()
    
    #inscription button
    
    inscription=Button(fenetre,text="S'inscrire",command=lambda: [clear(),sceneprofile()])
    inscription.pack(side=LEFT,expand=YES)
    #profile button
    profile = Button(fenetre,text="Acceder aux profiles existants",command=lambda: [clear(),scene_readers()])
    profile.pack(side=LEFT,expand=YES)
    #add livre button
    addlivre = Button(fenetre,text="Ajouter un livre",command=lambda: [clear(),scenebook()])
    addlivre.pack(side=LEFT,expand=YES)
    #Recommandation button
    recommandation = Button(fenetre,text="Acceder aux recommandations",command=lambda: [clear(),scenerecommandation()])
    recommandation.pack(side=LEFT,expand=YES)
    fenetre.mainloop()  

#The recommandation window/scene
def scenerecommandation():
    pseudo = StringVar()
    Label(fenetre,text="Entrez votre pseudo").grid(row=0,column=0)                                          #Checking if the pseudo exist
    Entry(fenetre,textvariable=pseudo).grid(row=0,column=1)                                                 #Enter your pseudo
    Button(fenetre,text="Valider",command=lambda:[recom_button(pseudo)]).grid(row=0,column=2)
    Label(fenetre,text="Livre recommandés :").grid(row=1,column=0)
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()]).grid(row=2,column=0)

#Displaying the recommanded book 
def recom_button(pseudo):
    pseudo1=StringVar()
    pseudo1.set(pseudo.get())
    a,b = personne_existe(pseudo1.get()) 
    
    if b == True :
        pseudo1.set(recommandation(a))                          #Checking if the pseudo exist
        clear()                                                 #If it exist, displaying the book 
        scenerecommandation()                                   #recommandation
    if b == False :                                             #If not , displaying "Ce lecteur n'existe pas"
        pseudo1.set("Ce lecteur n'existe pas")
        clear()
        scenerecommandation()
    Label(fenetre,textvariable=pseudo1).grid(row=1,column=1)

#The reader window/scene
def scene_readers():
    global liste_readers
    labels = []
    edit = []
    delete = []
    j=0
    l = []
    
    for i in liste_readers:                                                                                                                                                                 #For each user
        if i != None:
            labels.append(Label(fenetre,text=i["name"]+" "+str(i["sexe"]) + " " + str(i["age"]) + " " + str(i["img_picture"]) + " " + str(i["reading_style"]) + " " + i["favorite_book"]))  #Displaying all of the user's info
            labels[j].grid(row=1*j,column=0)
            
            edit.append(Button(fenetre,text="Edit",command=lambda y=j: [convert(y),clear(),sceneprofile()]))                                                                                #Displaying an edit button to change th user's info
            edit[j].grid(row=1*j,column=1)
            
            
            delete.append(Button(fenetre,text="Delete",command= lambda  x=j :[ clear(),delete_readers(x),scene_readers()]))                                                                         #Displaying a delete button to delete user
            delete[j].grid(row=1*j,column=2)
            
            j+=1
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()])                                                                                                      #Hub button
    hub.grid(row=j+1,column=0)   

#Converting all of the Var into python var and checking the favorite style of the user
def convert(y):
    
    global liste_readers
    global username
    global sexe
    global age
    global style
    
    username.set(liste_readers[y]["name"])          #Converting username,sexe and age into 
    sexe.set(liste_readers[y]["sexe"])              #the old user info
    age.set(liste_readers[y]["age"])
    style.set(liste_readers[y]["reading_style"])
     

#The window/scene of the inscription form
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
    if style.get() == "":                       #Making a default choice "sci-fi"
        style.set(styleoption[0])
    w = OptionMenu(fenetre,style,*styleoption)
    w.grid(row=4,column=1)
    lectureLabel = Label(fenetre,text="style préferé").grid(row=4,column=0)

    #Choisir livre lues 
    var = []
    liste_like=[]
    check = []
    j=0
    k=5
    for i in range(len(liste_livre)):                                                                       #For all of the existing books
        if liste_livre[i]!="":                                                                              #Making sure there is acutally a name 
            var.append(IntVar())                                                                            #Creating a list of IntVar()
            check.append(Checkbutton(fenetre,text=liste_livre[i],variable=var[i],offvalue=0,onvalue=1))     #Generating checkbutton with intvar in a list
            check[i].grid(row=(k),column=j)                                                                 #Placing all of the check button
            j+=1
            if j > 2 :                                                                                      #Making sure that if there is too much books
                j=0                                                                                         #the programm change row
                k +=1
                   
    
    #Bouton retourner au hub
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()])
    hub.grid(row=200,column=0)
    #Convertir en str
    #Sumbit button
    number= 1
    img_nbr = 3
    #
    Submit=Button(fenetre,text="S'inscrire",command=lambda: [clear(),submit(var,style,username.get(),password.get(),sexe.get(),age.get())])

    Submit.grid(row=100,column=1)

#The popup to modify a book's name
def popup(y):
    global liste_livre
    top = Toplevel(fenetre)
    nouveau_nom=StringVar()
    top.geometry("250x250")
    top.title("Modification")
    Label(top,text="Entrez le nouveau nom").pack(side=TOP)
    Entry(top,textvariable=nouveau_nom).pack(side=LEFT)
    Button(top,text="Confirmer",command=lambda:[modifier_livre(liste_livre[y],nouveau_nom.get()),top.destroy(),scenebook()]).pack(side=LEFT)
      
#The window/scene where all of the books are displayed
def scenebook():
    global liste_livre
    liste_livre = initialized_liste_livre() #Refreshing books database
    livre = StringVar()
    add_livre = Label(fenetre,text="Entrez le nom du livre que vous souhaitez ajouter")
    livreentry = Entry(fenetre,textvariable=livre)
    entrer = Button(fenetre,text="Entrer",command=lambda:[ajouter_livre(livre.get()),livre.set(""),scenebook()])
    add_livre.grid(row=0,column=0)
    livreentry.grid(row=1,column=0)
    entrer.grid(row=1,column=1)
    labels,edit,delete = [],[],[]
    j=0
    c=0
    k=0
    hub=Button(fenetre,text="Acceder aux hub",command=lambda: [clear(),fenetremain()]).grid(row=1,column=3)
    for i in range(len(liste_livre)):                   #For all of the books in liste_livre
        if j ==16 or j ==32:                            #Making sure after 16 or 32 books, the programm goes to the next column
            c +=3
            j=0
        if liste_livre[i]!="":                          #Making sure there is an actual book name and not just an empty line
            
            labels.append(Label(fenetre,text=liste_livre[i]))       #Generating all of the books name into a list of label
            labels[k].grid(row=1*(j+2),column=c)                    #Displaying all of the books
                
            edit.append(Button(fenetre,text="Edit",command=lambda y=i: [popup(y)]))     #Generating all of the edit button next to the book's name
            edit[k].grid(row=1*(j+2),column=c+1)                                        #Displaying all of the edit button

                
            delete.append(Button(fenetre,text="Delete",command= lambda  x=i , z=k:[ delete_book(liste_livre[x]),suppr(z,delete,edit)]))     #generating all of the delete button next to the edit button
            delete[k].grid(row=1*(j+2),column=c+2)                                                                                          #Displaying all of the delete button
            j+=1
            k+=1
        else:
            i+=1

#Deleting the widget of a deleted book
def suppr(x,delete,edit):
    delete[x].grid_forget()     #Deleting the delete button of a deleted book
    edit[x].grid_forget()       #Deleting the edit button of a deleted book
    clear()                     #Refreshing the window/scene
    scenebook()
    

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

def recommandation(index_lecteur):
    
    global liste_readers
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
    return (liste_livre[int(livre_recommandation)])

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
    
def personne_existe(nom):
    global liste_readers
    for a in range (0,len(liste_readers)):
        if liste_readers[a] != None:
            if liste_readers[a]["name"] == nom:
                return a,True
    return a,False



if __name__ == "__main__":
    global liste_readers
    global liste_livre

    liste_readers = initialized_liste_readers()
    liste_livre = initialized_liste_livre()
    
    fenetre= Tk()
    username = StringVar()
    sexe = StringVar()
    age = IntVar()
    style = StringVar()
    
    
    fenetremain()
