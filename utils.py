def get_population(country_dict):
    population = {
        'China': 1403500365,

    }
    keys = ['country', 'population']
    values = [300, 400]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda x: x['country'] == country, data))
    return result