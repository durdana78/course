'''
radius = int(input('Insert the radius: '))

while radius != 0:
    Area = 3.14 * radius ** 2
    Result = "The area of the circle is " + str(Area)
    print(Result)
    radius = int(input('Insert the radius: '))  # Convert input to int here

    if radius == 0:
        print('Radius cannot be 0\nTry a valid number')
        radius = int(input('Insert the radius: '))
'''

while True:
    radius = int(input('Insert the radius: '))

    if radius == 0:
        print('Radius cannot be 0\nTry a valid number')
    else:
        Area = 3.14 * radius ** 2
        Result = "The area of the circle is " + str(Area)
        print(Result)



