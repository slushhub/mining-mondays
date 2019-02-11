"""
Variables
Variables are just names for values.
Names help in reading.
Imagine asd vs my_telephone_number, which is more informative?
"""

# my name is Tero
my_name = 'Tero'

# my age is 24
my_age = 24

# teemus age is two times my age
teemus_age = 2 * my_age




























"""
Conditionals
The point of conditionals is to check for a value and act based on it.
Note the indented things are run only if the condition is truthy!
"""

# my name is Tero
my_name = 'Tero'

# if my name is Tero
if my_name == 'Tero':
  
  # then print Buenos Aires!
  print('Buenos Aires!')




























"""
Functions
Functions can take variables as input values.
They all output a value.
The point of a function is to make implementation details hidden behind a name.
Imagine a post office is a function. You input them a package.
They do all the complex stuff to deliver it.
"""

# define a function called calculate circle area with radius
# it takes radius as an input
def calculate_circle_area_with_radius(radius):

  # calculated area is pi times radius to the power of 2
  calculated_area = math.pi * radius**2

  # return calculated area
  return calculated_area



# area1 is the calculated circle area with radius of 5
area1 = calculate_circle_area_with_radius(5) # 78,5...

# area2 is the calculated circle area with radius of 20
area2 = calculate_circle_area_with_radius(20) # 1256...

# area3 is the calculated circle area with radius of 412
area3 = calculate_circle_area_with_radius(412) # 532996,16...
