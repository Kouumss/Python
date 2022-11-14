import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_QUESTION = 4


def poser_question():

    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0,1)
    # 0 -> +
    # 1 -> *
    operateur_str = "+"
    if o == 1:
         operateur_str = "*"
    reponse_str = input(f'Calculez {a} {operateur_str} {b} = ')
    reponse_int = int(reponse_str)
    # if reponse_int == a+b:
    #     print('Réponse correcte !')
    #     reponse_int = True
    # else:
    #     print('Réponse Incorrecte !')
    # return reponse_int
    if reponse_int == a+b or reponse_int == a*b:
        return True
    return False


nb_points = 0
moyenne = int(NOMBRE_QUESTION/2)

for i in range(0, NOMBRE_QUESTION):

    print(f'Question n°{i + 1} sur {NOMBRE_QUESTION}\n')
    # answer = poser_question()
    # if answer == True :
    #     nb_points += 1
    if poser_question():
        nb_points += 1

    print()

print(f'Votre score est : {nb_points} / {NOMBRE_QUESTION} !')

if nb_points == NOMBRE_QUESTION:
    print('Excellent !')

elif nb_points == 0:
    print('Réviser vos Maths !')

else:
    if nb_points >= moyenne:
        print('Pas mal!')
    else:
        print('Peut mieux faire !')
