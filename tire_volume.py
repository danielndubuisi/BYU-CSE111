"""the formula for volume of tire is v = (π * (w**2) * a ((w * a) + (2540 * d)))/10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
# import statements for useful modules
from datetime import datetime as dt
import math

# get user inputs
tire_width = float(input('Enter the width of the tire in mm (ex 205): '))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
wheel_diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

# approximate tire volume
tire_volume = math.pi * (tire_width ** 2) * aspect_ratio * ((tire_width * aspect_ratio) + (2540 * wheel_diameter))/10000000000

# get current date and time
current_date = dt.now()

# print output
print(f'The aproximate volume is {tire_volume:.2f} liters')

# Exceeding requirements with additional functionality
buy_tire = input('Do you want to buy tire with these dimensions?(Yes/No): ').lower()

# append user phone number if response is Yes
if buy_tire == 'yes':
    user_phone = input('Enter your phone number: ')
    # open and append data and phone number to text file
    with open('volumes.txt', mode='at') as volumes_file:
        # print information to the volumes text file
        print(f'{current_date:%Y-%m-%d}, {tire_width:.0f}, {aspect_ratio:.0f}, {wheel_diameter:.0f}, {tire_volume:.2f}, {user_phone}', file=volumes_file)
else:
    # open and append data only to text file
    with open('volumes.txt', mode='at') as volumes_file:
        # print information to the volumes text file
        print(f'{current_date:%Y-%m-%d}, {tire_width:.0f}, {aspect_ratio:.0f}, {wheel_diameter:.0f}, {tire_volume:.2f}', file=volumes_file)
