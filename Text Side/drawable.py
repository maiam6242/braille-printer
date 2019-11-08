#This should figure out the position on the page and determine if the content needs to be split over multiple pages
import serial
from physical import physical

class drawable:

    lines = []
    position_on_page = []
    physical = physical('/dev/ttyACM0')
    page_length = 279.4
    y_margin_size = 25.4
    x_margin_size = 25.4

    def get_end_position_on_page(self, size):
        '''
        Gets the x, y position that the new braille segment should be on the page (based on the size of the matrix and how much of the page is taken up from the page object)
        Returns: an x and y starting position for the new segment to be written
        '''
      
        y_size = size[1]
        y = physical.current_position()[1]
        x = x_margin_size
        end_y = y + y_size
        
        return x, end_y

    def should_split(self, end_y_position):
        '''
        Determines whether or not the segment should be split over multiple pages based on the starting position and size of entire segment
        Args: size of segment and position on page
        Returns: Boolean which is True if the segment should be split over multiple pages and False if not
        '''

        if page_length - end_y_position >= y_margin_size:
            return True
        else:
            return False

    def split_line(self, segment, size):
        '''
        If the string should be split, determines what line the matrix/segment should be split at and stores that in variable line in the form of a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        Args: size of the segment, how many lines the segment is (from translator)
        Returns: the value of line: a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        '''

        return 0
