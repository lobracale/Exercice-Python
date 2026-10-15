#Exercices Python : Listes, Variables & Conditions
"""
#Exercice 1 : Création, modification et accès direct
fruits = ['pomme', 'banane', 'orange']
fruits[1] = 'fraise'
print(fruits[0])
print(fruits[-1])
"""
"""
#Exercice 2 : Test d'appartenance avec condition
membres = ['Alice', 'Bob', 'Charlie']

nom = input("Entrez un nom : ")

if nom in membres:
    print("Présent")
else:
    print("Absent")
"""

"""
#Exercice 3 : Ajout conditionnel basé sur la taille
panier = ['Livre', 'Stylo']
if len(panier) < 3:
    article = input("Entrez un article : ")
    panier.append(article)
    print(panier)
else:
    print("Panier plein")
"""

"""
#Exercice 4 : Inversion et tri d'une liste
nombres = [42, 12, 89, 7, 23]

nombres.sort()
print(nombres)
nombres.reverse()
print(nombres)
"""

"""
#Exercice 5 : Calcul de moyenne tronquée
notes = [12, 5, 18, 15, 9]
notes.remove(min(notes))
notes.remove(max(notes))
moyenne = sum(notes) / len(notes)
print(notes)
print(moyenne)
"""

"""
#Exercice 6 : Extraction par slicing et assemblage
chiffres = [1, 2, 3, 4, 5, 6, 7, 8]

milieu = len(chiffres) // 2

nouvelle_liste = chiffres[milieu:] + chiffres[:milieu]

print(nouvelle_liste)
"""

"""
#Exercice 7 : Remplacement conditionnel du statut
serveur = ['Prod-01', 8080, 'ACTIF', 85]

if serveur[3] > 80:
    serveur[2] = 'ALERTE'

print(serveur)
"""

"""
#Exercice 8 : Suppression des doublons et tri
codes = [101, 202, 101, 303, 202, 404]

codes = list(set(codes))
codes.sort()

print(codes)
"""

"""
Exercice 9 : Rotation circulaire vers la droite
valeurs = ['A', 'B', 'C', 'D', 'E']

k = 2
k = k % len(valeurs)

nouvelle_liste = valeurs[-k:] + valeurs[:-k]

print(nouvelle_liste)
"""

"""
#Exercice 10 : Vérification d'un palindrome et comparaison des moitiés
sequence = [1, 2, 3, 3, 2, 1]

milieu = len(sequence) // 2

if sequence == sequence[::-1]:
    print("La séquence est un palindrome")
else:
    print("La séquence n'est pas un palindrome")

if sequence[:milieu] == sequence[milieu:]:
    print("Les deux moitiés sont identiques")
else:
    print("Les deux moitiés sont différentes")
"""