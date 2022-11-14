# DEFINITION FONCTIONS : 


def afficher(name, age):
    
    if age >= 60 :

        print("Bonjour " + name + " Vous êtes Sénior ! Vous avez " + str(age) + " ans.")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans." +'\n')


    elif age >= 21 and age < 59 : 

        print("Bonjour " + name + " Vous êtes un Adulte ! Vous avez " + str(age) + " ans.")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

    elif age >= 18 and age <= 21:

        print("Bonjour " + name + " Vous êtes Majeur depuis peu de temps ! Vous avez " + str(age) + " ans. ")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

    elif age <= 17 and age >= 12:

        print("Bonjour " + name + " Vous êtes un Adolescent ! Vous avez " + str(age) + " ans.")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

    elif age <= 11  and age >= 5 :

        print("Bonjour " + name + " Vous êtes un Enfant ! Vous avez " + str(age) + " ans.")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

    elif age == 1 or age < 4 :

        print("Bonjour " + name + " Vous êtes un Bébé !" + " Vous avez " + str(age) + " ans !" )
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")

    else :
        print("Bonjour " + name + " vous avez " + str(age) + " ans. Vous n'êtes pas Humain !")
        print("L'année prochaine vous aurez " + str(age + 1) + " ans.")


def demander_nom():

    name_str = ""
    while name_str == "":
        
        name_str = input('Quel est votre nom ? ')
    return name_str 


def demander_age(name):

    age_int = 0
    while age_int == 0:
        try:
            age_int = int(input('Quel est votre age ' + name + ' ? '))

        except ValueError:
            print("Erreur: Vous devez entrer un nombre pour l'age")
    return age_int





# CODE PRINCIPAL

# name1 = demander_nom()
# print('\n')

# name2 = demander_nom()
# print('\n')

# age1 = demander_age(name1)
# print('\n')

# age2 = demander_age(name2)
# print('\n')


# afficher(name1, age1)
# print('\n')

# afficher(name2, age2)
# print('\n')

# FIN APPEL


# BOUCLE FOR 

NOMBRE_PERSONNE = 3

for i in range(0, NOMBRE_PERSONNE) :
    
    name = "Personne " + str(i + 1)
    age = demander_age(name)
    afficher(name, age)
