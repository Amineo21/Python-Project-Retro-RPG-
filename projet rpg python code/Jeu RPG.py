import pickle


inventaire = {
    "épée": 1,
    "potion de guérison": 3,
    "clé magique (-5 pv/utilisation)": 2
}
monstre_pv = 100  
pv_perso= 200
Behemoth_pv=125
Boss_pv=200

def utiliser_item(item):
    global pv_perso, monstre_pv
    if item == "potion de guérison":
        pv_perso += 20  
        print("Vous avez utilisé une potion et récupéré 20 points de vie. Vous avez maintenant", pv_perso, "points de vie.")
        utiliser_objet(inventaire,"potion de guérison", 1)
        Combats()       
    elif item == "épée":
        monstre_pv -=20
        print("vous avez pris l'épée, votre puissance augmente de 20")
        utiliser_objet(inventaire,"épée", 1)
        Combats()        
    elif item == "clé magique":
        monstre_pv -=30
        pv_perso-=5
        print("Drôle d'objet mystérieux, mais pourquoi pas. 30 points de puissance en plus")
        utiliser_objet(inventaire,"clé magique", 1) 
        Combats() 
     
   
        
    else:
        print("Cet item n'est pas utilisable.")
        Combats()        

def utiliser_item_2(item):
    global pv_perso, Behemoth_pv
    if item == "potion de guérison":
        pv_perso += 20  
        print("Vous avez utilisé une potion et récupéré 20 points de vie. Vous avez maintenant", pv_perso, "points de vie.")
        utiliser_objet(inventaire,"potion de guérison", 1)
        Combats_2()
    elif item == "épée":
        Behemoth_pv -=20
        print("vous avez pris l'épée, votre puissance augmente de 20")
        utiliser_objet(inventaire,"épée", 1)
        Combats_2()
    elif item == "clé magique":
        Behemoth_pv-=30
        pv_perso-=5
        print("Drôle d'objet mystérieux, mais pourquoi pas. 30 points de puissance en plus")
        utiliser_objet(inventaire,"clé magique", 1)
        Combats_2()
    else:
        print("Cet item n'est pas utilisable.")
        Combats_2()

def utiliser_item_Boss(item):
    global pv_perso,  Boss_pv
    if item == "potion de guérison":
        pv_perso += 20  
        print("Vous avez utilisé une potion et récupéré 20 points de vie. Vous avez maintenant", pv_perso, "points de vie.")
        utiliser_objet(inventaire,"potion de guérison", 1)
        Boss_Final()
    elif item == "épée":
        Boss_pv -=10
        print("vous avez pris l'épée, votre puissance augmente de 10")
        utiliser_objet(inventaire,"épée", 1)
        Boss_Final()
    elif item == "clé magique":
        Boss_pv -=20
        pv_perso-=5
        print("Drôle d'objet mystérieux, mais pourquoi pas. 20 points de puissance en plus")
        utiliser_objet(inventaire,"clé magique", 1)
        Boss_Final()
    else:
        print("Cet item n'est pas utilisable.")
        Boss_Final()

def utiliser_objet(inventaire, item, quantite):
    if item in inventaire:
        inventaire[item] -= quantite
    else:
        inventaire[item] = quantite

def afficher_inventaire(inventaire):
    print("Votre inventaire :")
    for objet, quantite in inventaire.items():
        print(f"{objet}: {quantite}")


def Jouer():
    while True:
        Choix_Jouer = input("A-Avancer B-Rester C-Inventaire D-Quitter : ")
        if Choix_Jouer == "A":
        
            Combats()
            Combats_2()
            Boss_Final()
        elif Choix_Jouer == "B":
            print("Vous êtes dans un environnement inconnu et pourtant qui vous semble familier")
            Jouer()
        elif Choix_Jouer == "C":
            Inventaire()
            Jouer()
        elif Choix_Jouer == "D":
            sauvegarder_partie()
            Menu()
        else:
            print("ERREUR!!!")
            Jouer()

def sauvegarder_partie():
    global inventaire, pv_perso

    data = {'inventaire': inventaire,'pv_perso': pv_perso}

    with open('nom_fichier', 'wb') as fichier:
      pickle.dump(data, fichier)
    print("Partie sauvegardée avec succès.")


def Combats():
    while True:
        print("Un monstre est devant vous et il n'a pas l'air de faire de la figuration")
        global Action, pv_perso, monstre_pv, Behemoth_pv,  inventaire
        Action = input("1-Attaquer 2-Fuir 3-Magie 4-Inventaire 5-Quitter et sauvegarder: ")
        if Action == '1':
            monstre_attaquer()
            if monstre_pv <= 0:
                print("Vous avez vaincu le monstre ! Retour à la fonction Jouer.")

                Combats_2()
                break
                
            else:
                monstre_attaque()
        elif Action == '2':
            print("Vous avez fui, on ne peut pas vous en vouloir pour ça")
            Jouer()
        elif Action == '3':
            monstre_attaquer()
            Magie()
            
        elif Action == '4':
            Inventaire()
            item_choice = input("Choisissez un item de l'inventaire à utiliser : ")
            if item_choice in inventaire:
                utiliser_item(item_choice) 
                inventaire.remove(item_choice)  
            else:
                print("Cet item n'est pas dans votre inventaire.")
            Combats()
        elif Action =='5':
            sauvegarder_partie()
            Menu()
        else:
            print("ERREUR!!!!")
            Combats()

def monstre_attaquer():
    global  monstre_pv
    if Action == '1':
        pv_modifier()  
        if monstre_pv > 0:
            print("Le Briseur d'âmes est toujours là, et il a l'air énervé. Il lui reste", monstre_pv, "points de vie.")
    elif Action == '3':
        pv_modifier()  
        if monstre_pv > 0:
            print("Le Briseur d'âmes est toujours là, et il a l'air énervé. Il lui reste", monstre_pv, "points de vie.")

def monstre_attaque():
    global pv_perso
    pv_perso -= 15  
    print("Le monstre vous attaque ! Vous avez maintenant", pv_perso, "points de vie restants.")
    Combats()
    if pv_perso <= 0:
        print("Vous avez été vaincu ! Dommage.")
        Menu()
    else:
        Jouer()

def pv_modifier():
    global pv, monstre_pv
    if Action == '1':
        monstre_pv -= 10  
    elif Action == '3':
        monstre_pv -= 20  

    global Name
    Name= "Briseur d'âme"
    print(Name)


def Combats_2():
    while True:
        print("Un monstre est devant vous et il n'a pas l'air de faire de la figuration")
        global Action, pv_perso, Behemoth_pv, Boss_pv, inventaire
        Action = input("1-Attaquer 2-Fuir 3-Magie 4-Inventaire 5-Quitter et sauvegarder: ")
        if Action == '1':
            monstre_attaquer_2()
            if Behemoth_pv <= 0:
                print("Vous avez vaincu le monstre ! Retour à la fonction Jouer.")
                Boss_Final()
                break
                
            else:
                monstre_attaque_2()
        elif Action == '2':
            print("Vous avez fui, on ne peut pas vous en vouloir pour ça")
            Jouer()
        elif Action == '3':
            monstre_attaquer_2()
            Magie_2()
            
        elif Action == '4':
            Inventaire()
            item_choice = input("Choisissez un item de l'inventaire à utiliser : ")
            if item_choice in inventaire:
                utiliser_item_2(item_choice) 
                inventaire.remove(item_choice)  
            else:
                print("Cet item n'est pas dans votre inventaire.")
            Combats_2()
        elif Action =='5':
            sauvegarder_partie()
            Menu()
        else:
            print("ERREUR!!!!")
            Combats_2()

def monstre_attaquer_2():
    global  Behemoth_pv
    if Action == '1':
        pv_modifier_2()  
        if Behemoth_pv > 0:
            print("Le Behemoth est toujours là, et il a l'air énervé. Il lui reste", Behemoth_pv, "points de vie.")
    elif Action == '3':
        pv_modifier_2()  
        if Behemoth_pv > 0:
            print("Le Behemoth est toujours là, et il a l'air énervé. Il lui reste", Behemoth_pv, "points de vie.")

def monstre_attaque_2():
    global pv_perso
    pv_perso -= 25 
    print("Le monstre vous attaque ! Vous avez maintenant", pv_perso, "points de vie restants.")
    Combats_2()
    if pv_perso <= 0:
        print("Vous avez été vaincu ! Dommage.")
        Menu()
    else:
        Jouer()

def pv_modifier_2():
    global pv, Behemoth_pv
    if Action == '1':
        Behemoth_pv -= 10  
    elif Action == '3':
        Behemoth_pv -= 20  

    global Name_2
    Name_2= "Behemoth"
    print(Name_2)



def Boss_Final():
    while True:
        print("Un monstre est devant vous et il n'a pas l'air de faire de la figuration")
        global Action, pv_perso, Boss_pv, inventaire
        Action = input("1-Attaquer 2-Fuir 3-Magie 4-Inventaire 5-Quitter et sauvegarder: ")
        if Action == '1':
            monstre_attaquer_2()
            if Boss_pv <= 0:
                print("Vous avez vaincu tous nos monstre ! Félicitation, vous pouvez recomencez.")
                Menu()
                break
                
            else:
                monstre_attaque_3()
        elif Action == '2':
            print("Vous avez fui, on ne peut pas vous en vouloir pour ça")
            Jouer()
        elif Action == '3':
            monstre_attaquer_3()
            Magie_Boss()
            
        elif Action == '4':
            Inventaire()
            item_choice = input("Choisissez un item de l'inventaire à utiliser : ")
            if item_choice in inventaire:
                utiliser_item_Boss(item_choice) 
                inventaire.remove(item_choice)  
            else:
                print("Cet item n'est pas dans votre inventaire.")
            Boss_Final()
        elif Action =='5':
            sauvegarder_partie()
            Menu()
        else:
            print("ERREUR!!!!")
            Boss_Final()

def monstre_attaquer_3():
    global  Boss_pv
    if Action == '1':
        pv_modifier_3()  
        if Boss_pv > 0:
            print("Ganonduff est toujours là, et il a l'air énervé. Il lui reste", Boss_pv, "points de vie.")
    elif Action == '3':
        pv_modifier_3()  
        if Boss_pv > 0:
            print("Ganonduff est toujours là, et il a l'air énervé. Il lui reste", Boss_pv, "points de vie.")

def monstre_attaque_3():
    global pv_perso
    pv_perso -= 30
    print("Le monstre vous attaque ! Vous avez maintenant", pv_perso, "points de vie restants.")
    Boss_Final()
    if pv_perso <= 0:
        print("Vous avez été vaincu ! Dommage.")
        Menu()
    else:
        Jouer()

def pv_modifier_3():
    global pv, Boss_pv
    if Action == '1':
        Boss_pv -= 10  
    elif Action == '3':
        Boss_pv -= 20  

    global Name_3
    Name_3= "Ganonduff"
    print(Name_3)





def Magie():
    print("Utilisation de la magie, 20 de dégats")
    monstre_attaquer()
    Combats()
    monstre_attaquer_2()
    Combats_2()
    monstre_attaquer_3()
    Boss_Final()

def Magie_2():
    print("Utilisation de la magie, 20 de dégats")
    monstre_attaquer_2()
    Combats_2()
  
def Magie_Boss():
    print("Utilisation de la magie, 20 de dégats")
    monstre_attaquer_3()
    Boss_Final()



def Inventaire():
   
    afficher_inventaire(inventaire)

def Menu():
    
    Choix_Menu = input("A-Jouer B-Continuer C-Credit D-Quitter : ")
    if Choix_Menu == "A":
        print("Vous êtes dans un environnement inconnu et pourtant qui vous semble familier")
        Jouer()
    elif  Choix_Menu == "B":
        Continuer()
    elif Choix_Menu == "C":
        Credit()
    elif Choix_Menu == "D":
        Quitter()
    else:
        print("ERREUR!!!")
        Menu()

def Continuer():
    print("Continuer le jeu")
    Jouer()

Concepteurs="OUARDI Ahmed-Amine, RABHI Ilyas, KEKLIK Alican"
def Credit():
    print("Concepteurs:",Concepteurs)
    Menu()

def Quitter():
    print("Quitter le jeu")
    Menu()

Menu()