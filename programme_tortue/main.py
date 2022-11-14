import turtle

t = turtle.Turtle()  # CREER L'OBJET


def escalier(taille, nb, size_rotate):

    for i in range(0, nb):

        t.forward(taille)
        t.left(size_rotate)
        t.forward(taille)
        t.right(size_rotate)

    t.forward(taille)

# escalier(30, 5, 90)


def carre(size, nb, rotate):

    for i in range(0, nb):

        t.forward(size)
        t.left(rotate)
    size -= 10


def multi_carre(size, nb):

    for i in range(0, nb):

        carre(size, 4, 90)
        size += 10


multi_carre(5, 10)
escalier(60, 10, 90)


turtle.done()  # GARDER FENETRE OUVERTE
