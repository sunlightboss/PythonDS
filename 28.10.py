person = ["Bill", "Nurs", "Ali"]

age = (input("What's your age - "))
try:
    age = int(age)
except ValueError:
    print("Huy")
else:
    if age < 18:
        print("Shket")
    elif age >= 18 and age <=35:
        print("Normis")
    elif age > 35 and age < 65:
        print("Skuf")
    else:
        print("Bro na pensii")


