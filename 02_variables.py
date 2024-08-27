# Day 2:30 Days of python programming

first_name = "Antonio"
last_name = "Bermudez"
full_name = "Antonio Bermudez"
country = "Spain"
city = "Malaga"
age = 32
year = 2024
is_married = False
is_true = True
is_light_on = True
cats = ["Runa", "Yuki", "Bruce"]
personal_info = {
    'firstname' : 'Antonio',
    'lastname' : 'Bermudez',
    'country' : 'Spain',
    'city' : 'Malaga',
}

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(cats))
print(type(personal_info))

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Person information: ', personal_info)

radius = int(input('Dime el radio: '))
pi = 3.14159
area_circle = pi * (radius * radius)
circum_cicle = 2*pi*radius

print('Area mide: ', area_circle)
print('Circunferencia mide: ', circum_cicle)