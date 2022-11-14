import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIK = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIE = 4

vie = NOMBRE_VIE


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0 :
        print(f'Vous avez {vie} vie !')
        nombre_str = input(f"Quel est le nombre magique entre {nb_min} et {nb_max} ? ")

        try:    
            nombre_int = int(nombre_str)
        except ValueError: 
            print("Erreur: Vous ne pouvez pas utiliser d'autre caractères que des chiffres !")
        else: 
            if nombre_int > nb_max or nombre_int < nb_min:
                print(f'Veuillez entrer un nombre compris entre {nb_min} et {nb_max} !')
                nombre_int = 0
    return nombre_int


gagner = False

for i in range(0, NOMBRE_VIE): 

    vie = NOMBRE_VIE - i
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)

    if nombre == NOMBRE_MAGIK:
        print('Bravo le nombre Magik était bien ' + str(NOMBRE_MAGIK) + " !")
        gagner = True
        break

    elif nombre > NOMBRE_MAGIK:
        print('Le nombre Magik est plus petit..')
         
    else:
        print('Le nombre Magik est plus grand...')
    
if not gagner : 
    print(f'Il vous reste {vie} vies ... Vous avez perdu ! Le Nombre Magik était {NOMBRE_MAGIK} !')
       

