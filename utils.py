def get_population(country_dict):
    population_dict = {
        '2022': 300,
        '2023': 400
    }

    labels = population_dict.keys()
    values =  population_dict.keys()
    return labels,values

def population_by_country(data, country):
    result = list(filter(lambda x: x['country'] == country, data))
    return result

