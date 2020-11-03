from functions import *
import time
mise = 0
will = ""
valtc = 0

def blackjack():
  decoration()
  
  nbr_Joueurs = int(input("\nCombien de joueurs y a-t-il autour de la table ? (le croupier ne compte pas)\n> "))
  x = 1
  while x != nbr_Joueurs + 1:
    mise = int(input("Quelle somme souhaitez-vous miser Joueur " + str(x) + "?\n> "))
    somme_joueur[x] = mise
    x += 1

  print("Le jeu commence . . .")
  print("\n\nLe croupier tire ses cartes")
  
  valtc = cartes_croupier()
  time.sleep(2)
  print("\nLe croupier distribue les cartes des joueurs et les laisse piocher s'ils le souhaitent.")
  x = 1 
  while x < (nbr_Joueurs + 1):
    valt = 0
    d[(x)] = 0
    valt = cartes_joueur(x)
    d[x] = valt
    time.sleep(3)
    x += 1
   
  
  
  print("\nTous les joueurs ont pu tirer leurs cartes, le croupier va maintenant tirer les siennes.\n")
  print("==================================")
  print("==================================")
  time.sleep(2)
  
  print("\nLes règles pour le tirage du croupier sont les suivantes :\n> Il tire a 16 et s'arrête à 17")
  time.sleep(2)
  valtc = pioche_croupier(valtc)
  if valtc <= 21:
    print("\nMaintenant que le croupier a tiré ses cartes, nous allons les comparer aux votres dans le but de déterminer qui remportera la somme misée\n")
    time.sleep(3)
    somme_joueur[x] = comparaison_cartes(nbr_Joueurs, valtc)
  else:
    print("\n\nLe croupier a dépassé 21, il a donc perdu par définition. Cependant, la somme misée par les joueurs ayant déjà perdu ne peut être récupérée.")
    time.sleep(3)
    somme_joueur[x] = comparaison_cartes(nbr_Joueurs, valtc)
  print("Voici donc la somme d'argent restant de chaque joueur")
  x = 1
  while x != nbr_Joueurs + 1:
    print("Joueur " + str(x) + " : " + str(somme_joueur[x]))
    x += 1


def play():
  while 1 == 1:
    will = input("Souhaitez vous commencer une partie de blackjack ? (o/n)\n> ").lower()
    if "o" in will:
      blackjack()
      break
    elif "n" in will:
      print("D'accord, passez une bonne journée.")
      break
    else:
      print(str(will) + " n'est pas une réponse valide. Veuillez indiquer une réponse valide")

play()
