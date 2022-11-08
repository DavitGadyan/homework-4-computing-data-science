
##############

# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

data = {'Spain': [4, 8, 2, 0, 1],
        'France': [2, 3, 6],
        'Italy': [6, 8, 1, 7]
}


# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country
def total_registered_cases(country_name: str, data: dict) -> int:
    ''' Total registered cases

        Args:
            country_name (str): name of the country
            data (dict): dictionary key value pairs country and registered covid cases
        Returns:
            total_covid_cases (int): total number of covid cases
    '''
    if country_name in data.keys():
        total_covid_cases = sum(data[country_name])
        return total_covid_cases
    else:
        raise KeyError(f'{country_name} country not in data!!!')

# testing
# print(f'Number of total cases: ', total_registered_cases('Spain', data=data))

# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#
def total_registered_cases_per_country(data: dict) -> dict:
    '''Total registered cases per country

    Args:
        data (dict): dictionary key value pairs country and registered covid cases
    Returns:
        total_cases_data (dict): dictionary with a key per each country and total number of cases
    '''
    # define empty total_cases_data 
    total_cases_data = {}

    # per DRY priniciple I will use previous function to calculate for each country
    for k, v in data.items():
        total_cases_data[k] = total_registered_cases(country_name=k, data=data)
    
    return total_cases_data

# testing
# print('Total case dict: ', total_registered_cases_per_country(data))

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data: dict) -> dict:
    '''Highest Covid case country

    Args:
        data (dict): dictionary key value pairs country and registered covid cases
    Returns:
        highest_case_country (str): country with the greatest total amount of cases
    '''
    # per DRY calculate total_cases_data
    total_cases_data = total_registered_cases_per_country(data)

    highest_case_country = max(total_cases_data, key=total_cases_data.get)

    return highest_case_country

# testing
# print('Highest Covid case countryt: ', country_with_most_cases(data))