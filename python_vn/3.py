import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+9423147698")

print("\n phone numbers location is :")

print(geocoder.description_for_number(phone_number1, "en"))
