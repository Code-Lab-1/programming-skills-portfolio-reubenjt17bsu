#Exercise No:5
sandwich_orders = [
    'Pastrami', 'Ham and Cheese', 'Grilled cheese', 'Pastrami',
    'Baconator', 'Roast beef with onions', 'Pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of Pastrami today.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")