pets = []
pet = {
    'animal type': 'Hamster',
    'name': 'Johnson',
    'owner': 'Sky',
    'weight': 2,
    'eats': 'Peanuts',
}
pets.append(pet)

pet = {
    'animal type': 'Dog',
    'name': 'Roxi',
    'owner': 'Sunu',
    'weight': 28,
    'eats': 'Dog Food',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'Whiskers',
    'owner': 'Sheru',
    'weight': 15,
    'eats': 'Cat Food',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))