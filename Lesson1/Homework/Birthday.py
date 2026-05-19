# Birthday Card Generator

recipient_name = input("Enter the recipient's name: ")
year_of_birth = input("Enter the recipient's year of birth: ")
personal_message = input("Enter a short personalized message: ")
sender_name = input("Enter your name: ")

year_of_birth = int(year_of_birth)

current_year = 2026
age = current_year - year_of_birth
print()
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!")
print()
print(personal_message)
print()
print("With love and best wishes,")
print(sender_name)