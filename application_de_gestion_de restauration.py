# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 00:53:55 2021

@author: Ayoub Mabrouk
"""

def gestion_de_commande(LC):
    print(''' Gestion de commande

          1. Afficher les listes de commandes

          2. Chercher un commande
          3. Ajouter un commande
          4. Modifier un commande
          5. Supprimer un commande
          6. Retournez au menu précédant
''')
    a=input("quel est vote choix: ")
    while a not in ['1','2','3','4','5','6']:
        a=input("Choix invalidé, Quel est vote choix: ")
    if a=='1':
        Afficher_CM(LC)
        gestion_de_commande(LC)
    elif a=='2':
        Chercher_CM(LC)
        gestion_de_commande(LC)
    elif a=='3':
        Ajouter_CM(LC)
        gestion_de_commande(LC)
    elif a=='4':
        Modifier_CM(LC)
        gestion_de_commande(LC)
    elif a=='5':
        Supprimer_CM(LC)
        gestion_de_commande(LC)
    elif a=='6':
        login()
def Afficher_CM(LC):
    for i in LC:
        print(i)
def Chercher_CM(LC):
    print('''
seletionner le méthode de rechercher:
''')
    a=input("Donner le code commande: ")
    test=False
    commande=[]
    for i in LC:
        if a in i:
            commande=i
            test=True
    if test==False:
        print("Commande n'est pas trouve")
    else:
        print("Commnde a ete trouve")
        print(commande)
def Ajouter_CM(LC):
    CM=[]
    x=input("Code de commande: ")
    a=input("nombre de commande: ")
    b=input("ID de client: ")
    c=input("de quoi s'agit il la commande: ")
    d=input("le prix de commande: ")
    e=input("sur place ou emporter: ")
    f=input("temps d'attente moyenne: ")
    g=input("est ce que confirme la commande ou non?: ")
    CM.append(x)
    CM.append(a)
    CM.append(b)
    CM.append(c)
    CM.append(d)
    CM.append(e)
    CM.append(f)
    CM.append(g)
    LC.append(CM)

def Modifier_CM(LC):
    print("Modifier un commande")
    a=input("Donner le commande a modifier:(Code de commande): ")
    commande=[]
    test=False
    for i in LC:
        if a in i:
            commande=i
            test=True
    if test==False:
        print("commande n'ete pas trouve")
    else:
        commande[0]=input(" Donner le nouveau code de commande: ")
        commande[1]=input(" Donner le nouveaux nombre de commande: ")
        commande[2]=input(" Donner le louveaux ID de client: ")
        commande[3]=input(" De quoi s'agit il la commande: ")
        commande[4]=input("Le prix de commande: ")
        commande[5]=input("sur place ou emporter: ")
        commande[6]=input("temps d'attente moyenne: ")
        commande[7]=input("est ce que confirme la commande ou non?: ")
        for i in LC:
            if a in i:
                i=commande
        print("The commande a ete change")
def Supprimer_CM(LC):
    print("Supprimer un commande")
    a=input("Donner le code de commande a supprimer: ")
    test=False
    for i in LC:
        if a in i:
            test=True
            LC.remove(i)
    if test==True:
        print("Commande supprimer")
    else:
        print("Commande n'ete pas trouvé")
def Generate_Id(lm):
    from random import randint
    ID = str(randint(0,10000))
    for clt in lm:
        if clt[5] == ID:
            return Generate_Id(lm)
    return ID


def Generate_Id():
    from random import randint
    ID = str(randint(0,10000))
    return ID


def len_0(x):
    while len(x)==0:
        print("  x est obligatoire a remplir")
        x=input(''' S'il vous plaît remplissez-le:''')

    return x
def Len_8(x):
    while len(x)!=8:
        print("Le N° de x Doit contenir 8 chiffre")
        x=input(''' Réessayer:
>> ''')
    return x
def no_chiffre(x):
    i=0 
    j=0 
    while j<len(x):
        if x[i] in ['a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n']:           
            i=i+1
            j=j+1 
        else:
            x=input('la saisie doit contenir que des caractére:')
            j=0
        x=len_0(x)
    return x
    
def ajoute(liste_malades,liste_homme_femme, liste_enfant):
    print('''                                             ---------------------------
                                                          *    Ajouter un client  *
                                                                ----------------

                                                                                                                                ''')
    
    
    list1=["nom","prenom","region","date_de_naissance","telephone","ID"]
    choix_repeter=1
    while choix_repeter:
        cible = -1
        while cible not in range(0,3):
            cible=int(input("0: les malades\n1: homme/femme\n2: enfant\n"))
        if cible==0:
            
            i=0
            client=[]
            while i<len(list1):
                
                    print("entre les ",list1[i])
                    if list1[i]=="nom":
                        x=input("nom :")
                        x=len_0(x)
                        x=no_chiffre(x)
                        client.append(x)
                    elif list1[i]=="prenom":
                        x=input("prenom:")
                        x=len_0(x)
                        x=no_chiffre(x)
                        client.append(x)
                    elif list1[i]=="region":
                         x=input("region:")
                         x=len_0(x)
                         x=no_chiffre(x)
                         client.append(x)
                    elif list1[i]=="date_de_naissance":
                        x=(input("date_de_naissance:"))
                        x=Len_8(x)
                        client.append(x)
                    elif list1[i]=="telephone":
                        x=(input("telephone:"))
                        x=Len_8(x)
                        client.append(x)
                        liste_malades.append(client)   
                    else:
                        client.append(Generate_Id())
                        liste_malades.append(client)
                    
                    i=i+1    
        elif cible==1:
            i=0
            client=[]
            while i<len(list1):
                  print("entre les ",list1[i])
                  if list1[i]=="nom":
                    x=input("nom :")
                    x=len_0(x)
                    x=no_chiffre(x)
                    client.append(x)
                  elif list1[i]=="prenom":
                    x=input("prenom:")
                    x=len_0(x)
                    x=no_chiffre(x)
                    client.append(x)
                  elif list1[i]=="region":
                     x=input("region:")
                     x=len_0(x)
                     x=no_chiffre(x)
                     client.append(x)
                  elif list1[i]=="date_de_naissance":
                    x=(input("date_de_naissance:"))
                    x=Len_8(x)
                    client.append(x)
                    
                  elif list1[i]=="telephone":
                    x=(input("telephone:"))
                    x=Len_8(x)
                    client.append(x)
                    liste_homme_femme.append(client) 
                  else:
                        client.append(Generate_Id())
                        liste_malades.append(client)  
                  i=i+1
                
        else:
            i=0
            client=[]
            while i<len(list1):
                 print("entre les ",list1[i])
                 if list1[i]=="nom":
                    x=input("nom :")
                    x=len_0(x)
                    x=no_chiffre(x)
                    client.append(x)
                 elif list1[i]=="prenom":
                    x=input("prenom:")
                    x=len_0(x)
                    x=no_chiffre(x)
                    client.append(x)
                 elif list1[i]=="region":
                     x=input("region:")
                     x=len_0(x)
                     x=no_chiffre(x)
                     client.append(x)
                 elif list1[i]=="date_de_naissance":
                    x=(input("date_de_naissance:"))
                    x=Len_8(x)
                    client.append(x)
                    
                 elif list1[i]=="telephone":
                    x=(input("telephone:"))
                    x=Len_8(x)
                    client.append(x)
                    liste_enfant.append(client)
                 else:
                     client.append(Generate_Id())
                     liste_malades.append(client)
                 i=i+1
                 
        choix_repeter=int(input("est-ce que vous voulez ajouter autre client ?\n0: non \n1:oui "))
def modifie(liste_malades,liste_homme_femme,liste_enfant):
         print("""                            -------------------------
                                                *  modifier client*
                                                   -------------                              
                                                                                                  """)
      
                                                                                                            
         choix_repeter="oui"
         while choix_repeter=="oui":
             
                                                                                               
   
            choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades\n liste_homme_femme\n liste_enfant\n  :")
            while choix_liste not in ["liste_malades","liste_homme_femme","liste_enfant","quitter"]:
                choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades/liste_homme_femme/liste_enfant :")
                choix_liste=choix_liste.lower()
            if choix_liste=="liste_malades":
                        print("Modifier un client")
                        a=input("Donner le ID de  client modifier: ")
                        client=[]
                        test=False
                        for i in liste_malades:
                            if a in i:
                                client=i
                                test=True
                        if test==False:
                            print("client n'ete pas trouve")
                        else:
                            client[0]=input(" Donner le nouveau nom de client: ")
                            client[1]=input(" Donner le prenom de client: ")
                            client[2]=input(" Donner le region: ")
                            client[3]=input(" nouveaux date de naissance ")
                            client[4]=input("nouveaux telephone: ")
                            break
                            
            if choix_liste=="liste_homme_femme":
                        print("Modifier un client")
                        a=input("Donner le  ID client modifier: ")
                        client=[]
                        test=False
                        for i in liste_homme_femme:
                            if a in i:
                                client=i
                                test=True
                        if test==False:
                            print("client n'ete pas trouve")
                        else:
                              client[0]=input(" Donner le nouveau nom de client: ")
                              client[1]=input(" Donner le prenom de client: ")
                              client[2]=input(" Donner le region: ")
                              client[3]=input(" nouveaux date de naissance ")
                              client[4]=input("nouveaux telephone:")
                              break
            if choix_liste=="liste_enfant":
                        print("Modifier un client")
                        a=input("Donner le ID client modifier: ")
                        client=[]
                        test=False
                        for i in liste_enfant:
                            if a in i:
                                client=i
                                test=True
                        if test==False:
                            print("client n'ete pas trouve")
                        else:
                            client[0]=input(" Donner le nouveau nom de client: ")
                            client[1]=input(" Donner le prenom de client: ")
                            client[2]=input(" Donner le region: ")
                            client[3]=input(" nouveaux date de naissance ")
                            client[4]=input("nouveaux telephone: ")
                            break
            choix_repeter=input("est-ce que vous voulez rechercher autre client ???((oui)/(non)")



def supprimer(liste_malades,liste_homme_femme,liste_enfant):
        print("""                           -----------------------
                                             * supprimer client*
                                                -------------
                                                                                                     """)
   
        choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades/liste_homme_femme/liste_enfant/quitter  :")
        while choix_liste not in ["liste_malades","liste_homme_femme","liste_enfant","quitter"]:
            choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades/liste_homme_femme/liste_enfant/quitter :")
            choix_liste=choix_liste.lower()
        
        if choix_liste=="liste_malades":
            test=False
            id_client=(input("entre votre ID ==>"))
            for i in liste_malades:
                if i[-1]==id_client:
                        test=True
                        liste_malades.remove(i)
            if test==True:
                print("client supprimer")
            else:
                print("client n'ete pas trouvé")
        elif choix_liste=="liste_homme_femme":
            test=False
            id_client=(input("entre votre ID ==>"))
            for i in liste_homme_femme:
                if i[-1]==id_client:
                        test=True
                        liste_homme_femme.remove(i)
            if test==True:
                print("client supprimer")
            else:
                print("client n'ete pas trouvé")
        elif choix_liste=="liste_enfant":
            
            test=False
            id_client=(input("entre votre ID ==>"))
            for i in liste_enfant:
                if i[-1]==id_client:
                        test=True
                        liste_enfant.remove(i)
            if test==True:
                print("client supprimer")
            else:
                print("client n'ete pas trouvé")
        
        elif choix_liste=="quitter":
            choix_repeter=input("Voulez-vous sortir ou chercher à nouveau? ???\(1:quitter/ 2:supprimer client)")
            i=0
            while i<3 and choix_repeter not in ["1","2"]:
                choix_repeter=input("Voulez-vous sortir ou chercher à nouveau? ???\(1:quitter/ 2:supprimer client)")
                i=i+1
            if choix_repeter=="2" :
                supprimer(liste_malades, liste_homme_femme, liste_enfant)
            else:
                return 


def rechercher(liste_malades,liste_homme_femme,liste_enfant):
    print("""                       -------------------------
                                     * recherhcer un client*
                                         -------------
                                                                                        """)
    choix_repeter="oui"
    while choix_repeter=="oui":
            choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades/liste_homme_femme/liste_enfant  :")
            while choix_liste not in ["liste_malades","liste_homme_femme","liste_enfant" ]:
                choix_liste=input("Quelle liste souhaitez-vous rechercher?\n liste_malades/liste_homme_femme/liste_enfant  :")
                choix_liste=choix_liste.lower()
                
            if choix_liste=="liste_malades":
                    v_choix=int(input("entre votre ID:"))
                    pos=-1
                    i=0
                    while i<len(liste_malades) and pos==-1:
                        if liste_malades[i][-1]==v_choix:
                           pos=i
                        else:
                           i=i+1
                    if pos==-1:
                        print("le client non trouve")
                    else:
                        print(v_choix,"est existe ala liste_malades")
            elif choix_liste=="liste_homme_femme":
                v_choix=int(input("entre votre ID:"))
                debut = 0
                fin = len(liste_homme_femme)-1
                pos = -1
                while fin<= debut and pos == -1 :
                    mil = (fin +debut)//2
                    if liste_homme_femme[mil] == v_choix :
                        pos = mil
                    elif liste_homme_femme[mil] > v_choix :
                        sup = mil - 1
                    else:
                        inf = mil + 1
                if pos == -1:
                    print(v_choix,"n’existe pas dans liste_homme_femme ")
                else:
                    print(v_choix,"existe dans liste_homme_femme")
            elif choix_liste=="liste_enfant":
                v_choix=int(input("entre votre ID:"))
                test=False
                for i in liste_enfant:
                    for j in i:
                        if j==v_choix:
                            test=True
                            break
                if test:
                   print(v_choix,"existe dans liste_enfant")
                    
                else: 
                   print(v_choix,"n'existe pas dans liste_enfant ")
            choix_repeter=input("est-ce que vous voulez rechercher autre client ???oui/non\n")
    
def afficher(liste_malades,liste_homme_femme,liste_enfant):
    list1=["nom","prenom","region","date_de_naissance","telephone","ID"]
    from tabulate import tabulate
    choix_affichage=(input("1.Voulez-vous ouvrir tous les clients?\n2.un client\n3.quitter\n===>"))
    while choix_affichage not in["1","2","3"]:
        choix_affichage=(input("1:Voulez-vous ouvrir tous les clients?\n2:un client\n"))
    if choix_affichage=="1":
            print("""                       ---------------------------
                                           * afficher tous les clients*
                                               -------------------                                    """)
            print("Quelle liste souhaitez-vous rechercher?")
            choix_liste=int(input("0.liste_malades\n1.liste_homme_femme\n2.liste_enfant\n :"))
            while choix_liste not in range(3):
                choix_liste=int(input("0.liste_malades\n1.liste_homme_femme\n2.liste_enfant\n :"))
                
            if choix_liste==0:
                    if len(liste_malades)==0:
                        print(" cette liste  est vide")
                    else:
                        for i in liste_malades:
                             print (tabulate(liste_malades,list1,tablefmt='fancy_grid'))
                             break
                            
            elif choix_affichage==1:
                         if len(liste_homme_femme)==0:
                             print(" cette liste  est vide")
                         else:
                             for i in liste_homme_femme:
                                 print (tabulate(liste_homme_femme,list1,tablefmt='fancy_grid'))
                                 break
                                  
            else:
                    if len(liste_enfant)==0:
                             print(" cette liste  est vide")
                    else:
                        for i in liste_enfant:
                                  print (tabulate(liste_enfant,list1,tablefmt='fancy_grid'))
                                  break
                    
                        
    elif choix_affichage=="2":
            
            print("""
                                                   ------------------------
                                                 *   afficher un client  *
                                                       --------------                                 """)
    
            test=False        
            ch1="oui"
            while ch1=="oui":
                print("Quelle liste souhaitez-vous rechercher?")
                choix_liste=input("liste_malades/liste_homme_femme/ liste_enfant :")
                if choix_liste=="liste_malades":
                    id_client=input("Le ID que vous recherchez :")
                    if len(liste_malades)==0:
                        print(" cette liste  est vide")
                    else:
                        for i in liste_malades:
                            if i[-1]==id_client:
                                print("ID :",i[5])
                                print("le nom de client  :",i[0])
                                print("le prenom de client  :",i[1])
                                print("le region de client  :",i[2])
                                print("le date de naissance de client  :",i[3])
                                print("le telephone de client  :",i[4])
                                break
                        
        
                elif choix_liste=="liste_homme_femme":
                    id_client=input("Le ID que vous recherchez :")
                    if len(liste_homme_femme)==0:
                        print(" cette liste  est vide")
                    else:
                       for i in liste_homme_femme:
                            if i[-1]==id_client:
                                print("ID :",i[5])
                                print("le nom de client  :",i[0])
                                print("le prenom de client  :",i[1])
                                print("le region de client  :",i[2])
                                print("le date de naissance de client  :",i[3])
                                print("le telephone de client  :",i[4])
                                break
                            
                elif choix_liste=="liste_enfant":
                    id_client=input("Le ID que vous recherchez :")
                    if len(liste_enfant)==0:
                        print(" cette liste  est vide")
                    else:
                        for i in liste_enfant:
                            if i[-1]==id_client:
                                print("ID :",i[5])
                                print("le nom de client  :",i[0])
                                print("le prenom de client  :",i[1])
                                print("le region de client  :",i[2])
                                print("le date de naissance de client  :",i[3])
                                print("le telephone de client  :",i[4])
                                break
                else:
                   return
                            
                ch1=input(" Voulez-vous afficher un autre client?\n oui/non==>")
    else:
        return
def client(liste_malades,liste_homme_femme,liste_enfant):
    print('''
                               1 .ajouter un client
                               2 .modifier un client
                               3 .supprimer un client
                               4 .rechercher un client
                               5 .afficher un client                                                ''')
    choix=input("votre choix :")
    while choix not in ["1","2","3","4","5"] :
        print("choix invalid ")
        choix=input("autre fois :")
    if choix=="1":
        ajoute(liste_malades,liste_homme_femme,liste_enfant)
        print(" le client est bien ajouter")
        client(liste_malades, liste_homme_femme, liste_enfant)
    elif choix=="2":
        modifie(liste_malades,liste_homme_femme,liste_enfant)
        print("le client bien modifier:")
        
    elif choix=="3":
        supprimer(liste_malades,liste_homme_femme,liste_enfant)
        print("client bien supprimer")
        client(liste_malades, liste_homme_femme, liste_enfant)
    elif choix=="4":
        rechercher(liste_malades,liste_homme_femme,liste_enfant)
        client(liste_malades, liste_homme_femme, liste_enfant)
    elif choix=="5":
        afficher(liste_malades,liste_homme_femme,liste_enfant)
        client(liste_malades,liste_homme_femme,liste_enfant)
    else:
        return



def ajouter (stock):
 ch="oui"
 while ch=="oui":
    el= input("ajouter la date d'aujourd'huit ")
    el1= input("ajouter le nom de l'element que vous voulez ajouter :")
    el2= input("ajouter la contité de l'element ajlouté :")
    el3= input("ajouter la date d'expiration de l'element ajouté :")
    st=[]
    st.append(el)
    st.append(el1)
    st.append(el2)
    st.append(el3)
    stock.append(st)
    print(stock)
    ch=input('vous voulez ajouter un autre element ? oui/non :')
def chercher (stock):
    ch1="oui"
    while ch1=="oui":
       p=input("quel est l element vous cherchez? :")
       teste=False
       i=0
       for i in stock:
           for j in i:
            if j==p:
             teste=True
             break
       if teste==True:
            print(p,"est en stock")

       else:
            print(p,'pas en stock')

       ch1=input("Est ce que vous voulez chercher une autre chose ? oui/non :")

def suprimer (stock):
    ch2="oui"
    while ch2=="oui":
        sup=input("ecrivez le nom de l'element que vous voulez suprimer?:")
        teste=False
        i=0
        for i in stock:
            for j in i:
              if j == sup:
                  teste=True
                  stock.remove(i)
                  break
        if teste==True:
           print(sup,"et ses informatio suprimé")
           print(stock)
        else:
            print("produit n est pas trouvé")
        ch2=input("vous voulez suprimer une autre chose ? oui/non :")

def nom(l,mod,stock):
    teste=-1
    k=-1
    for i in stock:
        k=k+1
        for j in i:
            if mod == j:
                teste=True
                return k
    return teste

def saisir(stock):
    ch3="oui"
    while True or ch3=="oui":
        mod=input("ecrivez le nom de l'element que vous voulez modifier?:")
        if nom(stock,mod)==-1:
            print("produit n est pas trouvé")
            ch3=input("vous voulez modifier une autre chose ? oui/non :")
            if ch3=="non":
                break
        else:
            return mod

def ask(stock,n):
    i=nom(stock,n)
    mod1=int(input("""Qu est ce que vous voulez modifier ?
                  (1) date d ajout du produit
                  (2) nom du produit
                  (3)contités restante du produit
                  (4) dat d'expiration du produit :"""))

    if mod1==1:
        a=input("nouvelle date d ajout :")
        stock[i][0]=a
    elif mod1==2:
        b=input("nouveau nom :")
        stock[i][1]=b
    elif mod1==3:
        c=input("nouvelles contité restante :")
        stock[i][2]=c
    elif mod1==4:
        d=input("nouvelle date d'expiration:")
        stock[i][3]=d

def modifier(stock):
    while True:
        n=saisir(stock)
        ask(stock,n)
        print(stock)
        ch3=input("vous voulez modifier une autre chose ? oui/non :")
        if ch3=="non":
            break


def stock1(stock):
    x=int(input(""""qu est ce que vous voulez faire:
            (1)ajout du stock
            (2)chercher
            (3)suprimer
            (4)modifier:"""))
    if x==1:
     ajouter(stock)
    elif x==2:
     chercher(stock)
    elif x==3:
        suprimer(stock)
    elif x==4:
        modifier(stock)

def crer_compte(liste_compter):
    choix="oui"
    while choix=="oui":
        mail=input("entre votre mail :")
        mdp=input("mot de passe :")
        mdp1=input("verifiez votre mot de passe:")
        while mdp1!=mdp:
            print("verfication de mot de passe non valide")
            mdp=input("entrer mot de passe:")
            mdp1=input("verifiez votre mot de passe ou inserer exit pour exiter :")
            if mdp1=="exit":
              return
        numero=int(input("votre numero:"))
        date_naissance=(input("date de naissance:"))
        region=input("region:")
        sex=input("homme/femme")
        client=(mail,mdp,numero,date_naissance,sex,region)
        liste_compter.append(client)
        
        print("votre compter a ete crer avec suceès")
        choix=input(" vous voulez ajouter un autre client ???oui/non\n")
def login():
    username=input("username :")
    mot_de_passe=input("mot de passe :")
    my_username="oussamamabrouk"
    mon_mot_de_passe="0000"
    i=3
    while i>0 and  ((username!=my_username) and (mot_de_passe!=mon_mot_de_passe)):
        username=input(" username")
        mot_de_passe=input("mot de passe :")
        i=i-1
    if (username==my_username) and (mot_de_passe==mon_mot_de_passe):
        return True

    else:
        return False
def gestion():
    print("""
          *-----------------------------------------------------------------*
          *                 ******LISTE DES MODULES*****                    *
          *                                                                 *
          *       1.gestion de commande                                     *
          *       2.gestion de client                                       *
          *       3.gestion de stock                                        *
          *                                                                 *
          *-----------------------------------------------------------------* """)

    reponse=input("Choisir un module :")
    while reponse not in ["1","2","3"] :
        reponse=input("Choix invalid \n Choisir un module :")
    if reponse=="1":
        print("Gestion de commande ")
        LC=[]
        gestion_de_commande(LC)
        gestion()
    elif reponse=="2":
        print("Gestion de client")
        liste_malades=[]
        liste_homme_femme=[]
        liste_enfant=[]
        client(liste_malades,liste_homme_femme,liste_enfant)
        gestion()
    elif reponse=="3":
        print("Gestion de stock")
        stock=[]
        stock1(stock)
        gestion()
    else:
        return

def menu():
    print("""                            --------------------------------------------
                                         *                                          *
                                         *                                          *
                                         *           ******bienvenue*****           *
                                         *                                          *
                                         *                                          *
                                         *------------------------------------------*                               """)
    choix_entre=input("Avez-vous un compte oui/non?")
    choix_entre=choix_entre.lower()
    if choix_entre=="oui":
        login()
    elif choix_entre=="non":
        nv_compte=input("voulez vous creer un nouveau compte? oui/non? ")
        if nv_compte=="oui":
            liste_compter=[]
            crer_compte(liste_compter)
        else:
            print("Exit application...")
            return
    else:
        print("Choix invalid...EXIT ")
        return
if __name__ == "__main__":
    menu()
    login_status=login()
    if login_status:
        gestion()
    else:
        print("Erreur login...\n Exist")