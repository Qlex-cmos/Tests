#coding:utf-8

# Gérer les exceptions: try/except (+ else, finally)

#ageUtilisateur = input("Quel âge as-tu? ")

#try:
    #ageUtilisateur = int(ageUtilisateur)
#except:
    #print("L'âge indiqué est incorrect")
#else:
    #print("Tu as", ageUtilisateur, "ans")
#finally:
    #print("Fin du programme")


# Type d'exceptions :
# ValueError
# NameError
# TypeError
# ZeroDivisionError
# OSError
# AssertionError


nombre1 = 150

nombre2 = input("Choisir le nombre pour diviser: ")

try:
    nombre2 = int(nombre2)
    print("Résultat = {}".format(nombre1 / nombre2))
# Except permet de capturer l'exception
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par zéro")
except ValueError:
    print("Vous devez entrer un nombre")
except:
    print("Valeur incorrecte")
else:
    print("Bravo, tu as entré une valeur correcte")
finally:
    print("Fin du programme")

# Faire une levée d'exception manuelle, pour créer son propre type d'exception
try:
    age = int(input("Quel âge as-tu? "))
    if age < 25:
        raise ValueError

except ValueError:
    print("J'ai attrapé ton exception")

try:
    age = int(input("Quel âge as-tu? "))

    assert age > 25 # -> 'Je veux que âge soit plus grand que 25'
except AssertionError:
    print("J'ai attrapé l'exception!!!")














