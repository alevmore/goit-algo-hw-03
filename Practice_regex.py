import re

raw_numbers = ["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]

def normalize_phone(phone_number):
    pattern = r"[\d\+]+"
    phone_number = ''.join(re.findall(pattern, phone_number))
    if len(phone_number) ==10:
        phone_number = '+38'+phone_number
    elif len(phone_number) ==12:
        phone_number = '+'+phone_number
    return phone_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS sending:", sanitized_numbers)
     
