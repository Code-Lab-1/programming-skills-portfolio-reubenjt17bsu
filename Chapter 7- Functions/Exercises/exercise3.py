#Exercise No:3
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')

make_shirt('Extra large', 'I love You Forever!')
make_shirt(message="Readability counts.", size='Large')