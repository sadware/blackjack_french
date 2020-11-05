import random as r
import time
pioche = [2,3,4,5,6,7,8,9,10,"valet","reine","roi","as"]*4
global somme_joueur
global d 
global x
global valtc
d = {}
somme_joueur = {}
x = 1
valtc = 0


def as_valeur(c1):
  while 1 == 1:
    if c1 == "as":
      valeur_as = input("Quelle valeur souhaitez-vous que votre as ait ? (1 ou 11)\n> ")
      if "11" in valeur_as:
        c1 = 11
        break
      elif "1" in valeur_as:
        c1 = 1
        break
      else:
        print("Vous n'avez pas entré une valeur valide")
  return c1
   



def decoration():
  print("______ _            _    _            _  ")
  print("| ___ \ |          | |  (_)          | |  ")
  print("| |_/ / | __ _  ___| | ___  __ _  ___| | _")
  print("| ___ \ |/ _` |/ __| |/ / |/ _` |/ __| |/ /")
  print("| |_/ / | (_| | (__|   <| | (_| | (__|   < ")
  print("\____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\")
  print("                       _/ |                ")
  print("                      |__/                 ")

def cartes_joueur(x):
  premiere_carte = pioche[r.randint(0,12)]
  deuxieme_carte = pioche[r.randint(0,12)]
  print("\n==================================")
  print("==================================\n")
  print("Les cartes de joueur " +  str(x) + " sont " + str(premiere_carte)+" et " +  str(deuxieme_carte))
  val1 = 0
  val2 = 0
  if premiere_carte == "as":
    print("Il semble que la première carte que vous avez pioché est un as, veuillez choisir sa valeur")
    
    premiere_carte = as_valeur(premiere_carte)
  if deuxieme_carte == "as":
    print("Il semble que la deuxième carte que vous avez pioché est un as, veuillez choisir sa valeur")
    
    deuxieme_carte = as_valeur(deuxieme_carte)
  
  val1 = premiere_carte
  val2 = deuxieme_carte
  
  if premiere_carte == "valet" or premiere_carte == "reine" or premiere_carte == "roi":
    val1 = 10
  if deuxieme_carte == "valet" or deuxieme_carte == "reine" or deuxieme_carte == "roi":
    val2 = 10
  
  
  valt = val1 + val2
  if valt == 21:
    print("Blackjack ! Vous gagnez 2.5x la somme misée")
    somme_joueur[x] = 2.5*somme_joueur[x]

  print("\nLa valeur des cartes de joueur " + str(x) + " est : " + str(valt) + "\n")
  time.sleep(2)
  while valt < 21:
    piocher = input("\nJoueur " + str(x) + " souhaitez vous piocher une carte ? (O/N)\n> ").lower()
    valn = 0
    if "o" in piocher:
      nouvelle_carte = pioche[r.randint(0,12)]
      valn = nouvelle_carte
      print("La carte que vous venez de tirer est : " + str(nouvelle_carte))
      if nouvelle_carte == "valet" or nouvelle_carte == "reine" or nouvelle_carte == "roi":
        valn = 10
      elif nouvelle_carte == "as":
        print("Il semble que la nouvelle carte que vous avez pioché est un as, veuillez choisir sa valeur")
    
        valn = as_valeur(nouvelle_carte)
      
        
    elif "oui" in piocher:
      nouvelle_carte = pioche[r.randint(0,12)]
      valn = nouvelle_carte
      print("La carte que vous venez de tirer est : " + str(nouvelle_carte))
      if nouvelle_carte == "valet" or nouvelle_carte == "reine" or nouvelle_carte == "roi":
        valn = 10
      elif nouvelle_carte == "as":
        print("Il semble que la nouvelle carte que vous avez pioché est un as, veuillez choisir sa valeur")
    
        valn = as_valeur(nouvelle_carte)
      
      
    elif "n" in piocher:
      break
    elif "non" in piocher:
      break
    else:
      print("Vous n'avez pas indiqué quelle option vous souhaitez prendre...")
    valt = valt + valn
    print("La nouvelle valeur de vos carte est : " + str(valt))
  if valt > 21:
    print("Vous avez perdu !")
  else:
    print("\nVous allez devoir attendre que le croupier joue pour savoir si vous allez perdre ou gagner !\n")
  return valt





def cartes_croupier():
  carte1 = pioche[r.randint(0,12)]
  carte2 = pioche[r.randint(0,12)]
  print("\n==================================")
  print("==================================\n")
  print("Les cartes du croupier sont " + "(face cachée) et " + str(carte2))
  
  valc1 = carte1
  valc2 = carte2
  if carte1 == "valet" or carte1 == "reine" or carte1 == "roi":
    valc1 = 10
  if carte2 == "valet" or carte2 == "reine" or carte2 == "roi":
    valc2 = 10
  if carte1 == "as":
    valc1 = 11
  if carte2 == "as":
    if valc1 == 11:
      valc2 = 1
    else:
      valc2 = 11
  
  valtc = valc1 + valc2
  return valtc



def pioche_croupier(c3):
  print("\n\nLa valeur des cartes du croupier est : " + str(c3))
  valc3 = 0
  while c3 < 21:
    
    if c3 <= 16:
      carte3 = pioche[r.randint(0,12)]
      print("\n\nLe croupier pioche la carte " + str(carte3))
      valc3 = carte3
      if carte3 == "valet" or carte3 == "reine" or carte3 == "roi":
        valc3 = 10
      elif carte3 == "as" :
        if c3 > 11:
          valc3 = 1
        else:
          valc3 = 11
      
    else:
      print("\n\nLe croupier ne pioche pas de carte")
      break
    c3 = c3 + valc3
    print("La nouvelle valeur des cartes du croupier est " + str(c3))
    
  return c3

  


def comparaison_cartes(var, c4):
  i = 1
  while i < (var+1):
    if d[i] < 22:
      #si joueur <= 21
      if (c4 > 21) or (d[i] > c4):
        #si croupier > 21 ou croupier < joueur
        print("Bravo Joueur " + str(i) + ", tu gagnes !")
        somme_joueur[i] = 2*somme_joueur[i]
      elif c4 == d[i]:
        # si croupier = joueur
        print("Pas de victoire ni de défaite pour toi Joueur " + str(i) + " !") 
      else: 
        # si croupier <=21 et croupier > joueur
        print("Dommage Joueur " + str(i) + ", tu as perdu...")
        somme_joueur[i] = 0
    else:
      print("Dommage Joueur " + str(i) + ", tu as perdu...")
      somme_joueur[i] = 0
    i += 1
