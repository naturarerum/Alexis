from random import randrange


def main():
    # un nombre choisi au hasard est place dans la variable secret_number
    nombre_secret = randrange(1, 12)
    print(nombre_secret )

    # demander a l'utilisateur de deviner le nombre secret
    print("devine le nombre : ")
    nombre_devine = int(input())

    # si la reponse de l'utilisateur  = le chiffre choisi par l'ordinateur  on affiche que c'est une bonne réponse
    while nombre_devine != nombre_secret:
        print("devine le nombre : ")
        nombre_devine = int(input())
    if nombre_devine == nombre_secret:
        print("Bravo")
        quit() # et on quitte le programme


# ces dux lignes servent a executer le programme
if __name__ == '__main__':
    main()