year_of_age = int (input("Enter your age: "))

list = []

if year_of_age % 2 == 0:
    print(range(0, year_of_age+1, 2))

if year_of_age % 2 == 1:
    print(range(1, year_of_age+1, 2))
       
