import math

def can_calculator(height,width,cover):
    area = height * width
    cans = math.ceil(area/coverage)
    print(f"You'll need {cans} cans of paint.")

test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))
coverage = 5
can_calculator(height=test_height, width=test_width, cover = coverage)