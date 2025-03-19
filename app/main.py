import utils



# Obtener las claves y valores de la población desde utils
try:
    keys, values = utils.get_population()
    if not (isinstance(keys, list) and isinstance(values, list)):
        raise ValueError("get_population() debe retornar dos listas.")
    print("Keys:", keys)
    print("Values:", values)
except AttributeError:
    print("Error: La función get_population() no existe en utils.")
    keys, values = [], []

# Lista de países y sus poblaciones
data = [
    {'name': 'Peru', 'population': 300},
    {'name': 'Brazil', 'population': 4000},
    {'name': 'Argentina', 'population': 400},
    {'name': 'Chile', 'population': 100},
    {'name': 'Colombia', 'population': 500},
    {'name': 'Venezuela', 'population': 200}
]

# Solicitar un país al usuario
country_name = input('Enter a country: ').strip().capitalize()

# Buscar el país en la lista de datos
try:
    result = utils.get_country(data, country_name)
    if result:
        print("Country found:", result)
    else:
        print("Country not found.")
except AttributeError:
    print("Error: La función get_country() no existe en utils.")

if __name__ == '__main__':
    run()