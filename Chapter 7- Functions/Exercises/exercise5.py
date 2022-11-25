#Exercise No:5
def describe_city(city, country='California'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('San Diego')
describe_city('Kulsevyk', 'San Francisco')
describe_city('Alcatraz Island')