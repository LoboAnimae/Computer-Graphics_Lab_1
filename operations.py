import time
import struct


class Renderer:
    def __init__(self, builders):
        if self.glinit(builders):
            print('Parameters introduced correctly.')
            self.__f = open(self.__file_name, 'bw')
            self.gl_create_window(builders['width'], builders['height'])
        else:
            raise Exception('Parameters couldn\'t be used to create object')

    def glinit(self, builders):
        """Initializes any object that is required by the Software Renderer
        """
        try:
            self.__canvas = (builders['width'], builders['height'])
            self.__viewport = (builders['viewport_x'], builders['viewport_y'],
                               builders['viewport_coords'][0], builders['viewport_coords'][1])
            self.__point = (builders['point'][0], builders['point'][1])
            self.__rgb = (builders['rgb'][2],
                          builders['rgb'][1], builders['rgb'][0])
            self.__file_name = time.strftime("%H%M%S") + '_output_BMP_file.bmp'
            self.__clear_color = [builders['clear'][2],
                                  builders['clear'][1], builders['clear'][0]]
            self.__point_color = [builders['point_color'][2],
                                  builders['point_color'][1], builders['point_color'][0]]
            return True
        except:
            return False

    def convert(self, argument, conversion_type):
        if conversion_type == 1:
            return struct.pack('=c', argument.encode('ascii'))
        elif conversion_type == 2:
            return struct.pack('=l', argument)
        elif conversion_type == 3:
            return struct.pack('=h', argument)

    def gl_create_window(self, width, height):
        """Creates a window so that stuff can be drawn.

        Args:
            width (int): The width
            height (int): [description]
        """
        # File Header
        self.__f.write(self.convert('B', 1))
        self.__f.write(self.convert('M', 1))
        self.__f.write(self.convert(
            (14 + 40 + width + height), 2))
        self.__f.write(self.convert(0, 2))
        self.__f.write(self.convert(54, 2))

        # Image Header
        self.__f.write(self.convert(40, 2))
        self.__f.write(self.convert(width, 2))
        self.__f.write(self.convert(height, 2))
        self.__f.write(self.convert(1, 3))
        self.__f.write(self.convert(24, 3))
        self.__f.write(self.convert(0, 2))
        self.__f.write(self.convert((width * height * 3), 2))
        self.__f.write(self.convert(0, 2))
        self.__f.write(self.convert(0, 2))
        self.__f.write(self.convert(0, 2))
        self.__f.write(self.convert(0, 2))

        try:
            self.__framebuffer = [
                [bytes([self.__rgb[2], self.__rgb[1], self.__rgb[0]])  # TODO: CHANGE THE COLOR SO THAT IT CAN BE CHOSEN BY THE USER
                 for i in range(width)]
                for j in range(height)
            ]

            self.gl_view_port(
                self.__viewport[2], self.__viewport[3], self.__viewport[0], self.__viewport[1])
            return True
        except:
            return False

    def gl_view_port(self, x, y, width, height):
        for x in range(width):
            for y in range(height):
                self.__framebuffer[y][x] = bytes([255, 255, 255])

        self.gl_vertex(self.__point[0], self.__point[1])

    def gl_clear(self):
        pass

    def gl_clear_color(self, r, g, b):
        try:
            self.__clear_color = [b, g, r]
            return True
        except:
            return False

    def gl_vertex(self, x, y):
        self.__framebuffer[y][x] = bytes(
            [150, 0, 0])
        self.gl_finish()

    def gl_color(self, r, g, b):
        self.__point_color = [b, g, r]

    def gl_finish(self):
        for x in range(self.__canvas[0]):
            for y in range(self.__canvas[1]):
                self.__f.write(self.__framebuffer[y][x])
        self.__f.close()

        print('Generated ' + str(self.__file_name))


builders = {
    'width': 100,
    'height': 100,
    'viewport_x': 50,
    'viewport_y': 50,
    'point': [49, 49],
    'viewport_coords': [0, 0],
    'rgb': [0, 0, 0],
    'clear': [13, 14, 59],
    'point_color': [100, 100, 0]
}


bmp = Renderer(builders)
