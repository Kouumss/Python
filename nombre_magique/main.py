import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIK = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NOMBRE_VIE = 4

vie = NOMBRE_VIE

def demander_nombre(nb_min, nb_max, chance):

    nombre_int = 0
    while nombre_int == 0 :
        print(f'Vous avez {chance} vie !')
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



nombre = 0
while not nombre == NOMBRE_MAGIK and vie > 0: 

    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX, vie)

  
    if nombre == NOMBRE_MAGIK:
        print('Bravo le nombre Magik était bien ' + str(NOMBRE_MAGIK) + " !")
    
    elif nombre > NOMBRE_MAGIK:
        print('Le nombre Magik est plus petit..')
        vie -= 1

    else:
        print('Le nombre Magik est plus grand...')
        vie -= 1

if vie == 0:
    print(f'Il vous reste {vie} vies ... Vous avez perdu ! Le Nombre Magik était {NOMBRE_MAGIK} !')

#   if nombre >= NOMBRE_MIN and nombre <= NOMBRE_MAX:
