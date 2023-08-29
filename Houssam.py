#tirage au sort d'un prix compris entre 1 et 10 (comprs)
import random
cible = random.randint(1,10)
essai = None
for i in range (1,6):
    #choix du joueur
    try:
        essai= int(input(f"essai n){i} - prix?"))
    except:
        print("valeur incorrecte")
        continue #redémarre à l'itération suivante

    #Message "Bravo" si le prix a été trouvé
    if cible == essai:
        print("bravo!!!")
        break
    #Message "Pas assez" si le prix est trop bas
    elif cible > essai :
        print("pas assez")
    #Message "trop elevé" si le prix est trop haut
    else:
        print("trop elevé")
    #Message "perdu" au bout de 5 essais

    if (cible!= essai):
        print("perdu")
#fin au bout de 5 essais ou si le prix est trouvé
