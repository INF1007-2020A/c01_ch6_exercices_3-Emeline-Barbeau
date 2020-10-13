#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.

    if data is None : # Demander les valeurs ici
        data = [input("Entrez une valeur : ") for _ in range(10)]

    reversed_data = Stack()
    reversed_data.put_many(data)  # Stocker le résultat ici

    return [reversed_data.get() for _ in range(10)]  # Poper les valeurs pour les avoir dans le sens inverse


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.

    temp = [data.get() for _ in range(len(data) - position - 1)]  # -1 car une valeur ne doit pas être mise dans la liste temporaire
    data.get()

    temp.reverse() 
    data.put_many(temp)

    return data


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
   
    size_queue = len(data)

    temp = [data.get() for _ in range(position)]
    data.put_many(temp)

    data.get()
    
    temp = [data.get() for _ in range(size_queue - position - 1)]  # -1 car une valeur ne doit pas être mise dans la liste temporaire
    data.put_many(temp)

    return data


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée

    temp = [data.get() for _ in range(len(data))]
    temp.sort()
    data.put_many(temp)

    return data


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    temp = [data.get() for _ in range(len(data))]
    temp.sort()
    data.put_many(temp)

    return data


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.

    fifo, lifo = Queue(), Stack()

    for char in string :
        if ('a' <= char) and (char <= 'z') or ('A' <= char) and (char <= 'Z') :  # Minuscule ou majuscule
            fifo.put(char)

        else :
            lifo.put(fifo.get())

    return fifo, lifo


def main() -> None:
    print("On inverse des données...")
    print(f"Résultat: {reverse_data()}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_stack(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(fifo)}")

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
