import phonenumbers
from phonenumbers import carrier, timezone, geocoder

print("Enter The your phone number with country code: ")
num = input()
Phone_num = phonenumbers.parse(num)

# get timezone your number
print(timezone.time_zones_for_number(Phone_num))

# getting carrier of a phone number 
print(carrier.name_for_number(Phone_num, 'en'))

# getting region informations
print(geocoder.description_for_number(Phone_num, 'en'))

# checking validating of a phone number
print("Valid Mobile Number: ",phonenumbers.is_valid_number(Phone_num))

# checking possibility of a phone number
print("Checking possibility of Numbers: ", phonenumbers.is_possible_number(Phone_num))
