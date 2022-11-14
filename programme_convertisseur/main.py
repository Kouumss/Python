POUCES = 0.394
CM = 2.54
choix = 0
mesure1 = 'CM'
mesure2 = 'POUCE'
leave = False

def demander_convertir():
    global leave
    global choix
    choix_mesure_str = input(
        '1 : [CM => POUCE] or 2 : [POUCE => CM] ** Quitter = 3**')
    choix_mesure_int = int(choix_mesure_str)

    if choix_mesure_int == 1:
        choix = 1
    elif choix_mesure_int == 2:
        choix = 2
    elif choix_mesure_int == 3:
        choix = 3
  

    if choix == 1:
        valeur_str = input(
            f'Entrez la valeur en {mesure1} à convertir en {mesure2}: ')
        valeur_int = int(float(valeur_str))
        valeur_int *= POUCES
        print(f'{valeur_str} {mesure1} équivaut à {valeur_int} {mesure2}')
    elif choix == 3:
        leave = True
        print('GoodBye')
        return leave
    else:
        valeur_str = input(
            f'Entrez la valeur en {mesure2} à convertir en {mesure1} : ')
        valeur_int = int(float(valeur_str))
        valeur_int *= CM
        print(f'{valeur_str} {mesure2} équivaut à {valeur_int} {mesure1}')
    return choix_mesure_int


while leave == False:
    choix_mesure = demander_convertir()
