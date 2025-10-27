import math as mt

numbers = [1,2,3,4,5,6]
people = ["Tom", "Sam", "Jack", "Bob", "Tim", "Sara"]

people_2 = ["Tom", "Sam"]
people_2.extend(people)

tim_index = people_2.index("Jack")
print(people_2, tim_index, people_2[tim_index])