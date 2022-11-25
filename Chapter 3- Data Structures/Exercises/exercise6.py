#Exercise No:6
guests = ['Robert Downey Jr', 'Lionel Messi', 'Olajide Olatunji(KSI)']

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print("\nSorry, " + name + " can't make it to dinner.")

del(guests[2])
guests.insert(2, 'Dwayne Johnson')

name = guests[0].title()
print("\n" + name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

del(guests[1])

print(guests)