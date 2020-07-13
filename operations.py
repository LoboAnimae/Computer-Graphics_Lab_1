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

            return True
        except:
            return False

    def gl_create_window(self, width, height):
        """Creates a window so that stuff can be drawn. 

        Args:
            width (int): The width
            height (int): [description]
        """
        # File Header
        self.__f.write(struct.char('B'))
        self.__f.write(struct.char('M'))
        self.__f.write(struct.dword(
            14 + 40 + self.__canvas[0]+self.__canvas[1]))
        self.__f.write(struct.dword(0))
        self.__f.write(struct.dword(14 + 40))

        # Image Header
        self.__f.write(struct.dword(40))
        self.__f.write(struct.dword(self.__canvas[0]))
        self.__f.write(struct.dword(self.__canvas[1]))
        self.__f.write(struct.word(1))
        self.__f.write(struct.word(24))
        self.__f.write(struct.dword(0))
        self.__f.write(struct.dword(self.__canvas[0] * self.__canvas[1] * 3))
        self.__f.write(struct.dword(0))
        self.__f.write(struct.dword(0))
        self.__f.write(struct.dword(0))
        self.__f.write(struct.dword(0))


    def gl_view_port(self, x, y, width, height):
        """Defines an area where stuff can be directly drawn upon. Like a sub-space inside the window. 

        Args:
            x (int): X-Value for the top-left corner of the subspace.
            y (int): Y-Value for the top-left corner of the subspace.
            width (int): Total width of the subspace. X + Width <= Total width of the picture.
            height (int): Total height of the subspace. Y + Height <= Total height of the picture.
        """

    def gl_clear(self):
        pass

    def gl_clear_color(self, r, g, b):
        pass

    def gl_vertex(self, x, y):
        pass

    def gl_color(self, r, g, b):
        pass

    def gl_finish(self):
        pass
