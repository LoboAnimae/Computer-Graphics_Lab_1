import operations

image_width = 0
image_height = 0
point_x = 0
point_y = 0
rgb = [0, 0, 0]


def entry_point(failure=False):
    if failure:
        failure_var = 'Something went wrong. Restarting program...'
        border = '-'
        for i in failure_var:
            border = border + '-'
        print('\n\n\n\n' + border + '\n' +
              failure_var + '\n' + border + '\n\n\n\n')

    try:
        print('Hello, and welcome to the program.')
        printing_menu = 'In this program, you will be able to generate a single picture with a certain'
        border = ''
        for i in printing_menu:
            border = border + '-'
        print(border + '\n' + printing_menu)
        print('background of your choosing. \nDo you wish to start the program with the default values?(Y/N)\n' + border)
        option = input('>>> ')
        if option == 'y' or option == 'Y':
            print('Default values have been set')
            set_values()
        else:
            choose_values()
    except Exception as e:
        print('An error has occurred: ' + str(e))
        entry_point(True)


def choose_values():
    print('Please input your values:')
    width = int(input('Input your width: '))
    height = int(input('Input your height: '))
    x = int(input('Input your X-value: '))
    while x > width:
        x = int(input(
            'The X-value must be smaller than the width value (Currently ' + str(width) + '): '))
    y = int(input('Input your Y-value: '))
    while y > height:
        y = int(input(
            'The Y-value must be smaller than the height value (Currently ' + str(height) + '): '))
    red = int(input('Please input your RED value: '))
    while red < 0 or red > 255:
        red = int(input('Your RED value must be a number between 0 and 255: '))
    green = int(input('Please input your GREEN value: '))
    while green < 0 or green > 255:
        green = int(
            input('Your GREEN value must be a number between 0 and 255: '))
    blue = int(input('Please input your BLUE value: '))
    while blue < 0 or blue > 255:
        blue = int(input('Your BLUE value must be a number between 0 and 255: '))
    set_values(width, height, x, y, red, green, blue)


def main():
    menu = 'Please select one of the following: '
    option1 = '1. Generate BMP Image'
    option2 = '2. Change Image Values'
    option3 = '3. Check Current Values'
    option4 = '4. Exit Program'
    print(menu + '\n' + option1 + '\n' +
          option2 + '\n' + option3 + '\n' + option4)
    choice = 0
    while choice < 1 or choice > 4:
        try:
            choice = int(input('>>> '))
        except Exception as e:
            print('Invalid choice type.')
            main()
    if choice == 1:
        pass
    elif choice == 2:
        choose_values()
    elif choice == 3:
        show_values()
    elif choice == 4:
        exit(0)
    else:
        print('You somehow ended here. Congrats.')
        entry_point(True)


def set_values(width=100, height=100, x=0, y=0, red=0, green=0, blue=0):
    try:
        global image_width
        global image_height
        global point_x
        global point_y
        global rgb

        image_width = width
        image_height = height
        point_x = x
        point_y = y
        rgb = [red, green, blue]
        show_values()
    except Exception as e:
        print('An error has occurred: ' + str(e))
        entry_point(True)


def show_values():
    print('----------------------------------------------------------------')
    print('Values have been set as:')
    print('Width: ' + str(image_width))
    print('Height: ' + str(image_height))
    print('X-Value: ' + str(point_x))
    print('Y-Value: ' + str(point_y))
    print('Colors: RGB(' + str(rgb[0]) + ', ' +
          str(rgb[1]) + ', ' + str(rgb[2]) + ')')
    print('----------------------------------------------------------------')

    main()


entry_point()
