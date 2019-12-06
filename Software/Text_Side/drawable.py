'''This should figure out the position on the page and determine if the
content needs to be split over multiple pages'''
import serial
import numpy as np
from Text_Side.physical import Physical
import Text_Side.translator as translator

class Drawable:
    '''This should figure out the position on the page and determine if the
    content needs to be split over multiple pages
    '''
    
    def __init__(self, serial, interface):
        self.page_left = 0
        self.page_length = 279.4
        self.y_margin_size = 25.4
        self.x_margin_size = 25.4
        self.line_height = 6.3
        self.line_spacing = 8.66 #FIXME!!!
        self.character_width = 3.9
        self.physical = Physical(serial, self.character_width, self.line_height, interface)
        self.interface = interface
        self.chars_per_line = translator.CHARACTERS_PER_LINE
        self.position_on_page = 0 #TODO: HOW TF SHOULD THIS BE HANDLED WHILE STILL BEING ABLE TO CHECK FOR BUTTONS #self.physical.current_position()[1]

    def get_end_position_on_page(self, size):
        '''
        Gets the x, y position that the new braille segment should be on the page
        (based on the size of the matrix and how much of the page is taken up from the page object)

        Returns: an x and y starting position for the new segment to be written
        '''
        print('[drawable.py] ','starting position_on_page: %s' %self.position_on_page)
        y_size = size[1]
        x = self.x_margin_size
        end_y = self.position_on_page + y_size
        self.position_on_page += y_size
        print('[drawable.py] ', 'end y: %s' %end_y)
        print('[drawable.py] ', 'new position_on_page: %s' %self.position_on_page)
        return x, end_y

    def should_split(self, end_y_position):
        '''
        Determines whether or not the segment should be split over
        multiple pages based on the starting position and size of entire segment
        Args: size of segment and position on page
        Returns: Boolean which is True if the segment should be split over
        multiple pages and False if not
        '''
        print('[drawable.py] ', 'should split')
        print('[drawable.py] ', 'type of page_length: %s and value:' % type(self.page_length))
        print('[drawable.py] ', 'type of end_y_position: %s and value:' %type(end_y_position))
        print('[drawable.py] ', 'page_length - end_y_position: ' + str(float(self.page_length) \
            - float(end_y_position)))
        print('[drawable.py] page length : %f' %self.page_length)
        if self.page_length - self.position_on_page <= self.y_margin_size:
            print('[drawable.py] ', 'should really split')
            return True
        else:
            print('[drawable.py] ', 'shouldn\'t split')
            return False

    def split_line(self, segment, num_lines):
        '''
        If the string should be split, determines what line the matrix/segment should be
        split at and stores that in variable line in the form of a list of dot matrices,
        with the first entry being the portion which should be written on the first page
        and the second entry being the portion to be written on the next page
        Args: size of the segment, how many lines the segment is (from translator)
        Returns: the value of line: a list of dot matrices, with the first entry being the
        portion which should be written on the first page and the second entry being the
        portion to be written on the next page
        '''

        #TODO: Write me, dude!! Should probably put in tolerancing of some kind?

        self.interface.check_buttons()
        print('[drawable.py] ', 'how much usable space there is: %s' % str(self.page_left - self.y_margin_size))
        print('[drawable.py] ', 'That means there are ___ lines left on this page (see below :\'( )')
        print('[drawable.py] ', str(round((self.page_left-self.y_margin_size) \
            / (self.line_height+self.line_spacing), 0)))
        print(self.line_height+self.line_spacing)
        print('[drawable.py] ', 'number of lines in segment: %s'%num_lines)
        lines_on_first = int(round((self.page_left-self.y_margin_size) \
            /(self.line_height+self.line_spacing), 0))
        print('[drawable.py] ', 'number of lines in segment that should be in first section: %s'%str(lines_on_first))
        lines_on_second = int(num_lines - lines_on_first)
        print('[drawable.py] ', 'lines that should be written on second page: %s' %str(lines_on_second))
        first = []
        second = []
        print('[drawable.py] ', type(segment))
        print('[drawable.py] ', 'this is the shape of the segment: %s' %str(np.shape(segment)))
        print('[drawable.py] ', int(lines_on_first))

        for row1 in range(0, lines_on_first):
            self.interface.check_buttons()
            print('[drawable.py] ', row1)
            first.append(segment[row1, :])
        for row2 in range(lines_on_first+1, num_lines):
            self.interface.check_buttons()
            print('[drawable.py] ', row2)
            second.append(segment[row2, :])

        return [first, lines_on_first, second, lines_on_second]

    def is_full(self):
        '''
        Determines whether or not a page is full based on the position on the page
        (as opposed to the number of lines that have been written)
        Returns: True if the page is full and False if the page is not filled yet
        '''
        self.interface.check_buttons()
        print('[drawable.py] ', 'is full')
        print('[drawable.py] ', 'is left %s' %str(self.page_length - self.position_on_page))
        print('[drawable.py] ', 'position_on_page: '+str(self.position_on_page))
        self.page_left = self.page_length - self.position_on_page
        if self.page_length - self.position_on_page >= self.y_margin_size:
            print('[drawable.py] ', 'is not full')
            return False
        else:
            print('[drawable.py] ', 'is actually full')
            return True

    def size_on_page(self, number_lines):
        '''
        Determines the amount of space on a page which the segment will take up
        and converts that to an amount of millimeters, sets the variable size
        to the dimensions in millimeters in the form of a list
        Args: number of lines in a segment
        Returns: the dimensions in millimeters in the form of a list
        '''

        # A braille line is .28 inches in height
        # Braille lines are typically spaced .04 inches from top to top (not .04 apart)

        # |____|  | is y_size and _ is x_size

        # TODO: Check this

        self.interface.check_buttons()
        y_size = self.line_height * number_lines + self.line_spacing * number_lines
        x_size = self.chars_per_line * self.character_width # NEED TO ACTUALLY CALC AND FIND THIS
        size = [round(x_size, 2), round(y_size, 2)]
        print('[drawable.py] ', size)
        return size
