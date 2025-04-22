import math

manufactured_items = int(input('What is the number of manufactured items? '))
items_per_box = int(input('What is the number of items to pack per box? '))

total_boxes = math.ceil(manufactured_items/items_per_box)

print(f'For {manufactured_items} items, packing {items_per_box} items in each box, you will need {total_boxes} boxes.')