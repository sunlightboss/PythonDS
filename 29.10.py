# x = int(input("Enter a number - "))
# if x % 2 == 0:
#     print(f"{x} - Chetnoe")
# else:
#     print(f"{x} - Nechetnoe")

# Logic problems

def positive():
    x = int(input("Enter a number - "))
    if x > 0:
        print("Positive")
    elif x == 0:
        print("You've entered zero")
    else:
        print("Negative")

def odd_notodd():
    x = int(input("Enter a number - "))
    if x % 2 == 0:
        print(f"{x} - Chetnoe")
    else:
        print(f"{x} - Nechetnoe")

def inequality():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))

    true_1st = a > 2
    true_2nd = b <= 3

    if true_1st and true_2nd:
        print("Propper inequality")
    else:
        print("Wrong")

def triple():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))
    c = int(input("Enter 3rd number - "))

    is_true = a < b < c
    if is_true:
        print("Correct")
    else:
        print("Wrong")

def ineq():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))
    c = int(input("Enter 3rd number - "))

    is_true = a > b and c > b
    if is_true:
        print("B is in between")
    else:
        print("Wrong")

def double_odd():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))

    is_true = a % 2 == 0 and b % 2 == 0
    if is_true:
        print("Chetnoe")
    else:
        print("Nechetnoe")

def or_odd():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))

    is_true = a % 2 != 0 or b % 2 != 0
    if is_true:
        print("Nechetnoe")
    else:
        print("Chetnoe")

def only1_odd():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))

    is_true1 = a % 2 != 0
    is_true2 = b % 2 != 0
    if is_true1 + is_true2 > 1:
        print("Oba nechetnye")
    elif is_true2 + is_true1 == 1:
        print("Odin nechetnyi")
    else:
        print("Oba chetnye")


def both_odd():
    a = int(input("Enter 1st number - "))
    b = int(input("Enter 2nd number - "))

    is_true1 = a % 2 == 0
    is_true2 = b % 2 == 0

    if is_true1 and is_true2:
        print("same chetnost")
    elif not is_true2 and not is_true2:
        print("same chetnost")
    else:
        print("Not same")


# word = "milk"
# list1 = ['apple', 'banana', 'milk']
# if word in list1:
#     new_word = word.replace('k', 'c')
#     print(new_word)

a = 32
b  = 3.5
x = True

a = str(a)
b = str(b)
x = str(x)
print([a,b,x])

    