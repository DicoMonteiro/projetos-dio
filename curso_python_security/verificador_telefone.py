import phonenumbers

from phonenumbers import geocoder


phone = input('Digite o telefone no formato: +551140029822: ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

