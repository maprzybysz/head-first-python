import pprint 

people = {}
people['Ford'] = {
    'Nazwisko': 'Ford Prefect',
    'Plec': 'mężczyzna', 
    'Zawoód': 'badacz',
    'Planeta macierzysta': 'Betelgeza Siedem'
}

people['Arthur'] = { 'Nazwisko': 'Arthur Dent',
'Płeć': 'mężczyzna',
'Zawód': 'pan kanapka',
'Planeta macierzysta': 'Ziemia' }

people['Trillian'] = { 'Nazwisko': 'Tricia McMillan',
'Płeć': 'kobieta',
'Zawód': 'matematyczka',
'Planeta macierzysta': 'Ziemia' }

people['Robot'] = { 'Nazwisko': 'Marvin',
'Płeć': 'nieznana',
'Zawód': 'paranoiczny android',
'Planeta macierzysta': 'nieznana' }

pprint.pprint(people)

print(people['Arthur']['Zawód'])