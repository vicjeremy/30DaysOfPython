# Day 5: 30 Days of python programming

# Exercises: Level 1
a = [] # 1.

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # 2.

print(len(b)) # 3.

print(b[0], b[len(b)//2], b[-1]) # 4.

mixed_data_types = ['jeremy', 23, 1.67, 'single', 'Indonesia'] # 5.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'] # 6.

print(it_companies) # 7.

print(len(it_companies)) # 8.

print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1]) # 9.

it_companies[0] = 'Twitter' # 10.
print(it_companies)

it_companies.append('Netflix') # 11.
print(it_companies)

it_companies.insert(len(it_companies)//2, 'Tokopedia') # 12.
print(it_companies)

it_companies[2] = it_companies[2].upper() # 13.
print(it_companies)

combine = '#; '.join(it_companies) # 14.
print(combine)

print('Tokopedia' in it_companies) # 15.
print('Stockbit' in it_companies)

it_companies.sort()
print(it_companies) # 16.

it_companies.reverse()
print(it_companies) # 17.

print(it_companies[0:3]) # 18.

print(it_companies[-3:]) # 19.

print(it_companies[len(it_companies)//2]) # 20.

print(it_companies)
del it_companies[0]
print(it_companies) # 21.

del it_companies[len(it_companies)//2]
print(it_companies) # 22. 

del it_companies[-1]
print(it_companies) # 23.

it_companies.clear()# 24.

del it_companies # 25.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end # 26.
print(full_stack) 

full_stack.insert(5, 'Python') # 27.
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort() # sorting the list
min_ages = min(ages) # finding the minimum value
max_ages = max(ages) # finding the maximum value
print(min_ages, max_ages)

ages.append(min_ages) # adding the minimum value to the list
ages.append(max_ages) # adding the maximum value to the list
print(ages)

print(len(ages)) # finding the length of the list
median_ages = (ages[len(ages)//2] + ages[len(ages)//2 + 1]) / 2 # finding the median value
print(median_ages)

average_ages = sum(ages) / len(ages) # finding the average value
print(average_ages)

print(max_ages - min_ages) # finding the range of the ages

print(abs(min_ages - average_ages), abs(max_ages - average_ages)) # finding the absolute difference between the minimum and maximum values and the average value

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

print(countries[len(countries)//2]) # finding the middle value of the list

countries_first = countries[0:len(countries)//2] # finding the first half of the list
print(len(countries_first))

countries_second = countries[len(countries)//2:] # finding the second half of the list
print(len(countries_second))

scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru, us, *scandic = scandic_countries # unpacking the list
print(ch, ru, us, scandic)










