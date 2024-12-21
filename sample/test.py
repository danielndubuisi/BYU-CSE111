
# from datetime import datetime as dt

# day_of_the_week = {
#     0 : "Monday",
#     1 : "Tuesday",
#     2 : "Wednesday",
#     3 : "Thursday",
#     4 : "Friday",
#     5 : "Saturday",
#     6 : "Sunday",
# }


# def get_weekday(day_number):
#     if day_number:
#         print(f'The day of the week is {day_of_the_week[day_number]}')

# day_number = dt.now().weekday()

# get_weekday(day_number)


numbers = [1, 3, 56, 34, 25, 11, 2, 5, 8, 9, 0, 23, 67 ]

employees = [
    { "name": "Daniel",
    "age": 23,
    "ID": "10002345ND",
    "department": "IT",
    "role": "Developer"
    },
    { "name": "John",
    "age": 25,
    "ID": "10376w345AJ",
    "department": "IT",
    "role": "Designer"
    },
    { "name": "Kunle",
    "age": 28,
    "ID": "235679345KO",
    "department": "Marketing",
    "role": "Marketer"
    },
]

emp_names = map(lambda emp: emp["name"], employees)

mp = map(lambda num: num + 1, numbers)
filtered = filter(lambda num: num % 2 == 0 and num > 0, numbers)

print(list(mp))
print(list(filtered))

