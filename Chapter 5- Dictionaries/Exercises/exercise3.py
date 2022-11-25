#Exercise No:3
glossary = {
    'string': 'A series of characters.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'value': 'An item associated with a key in a dictionary.',
    'dictionary': "A collection of key-value pairs.",
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)