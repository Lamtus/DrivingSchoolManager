import json
import os,time
#from MiniProjet.function1 import * 
def saisie_cat():
    c=input("Taper la catégorie (A : moto, B :voiture, C : camion) : \n")
    while (c.upper() !="A" and c.upper() != "B" and c.upper() !="C"):
        c=input("Taper la catégorie (A : moto, B :voiture, C : camion) : \n")
    return(c.upper())
def saisie_cin():
    CIN=input("Taper le numero de CIN : \n")
    contenu={}
    try:
        with open("MiniProjet/candidate.json") as ca:
            contenu = json.load(ca)
    except:contenu={}
    while len(CIN)!= 8 or CIN.isdigit()==False :
        CIN=input("Taper le numero de CIN : \n")   
    return (CIN)
def saisie_Im():
    print("Taper le numero d'immatriculation de la vehicule ")
    num1=input("Le numero comp ose de 4 chiffres : \n")
    while len(num1)>4 or num1.isdigit()==False:
            num1=input("Le numero compose de 4 chiffres : \n")
    num2=input("Le numero compose de 3 chiffres : \n")
    while len(num2)>3 or num2.isdigit()==False :
            num2=input("Le numero compose de 3 chiffres : \n")
    im= num1+"tu"+num2    
    return(im)
def saisie_km():
    km=int(input("Taper le kilometrage totale de la vehicule : \n"))
    while km <0 :
        km=int(input("Taper le kilometrage totale de la vehicule : \n"))
    return(km)

def saiseheure():
    h=int(input("taper l'heure : \n"))
    while h<6 or h>20:
        h=int(input("taper l'heure : \n"))
    m=int(input("taper les minutes : \n"))
    while m<0 or m>60:
        m=int(input("taper les minutes : \n"))
    heure=str(h)+":"+str(m)
    return(heure)

def saisie_date():    
    date=input("La date d'envoi (JJ/MM/AA) : ")
    while(len(date) != 8):
        print ("Veuillez respecter les 8 caracteres demandes")
        print ("La date d'envoi (JJ/MM/AA) : ")
        date = input()
    else:
        while(date[2] != '/' or date[5] != '/'):
            #controle des nombres jours et mois
            print ("Veuillez respecter le format date JJ/MM/AA requis")
            print ("La date d'envoi (JJ/MM/AA) : ")
            date = input()
        else:
            # verifier la saisie de chiffres
            jour = int(date[:2])
            mois = int(date[3:5])
            annee = int(date[6:])
 
            while mois > 13 or mois < 0:
                print ("Erreur: Mois Invalide")
                date = input()
                jour = int(date[:2])
                mois = int(date[3:5])
                annee = int(date[6:])
            if mois in (1, 3, 5, 7, 8, 10, 12):
                while jour > 31:
                    print ("Erreur: Le jour ne peut contenir que 31 jours.")
                    print ("Veuillez resaisir le jour: ")
                    jour = int(input())
                date=str(jour)+date[2:]
            elif mois == 2:
                if annee % 4 == 0:
                    while jour > 30:
                        print ("Erreur: Le jour ne peut contenir que 29 jours.")
                        print ("Veuillez resaisir le jour: ")
                        jour = int(input())
                date=str(jour)+date[2:]
            else:
                while jour > 29:
                    print ("Erreur: Le jour ne peut contenir que 28 jours.")
                    jour = int(input())
                else:
                    while jour > 31:
                        print ("Erreur: Le jour ne peut contenir que 30 jours.")
                        jour = int(input())
                date=str(jour)+date[2:]
    return(date)
def saisie_tel():
    tel=input("Taper votre numero de telephone : ")
    while tel.isdigit() != True:
        print("veuillez saisir votre numero de tel correctement ")
        tel=input("Taper votre numero de telephone : ")
    return(tel)
def saisie_tab_cod():
    nb_code= int(input("taper le nombre de seance de code : \n"))
    while nb_code < 0:
        nb_code= int(input("taper le nombre de seance de code : \n"))
    tab1=[]
    if nb_code !=0:
            nb=1
            for e in range(nb_code):
                seance={}
                date=saisie_date()
                heure=saiseheure()
                ing=input("Taper le nom de l'ingenieur : \n")
                seance={nb:[date,heure,ing]}
                tab1.append(seance)
                nb+=1    
    return(tab1)
def saisie_tab_con():
    nb_con=int(input("taper le nomnre de seance de conduite : \n"))
    while nb_con <0:
        nb_con=int(input("taper le nomnre de seance de conduite : \n"))
    Tab2=[]
    if nb_con !=0:
        nb=1
        for e in range(nb_con):
            seance={}
            date=saisie_date()
            heure=saiseheure()
            ing=input("Taper le nom de l'ingenieur : \n")
            try:
                with open("MiniProjet/vehicule.json") as ca:
                    contenu = json.load(ca)
            except:contenu={}
            im=saisie_Im()
            while recherche(contenu,im) != True:
                im=saisie_Im()        
            seance={nb:[date,heure,ing,im]}
            Tab2.append(seance)
            nb+=1
    return(Tab2)
def ajout_condidat():
    try:
        with open("MiniProjet/candidate.json") as ca:
            contenu=json.load(ca)
    except:contenu={}
    CIN=saisie_cin()    
    while recherche(contenu,CIN)!=False:
        print("ce candidat existe deja ")
        CIN=saisie_cin()    
    c=saisie_cat()
    nom=input("taper votre nom : ")
    prenom=input("taper votre prenom : ")
    tlf=saisie_tel()
    #L= saisie_tab_cod()
    #L1= saisie_tab_con()
    #candidat={CIN:[c,L,L1]}
    contenu[CIN]=[c,nom,prenom,tlf]
    with open("MiniProjet/candidate.json","w") as ca:
        json.dump(contenu,ca,indent=2)
def ajout_vehicule():
    try:
        with open("MiniProjet/vehicule.json") as ca:
            contenu = json.load(ca)
    except:contenu={}
    im=saisie_Im()
    while recherche(contenu,im)!= False:
        im=saisie_Im()        
    date= saisie_date()
    km=saisie_km()
    pr_vd = (int(str(km % 100000)[0])+1)*10000 - (km % 100000)
    #vehicule={im:[date,km,pr_vd]}
    try:
        with open("MiniProjet/vehicule.json") as v:
            contenu=json.load(v)
    except :contenu[im] = [date,km,pr_vd]
    contenu[im]=[date,km,pr_vd]
    with open("MiniProjet/vehicule.json","w") as v:
        json.dump(contenu,v,indent=2)
def recherche(dict,x):
    for e in dict:
        if e in x.split(","):
            return(True)
    return(False)
def recherche1(dict,a,h):
  for e in dict:
    if a and h in e.split(","):
      return(True)
  return(False)
def supp(dict,x):
    for e in dict:
        if x in e:
            del dict[e]
            break
    while recherche(dict,x)==True:
        supp(dict,x)
def count(dict,x):
    nb=0
    for e in dict:
        if x in e :
            nb+=1
    return(nb)       

def supp_candidat():
    CIN_sup=saisie_cin()
    with open("MiniProjet/candidate.json") as c:
        contenu=json.load(c)
    if recherche(contenu,CIN_sup) == False:
        print("ce candidat n'existe pas")
    else:
        supp(contenu,CIN_sup)
        with open ("MiniProjet/candidate.json","w") as c1:
            json.dump(contenu,c1,indent=2)
        try:
            with open("MiniProjet/seance_conduite.json")as s:
                contenu1=json.load(s)
        except:contenu1={}
        print(contenu1)
        supp(contenu1,CIN_sup)
        with open ("MiniProjet/seance_conduite.json","w") as c2:
            json.dump(contenu1,c2,indent=2)
        try:
            with open("MiniProjet/seance_code.json")as s1:
                contenu2=json.load(s1)
        except:contenu2={}
        print(contenu2)
        supp(contenu2,CIN_sup)
        with open ("MiniProjet/seance_code.json","w") as c1:
            json.dump(contenu2,c1,indent=2)
        

def supp_vehicule():
    Im_supp=saisie_Im()
    with open ("MiniProjet/vehicule.json") as v:
        contenu=json.load(v)
        if recherche(contenu,Im_supp)==False:
            print("cette vehicule n'existe pas ")
        else:
            supp(contenu,Im_supp)
            with open ("MiniProjet/vehicule.json","w") as v1:
                json.dump(contenu,v1,indent=2)
def modif_cand():
    CIN_R=saisie_cin()
    try:
        with open("MiniProjet/candidate.json") as ca:
            contenu=json.load(ca)
    except:contenu={}
    if recherche(contenu,CIN_R)==False:
        print("ce candidat n'existe pas")
    else:
        print("0 : Modifier Nom \n1 : Modifier Prenom\n2: Modifier le num de tel\n")
        x=int(input("Taper votre choix"))
        while(x!=0 and x!=1 and x!=2):
            x=int(input("0 : Modifier les senaces de code \n1 : Modifier les seances de conduite\n"))
        if(x==0):
            nom=input("Taper votre nom : ")
            contenu[CIN_R][1]=nom
            with open("MiniProjet/candidate.json","w") as r:
                json.dump(contenu,r,indent=2)
        elif x==1:
            prenom=input("taper votre prenom : ")
            contenu[CIN_R][2]=prenom
            with open("MiniProjet/candidate.json","w") as r:
                json.dump(contenu,r,indent=2)
            with open("MiniProjet/candidate.json","w") as r:
                json.dump(contenu,r,indent=2)
        else:
            tel=saisie_tel()
            contenu[CIN_R][3]=tel
            with open("MiniProjet/candidate.json","w") as r:
                json.dump(contenu,r,indent=2)
            with open("MiniProjet/candidate.json","w") as r:
                json.dump(contenu,r,indent=2)
def modif_vehicule():
    Im_R=saisie_Im()
    try:
        with open("MiniProjet/vehicule.json") as ca:
            contenu=json.load(ca)
    except:contenu={}
    if recherche(contenu,Im_R)==False:
        print("cette vehicule n'existe pas")
    else:
        nb=int(input("Taper le nouveau kilometrage de la vehicule : "))
        while(nb<contenu[Im_R][1]):
                nb=int(input("Taper le nombre de seance a ajouter")) 
        contenu[Im_R][1]=nb 
        contenu[Im_R][2]=(int(str(nb % 100000)[0])+1)*10000 - (nb % 100000)              
        with open("MiniProjet/vehicule.json","w") as r:
            json.dump(contenu,r,indent=2)
def menu_candidat():
    os.system("cls")
    print("\t\t GESTION DES CANDIDATS\n\n")
    print("\t\3 1 SAISIE D'UN CANDIDAT \n")
    print("\t\3 2 SUPPRESSION D'UN CANDIDAT \n")
    print("\t\3 3 MODIFICATION D'UN CANDIDAT \n")
    print("\t\3 4 AFFICHAGE D'UN CANDIDAT \n")
    print("\t\3 0 RETOUR \n")
    choix=input("Taper votre choix :")
    while choix !="1" and choix !="2" and choix !="3"and choix!="4"and choix!="0":
        choix=input("Taper votre choix :")
    if choix=="1":
        os.system("cls")
        print("\n\n\n\n\n\n")
        ajout_condidat()
    elif choix=="2":
        os.system("cls")
        print("\n\n\n\n\n\n")
        supp_candidat()
        x=input("")
    elif choix=="3":
        os.system("cls")
        print("\n\n\n\n\n\n")
        modif_cand()
        x=input("")
    elif choix=="4":
        os.system("cls")
        print("\n\n\n\n\n\n")
        affichage_candidat()
    else:
        menu_principale()    
def menu_vehicule():
    os.system("cls")
    print("\t\t GESTION DES VEHICULES\n\n")
    print("\t\3 1 SAISIE D'UNE VEHICULE \n")
    print("\t\3 2 SUPPRESSION D'UNE VEHICULE \n")
    print("\t\3 3 MODIFICATION D'UNE VEHICULE \n")
    print("\t\3 4 INFORMATION SUR UNE VEHICULE \n")
    print("\t\3 5 LISTE DES VEHICULES\n")
    print("\t\3 0 RETOUR \n")
    choix=input("Taper votre choix :")
    while choix !="1" and choix !="2" and choix !="3"and choix!="4"and choix!="5":
        choix=input("Taper votre choix :")
    if choix=="1":
        os.system("cls")
        print("\n\n\n\n\n\n")
        ajout_vehicule()
    elif choix=="2":
        os.system("cls")
        print("\n\n\n\n\n\n")
        supp_vehicule()
        x=input("")
    elif choix=="3":
        os.system("cls")
        print("\n\n\n\n\n\n")
        modif_vehicule()
        x=input("")
    elif choix=="4" :
        os.system("cls")
        print("\n\n\n\n\n\n")
        affichage_vehicule()
    elif choix=="5" :
        os.system("cls")
        print("\n\n\n\n\n\n")
        liste_vehicule() 
    else :
        os.system("cls")
        menu_principale()       
def affichage_candidat():
    CIN=saisie_cin()
    with open("MiniProjet/candidate.json") as c:
        contenu=json.load(c)
    if recherche(contenu,CIN) == False:
        print("ce candidat n'existe pas")
    else:
        try:
            with open("MiniProjet/seance_conduite.json")as s:
                contenu2=json.load(s)
        except:
            contenu2={}
        try:
            with open("MiniProjet/seance_code.json")as s:
                contenu1=json.load(s)
        except:
            contenu1={}
        if contenu[CIN][0]=="A":
            pd=0.02
            pt=0.04
        elif contenu[CIN][0]=="B":                
            pd=0.03
            pt=0.06
        else:
            pd=0.05
            pt=0.08
        print("Categorie : ",contenu[CIN][0],
        "\nNom : ",contenu[CIN][1],
        "\nPrenom : ",contenu[CIN][2],
        "\nNum TEL : ",contenu[CIN][3])
        print("\nNombre de seance de code : ",count(contenu1,CIN),
        "\nNombre de seance de conduite : ",count(contenu2,CIN),
        "\nLe prix des seances de code : ",count(contenu1,CIN)*(1+pd)*15,
        "Dt \nLe prix des seances de conduite : ",count(contenu2,CIN)*(1+pt)*15,
        "Dt\nLe prix totale : ",count(contenu1,CIN)*(1+pd)*15+count(contenu2,CIN)*(1+pt)*15,"Dt\n")
        x=input()
def affichage_vehicule():
    im=saisie_Im()
    with open("MiniProjet/vehicule.json") as c:
        contenu=json.load(c)
        if recherche(contenu,im) == False:
            print("cette vehicule n'existe pas")
        else:
            print("Le prochain entretien est apres ",contenu[im][2],"Km")
            x=input()
def ajout_seance_code():
    date=saisie_date()
    heure=saiseheure()
    cin=saisie_cin()
    try:
        with open("MiniProjet/seance_code.json")as s:
            contenu=json.load(s)
    except:contenu={}
    try:
        with open("MiniProjet/candidate.json") as ca:
            contenu1=json.load(ca)
    except:contenu1={}
    while(recherche(contenu1,cin)!=True or recherche1(contenu,date,heure)!=False):
        print("veuillez saisir les informations correctement")
        date=saisie_date()
        heure=saiseheure()
        cin=saisie_cin()
    ing=input("Taper le nom de l'ingenieur : \n")
    contenu[date+","+heure+","+cin]=[ing]
    with open("MiniProjet/seance_code.json","w")as s:
        json.dump(contenu,s,indent=2)
def modification_seance_code():
    cin=saisie_cin()
    try:
        with open("MiniProjet/candidate.json")as s:
            contenu=json.load(s)
    except:contenu={}
    if recherche(contenu,cin)==False:
        print("Ce candidat n'existe pas")
    else :
        date=saisie_date()
        h=saiseheure()
        if(recherche1(contenu,date,h)==False):
            print("cette senace n'existe pas")
        else:
            ingen=input("Taper le nom del'ingenieur")
            contenu[date,h,cin]=[ingen]
            with open("MiniProjet/seance_code","w")as r:
                json.dump(contenu,r,indent=2)
    x=input("")
def modification_seance_conduite():
    cin=saisie_cin()
    try:
        with open("MiniProjet/candidate.json")as s:
            contenu=json.load(s)
    except:
        contenu={}
    if recherche(contenu,cin)==False:
        print("Ce candidat n'existe pas")
    else :
        date=saisie_date()
        h=saiseheure()
        if(recherche1(contenu,date,h)==False):
            print("cette senace n'existe pas")
        else:
            ingen=input("Taper le nom del'ingenieur")
            contenu[date,h,cin]=[ingen]
            with open("MiniProjet/seance_conduite","w")as r:
                json.dump(contenu,r,indent=2)
    x=input("")
def  ajout_seance_conduite(): 
    date=saisie_date()
    heure=saiseheure()
    cin=saisie_cin()
    try:
        with open("MiniProjet/seance_conduite.json")as s:
            contenu=json.load(s)
    except:
        contenu={}
    try:
        with open("MiniProjet/candidate.json") as ca:
            contenu1=json.load(ca)
    except:contenu1={}

    while(recherche(contenu1,cin)!=True or recherche1(contenu,date,heure)!=False):
        print("veuillez saisir les informations correctement")
        date=saisie_date()
        heure=saiseheure()
        cin=saisie_cin()
    im=saisie_Im()
    try:
        with open("MiniProjet/vehicule.json") as c:
            contenu1=json.load(c)
    except: 
        contenu1={}
    while(recherche(contenu1,im)==False):
        print("cette vehicule n'existe pas dans notre auto_ecole \nveuillez saisir le num de matricule correctement")
        im=saisie_Im()
    ing=input("taper l'ingenieur")
    contenu[date+","+heure+","+cin]=[im,ing]
    with open("MiniProjet/seance_conduite.json","w")as s:
        json.dump(contenu,s,indent=2)

def menu_seance():
    os.system("cls")
    print("\t\t GESTION DES SEANCES\n\n")
    print("\t\3 1 SEANCE DE CODE \n")
    print("\t\3 2 SEANCE DE CONDUITE \n")
    print("\t\3 0 RETOUR \n")
    choix=input("Taper votre choix :")
    while choix !="1" and choix !="2"and choix!="0" :
        choix=input("Taper votre choix :")
    if choix=="1":
        os.system("cls")
        menu_code()
    elif choix=="2":
        os.system("cls")
        menu_conduite()
    else:
        menu_principale()
def menu_code():
    os.system("cls")
    print("\t\t GESTION DES SEANCES DE CODE\n\n")
    print("\t\3 1 AJOUT \n")
    print("\t\3 2 MODIFICATION \n")
    print("\t\3 0 RETOUR \n")
    choix=input("Taper votre choix :")
    while choix !="1" and choix !="2"and choix!="0" :
        choix=input("Taper votre choix :")
    if choix=="1":
        os.system("cls")
        ajout_seance_code()
    elif choix=="2":
        os.system("cls")
        modification_seance_code()
    else:
        os.system("cls")
        menu_seance()
def menu_conduite():
    os.system("cls")
    print("\t\t GESTION DES SEANCES DE CONDUITE\n\n")
    print("\t\3 1 AJOUT \n")
    print("\t\3 2 MODIFICATION \n")
    print("\t\3 0 RETOUR \n")
    choix=input("Taper votre choix :")
    while choix !="1" and choix !="2" and choix!="0":
        choix=input("Taper votre choix :")
    if choix=="1":
        os.system("cls")
        ajout_seance_conduite()
    elif choix=="2":
        os.system("cls")
        modification_seance_conduite()
    else:
        os.system("cls")
        menu_seance()
def liste_vehicule():
    try:
        with open("MiniProjet/vehicule.json")as v:
            contenu=json.load(v)
    except:
        contenu={}
    if len(contenu)==0:
        print("Le parc est vide")
    else:
        i=1
        for e in contenu:
            print("vehicule : ",i,"\nMatricule : ",e)
            i+=1
    x=input("")
def menu_principale():
    os.system("cls")
    print("\t\t BIENVENUE DANS NOTRE AUTOECOLE\n\n")
    print("\2 1  CANDIDAT\n")
    print("\2 2  VEHICULE\n")
    print("\2 3 SEANCE \n")
    print("\2 0 QUITTER \n")
    choix=input("Taper votre choix :")
    while choix=="1"and choix =="2"and choix=="0"and choix=="3":
        choix=input("Taper votre choix :")
    while(choix!="0"):
        if choix=="1":
            os.system("cls")
            menu_candidat()
        elif choix=="2":
            os.system("cls")
            menu_vehicule()
        else:
            os.system("cls")
            menu_seance()
        os.system("cls")
        print("\t\t BIENVENUE DANS NOTRE AUTOECOLE\n\n")
        print("\2 1  CANDIDAT\n")
        print("\2 2  VEHICULE\n")
        print("\2 3 SEANCE \n")
        print("\2 0 QUITTER \n")
        choix=input("Taper votre choix :")
        while choix=="1"and choix =="2"and choix=="0"and choix!="3":
            choix=input("Taper votre choix :")