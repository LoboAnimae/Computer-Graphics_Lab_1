from operations import Renderer

image_width = 0
image_height = 0
sub_image_width = 0
sub_image_heigth = 0
point_coordinates = [0, 0]
viewport_upper_left = [0, 0]
rgb = [0, 0, 0]


def entry_point(failure=False):
    """Entry point of the program. It's whatever the user sees for the 
       first time and allows the values to be changed or not. 

    Args:
        failure (bool, optional): If the program fails, act differently. Defaults to False.
    """
    if failure:
        print('\033[1;37;41m')
        failure_var = 'Something went wrong. Restarting program...'

        border = '-'
        for i in failure_var:
            border = border + '-'

        print('\n\n\n\n' + border + '\n' +
              failure_var + '\n' + border + '\n\n\n\n')
        print('\033[0;37;40m')

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
    """Let's the user use new values for the program
    """
    print('Please input your values:')
    width = int(input('Input your width: '))
    height = int(input('Input your height: '))
    try:
        sub_width = int(
            input('Input your viewport sub-width (PRESS ENTER TO NOT CREATE A VIEWPORT): '))
    except:
        warning = '\nA VIEWPORT WILL NOT BE CREATED. SKIPPING VIEWPORT VALUES\n'
        border = ''
        for i in warning:
            border = border + '-'
        print('\033[1;37;41m')
        print(border + warning + border)
        print('\033[0;37;40m')
        sub_width = ''
    if sub_width == '':
        sub_width = 0
        sub_height = 0
        viewport_x = 0
        viewport_y = 0
    else:
        while sub_width > width:
            sub_width = int(
                input('Input your viewport sub-width (SUB-WIDTH CAN\'T BE BIGGER THAN WIDTH (' + str(width) + ')): '))
        try:
            sub_height = int(input('Input your viewport sub-height: '))
            while sub_height > height:
                sub_height = int(input(
                    'Input your viewport sub-height (It can\'t be higher than Height(' + str(height) + '): '))
        except:
            sub_height = sub_width
        try:
            viewport_x = int(
                input('Please input the X-Value of the upper-left corner: '))
            while width - sub_width < viewport_x:
                viewport_x = int(
                input('Please input the X-Value of the upper-left corner (Given your values, this value must be equal or less than ' + str(width - sub_width) + ' without being negative): '))
        except:
            viewport_x = 0
        try:
            viewport_y = int(
                input('Please input the Y-Value of the upper-left corner: '))
            while height - sub_height < viewport_y:
                viewport_y = int(
                input('Please input the Y-Value of the upper-left corner (Given your values, this value must be equal or less than ' + str(height - sub_height) + ' without being negative): '))

        except:
            viewport_y = 0

    x = int(input('Input your X-value: '))
    while x > width:
        x = int(input(
            'The X-value must be smaller than the width value (Currently ' + str(width) + '): '))
    y = int(input('Input your Y-value: '))
    while y > height:
        y = int(input(
            'The Y-value must be smaller than the height value (Currently ' + str(height) + '): '))
    print('\033[0;31;40m')
    red = int(input('Please input your RED value: '))
    while red < 0 or red > 255:
        red = int(input('Your RED value must be a number between 0 and 255: '))
    print('\033[0;32;40m')
    green = int(input('Please input your GREEN value: '))
    while green < 0 or green > 255:
        green = int(
            input('Your GREEN value must be a number between 0 and 255: '))
    print('\033[0;34;40m')
    blue = int(input('Please input your BLUE value: '))
    while blue < 0 or blue > 255:
        blue = int(input('Your BLUE value must be a number between 0 and 255: '))
    print('\033[0;37;40m')
    set_values(width, height, sub_width, sub_height, x, y,
               viewport_x, viewport_y, red, green, blue)


def main():
    """Main Section of the program
    """
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
        builders = {
            'width': image_width,
            'height': image_height,
            'viewport_x': sub_image_width,
            'viewport_y': sub_image_heigth,
            'point': point_coordinates,
            'viewport_coords': viewport_upper_left,
            'rgb': rgb
        }
        image_creator = Renderer(builders)

    elif choice == 2:
        choose_values()
    elif choice == 3:
        show_values()
    elif choice == 4:
        exit(0)
    else:
        print('You somehow ended here. Congrats.')
        entry_point(True)


def set_values(width=100, height=100, sub_width=0, sub_height=0, x=0, y=0, viewport_x=0, viewport_y=0, red=0, green=0, blue=0):
    """Sets the values at any point of the program. Can change to default values. 

    Args:
        width (int, optional): Width of the image. Defaults to 100.
        height (int, optional): Height of the image. Defaults to 100.
        sub_width (int, optional): Witdh of the viewport. Defaults to 0.
        sub_height (int, optional): Height of the viewport. Defaults to 0.
        x (int, optional): X of the point. Defaults to 0.
        y (int, optional): Y of the point. Defaults to 0.
        viewport_x (int, optional): Where the viewport's top left corner is in X. Defaults to 0.
        viewport_y (int, optional): Where the viewport's top left corner is in Y. Defaults to 0.
        red (int, optional): RED value of RGB. Defaults to 0.
        green (int, optional): GREEN value of RGB. Defaults to 0.
        blue (int, optional): BLUE value of RGB. Defaults to 0.
    """
    try:
        global image_width
        global image_height
        global sub_image_width
        global sub_image_heigth
        global point_coordinates
        global viewport_upper_left
        global rgb

        image_width = width
        image_height = height
        sub_image_width = sub_width
        sub_image_heigth = sub_height
        point_coordinates = [x, y]
        viewport_upper_left = [viewport_x, viewport_y]
        rgb = [red, green, blue]
        show_values()
    except Exception as e:
        print('An error has occurred: ' + str(e))
        entry_point(True)


def show_values():
    """Prints out the saved program values
    """
    print('\033[0;30;47m')
    print()
    print('----------------------------------------------------------------')
    print('Values have been set as:')
    print('Image size: ' + str(image_width) + 'x' + str(image_height))
    if sub_image_width != 0 and sub_image_heigth != 0:
        print('Viewport Size: ' + str(sub_image_width) +
              'x' + str(sub_image_heigth))
        print('Viewport Upper Left Corner: (' +
              str(viewport_upper_left[0]) + ', ' + str(viewport_upper_left[1]) + ')')
    print('Point\'s Coordinates: (' +
          str(point_coordinates[0]) + ', ' + str(point_coordinates[1]) + ')')
    print('Colors: RGB(\033[0;31;47m' + str(rgb[0]) + ',\033[0;32;47m ' +
          str(rgb[1]) + ',\033[0;34;47m ' + str(rgb[2]) + '\033[0;30;47m)')
    print('----------------------------------------------------------------')
    print()
    print('\033[0;37;40m')

    main()


entry_point()
