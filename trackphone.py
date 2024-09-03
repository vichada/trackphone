from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("phonenumber")
phone_number2 = phonenumbers.parse("phonenumber")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"de"))
print(geocoder.description_for_number(phone_number2,"de"))

# LETS TRACK PHONE NUMBERS
