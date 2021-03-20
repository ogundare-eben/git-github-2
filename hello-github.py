#Writing a form filling automated script - customer database - integrate with SQL Db.
first_name = input("First Name: ")
last_name = input("Last Name: ")
message = """Thank you for taking time to fill this form with us. 'Your data privacy our concern...'"""

print(f"Hello {last_name.title()},\n\t{message}\n")

sex = input("Sex: )
age = int(input("Age: "))

country = input("Country: ")

if len(country) <= 3:
    print("No abbrev is allow. Please type country in full")
    re_type = input('Country: ')
    if len(re_type) <= 3:
        print("\t\t...We hereby cancel your registration! Goodluck!!!")

print("End")
