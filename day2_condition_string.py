# Day 2: Conditional Logic

temperature = 35
if temperature > 40:
    print("It's a hot day.")
elif temperature < 20:
    print("It's a cold day.")
else:
    print("Weather is pleasant.")

age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("Sorry, you must be at least 18.")




# Age Group Detector

age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 60:
    print("You are an Adult.")
else:
    print("You are a Senior Citizen.")



    # String Methods

name = "   Shailendra   "
print(name.strip())  # "Shailendra"

email = "Captain@Gmail.COM"
print(email.lower())  # "captain@gmail.com"

text = "Python is fun"
print("fun" in text)  # True




# Name + Age Cleaner

name = input("Enter your name: ")
age = int(input("Enter your age: "))

clean_name = name.strip().title()

if age < 18:
    print(f"Sorry {clean_name}, you’re underage.")
else:
    print(f"Welcome, {clean_name}!")



# Gmail Validator

full_name = input("Enter your full name: ")
email = input("Enter your email: ")
message = input("Enter your message: ")

full_name = full_name.strip().title()
email = email.strip().lower()
message = message.strip()

if email.endswith("@gmail.com"):
    print("✅ Valid Gmail")
else:
    print("❌ Invalid email domain")

print(f"Name: {full_name}")
print(f"Email: {email}")
print(f"Message: {message}")

