"""
Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”
"""
import math

def main():
    # assign initial best values
    max_storage_eff = -1
    best_storage_eff_can = ''
    max_cost_eff = -1
    best_cost_eff_can = ''

    # can_sizes = [["#1 Picnic",6.83,10.16,0.28], ]

    # load dataset from csv file
    with open('cans.csv') as cans_file:
        # skip header
        next(cans_file)

        # loop through each can data line
        for line in cans_file:
            can_details = line.strip().split(',') #returns a list

            # # store each part in a variable
            can_name = can_details[0]
            can_radius = float(can_details[1])
            can_height = float(can_details[2])
            can_cost = float(can_details[3])

            # call compute storage efficiency function
            storage_efficiency = compute_storage_efficiency(can_radius, can_height)

            # call compute cost efficiency function
            cost_efficiency = compute_cost_efficiency(can_cost, can_radius, can_height)

            print(f'{can_name} {storage_efficiency:.2f} {cost_efficiency:.2f}')

            # check best storage effifciency and cost efficiency
            if storage_efficiency > max_storage_eff:
                max_storage_eff = storage_efficiency
                best_storage_eff_can = can_name
            
            if cost_efficiency > max_cost_eff:
                max_cost_eff = cost_efficiency
                best_cost_eff_can = can_name

    print(f'The most storage efficient can is {best_storage_eff_can} with a value of {max_storage_eff:.2f}, while the most cost efficient can is {best_cost_eff_can} with a value of {max_cost_eff:.2f}')


# Function that computes can volume
def compute_volume(radius, height):
    vol = math.pi * (radius ** 2) * height
    return vol


# Function that computes can surface area
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Function that computes cost efficiency
def compute_cost_efficiency(cost, radius, height):
    # calculate volume with compute_volume function
    vol = compute_volume(radius, height)
    cost_efficiency = vol / cost
    return cost_efficiency

# function that computes storage efficiency
def compute_storage_efficiency(radius, height):
    # call compute volume function to calculate can volume
    can_volume = compute_volume(radius, height)

    # call compute surface area function to calculate can surface area
    can_surface_area = compute_surface_area(radius, height)

    # calculate storage efficiency
    storage_efficiency = can_volume / can_surface_area

    return storage_efficiency


# # call the main function
main()