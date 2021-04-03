with open('animals.txt', 'r') as animals, \
        open('animals_new.txt', 'w') as animals_new:
    animals_new.write(' '.join(animals.read().split('\n')))

animals.close()
animals_new.close()
