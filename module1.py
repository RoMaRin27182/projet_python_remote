from tkinter import *
import json


root=Tk()
root.title("Algèbre matricielle")
# root.geometry('800x600')
# root.resizable(width=False,height=False)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root_x=int(2*screen_width/3)
root_y=int(2*screen_height/3)

dim=str(root_x)+"x"+str(root_y)
root.geometry(dim)

fontsize=int(root_x/100)

# print(screen_width,screen_height)

lbl=Label(root,text="Notation, relations de base",font=("Arial Bold",30),fg="white",bg="blue")
lbl.grid(column=0,row=0,sticky="W")



with open("questions.json") as fh:
    liste_questions=json.load(fh)

nb_questions=len(liste_questions)

class Carte:
    def __init__(self, recto,verso):
        self.recto = recto
        self.verso = verso
        self.affiche_en_cours=StringVar()


    def affiche_question(self):
        self.affiche_en_cours.set(self.recto)
        question=Label(root,textvariable=self.affiche_en_cours,wraplength=600,font=("Arial Bold",2*fontsize),bg="white",fg="blue",width=40,height=10,relief=RAISED)
        question.grid(column=0,row=1)
        repondre_b.grid(column=0,row=4)
        terminer_b.grid(column=2,row=4)
        autoval.set(-1)

    def affiche_reponse(self):
        self.affiche_en_cours.set(self.verso)



liste_cartes=[]
for question in liste_questions:
    liste_cartes.append(Carte(question["énoncé"],question["réponse"]))

def terminer():
    global score, nb_questions
    final=LabelFrame(root, text="résultat final",font=("Arial Bold",20),bg="white",fg="blue" )
    final.grid(column=0,row=2,columnspan=3)
    scoretxt.set("score:"+str(score.get()*100/(2.0*nb_questions))+"%")
    Label(final,textvariable=scoretxt, font=("Arial Bold",20),bg="white",fg="blue",padx=10,pady=10).grid(column=1,row=1)
    suivante_b["state"]=DISABLED


def repondre():

    carte_en_cours.affiche_reponse()
    autoeval.grid(column=0,row=2,padx=20,pady=20)
    bouton1.grid(column=1,row=3,padx=20,pady=40)
    bouton2.grid(column=2,row=3,padx=20,pady=40)
    bouton3.grid(column=3,row=3,padx=20,pady=40)
    bouton1["state"]=NORMAL
    bouton2["state"]=NORMAL
    bouton3["state"]=NORMAL
    affiche_score.grid(column=0,row=5,columnspan=4)
    repondre_b["state"]=DISABLED
    suivante_b.grid(column=1,row=4)
    terminer_b.grid(column=2,row=4)
    suivante_b["state"]=NORMAL

def auto_evaluation():
    score.set(score.get()+autoval.get())
    scoretxt.set("score:"+str(score.get()))
    repondre_b["state"]=DISABLED
    suivante_b["state"]=NORMAL
    bouton1["state"]=DISABLED
    bouton2["state"]=DISABLED
    bouton3["state"]=DISABLED


def suivante():
    global liste_cartes,carte_en_cours,autoval,nb_questions
    n=liste_cartes.index(carte_en_cours)
    print("n=",n)
    if n==nb_questions-1:
        terminer()
    else:
       carte_en_cours=liste_cartes[n+1]
       print("score=",score.get())
       print("value=",autoval.get())
       repondre_b["state"]=NORMAL
       suivante_b["state"]=DISABLED

       carte_en_cours.affiche_question()



terminer_b=Button(root,text="terminer",command=terminer,font=("Arial Bold",20),bg="white",fg="blue",padx=10,pady=10)
repondre_b=Button(root,text="répondre",command=repondre,font=("Arial Bold",20),bg="white",fg="blue",padx=10,pady=10)
suivante_b=Button(root,text="question suivante",command=suivante, font=("Arial Bold",20),bg="white",fg="blue",padx=10,pady=10)

autoeval=LabelFrame(root,text="auto-évaluation",font=("Arial Bold",20),bg="white",fg="blue")

autoval = IntVar()
bouton1 = Radiobutton(autoeval, text="Bonne réponse",fg="blue", variable=autoval, value=2,command=auto_evaluation)
bouton2 = Radiobutton(autoeval, text="incomplet", fg="blue",variable=autoval, value=1,command=auto_evaluation)
bouton3 = Radiobutton(autoeval, text="Erreur/ne sait pas",fg="blue", variable=autoval, value=0,command=auto_evaluation)

score=IntVar()
score.set(0)
scoretxt=StringVar()
scoretxt.set("score:"+str(score.get()))
affiche_score = Label(root,textvariable=scoretxt, font=("Arial Bold",20),bg="white",fg="blue",padx=10,pady=10)

# Afficher la première QUESTION:
carte_en_cours=liste_cartes[0]
# n=liste_cartes.index(carte_en_cours)
# print("n=",n)
carte_en_cours.affiche_question()

root.mainloop()
