#This should figure out the position on the page and determine if the content needs to be split over multiple pages
import serial
from physical import physical

class drawable:

    lines = []
    position_on_page = []
    physical = physical('/dev/ttyACM0')

    def get_position_on_page(self):
        '''
        Gets the x, y position that the new braille segment should be on the page (based on the size of the matrix and how much of the page is taken up from the page object)
        Returns: an x and y starting position for the new segment to be written
        '''
        
        physical.current_position()

        return 0

    def set_position_on_page(self):
        '''
        Sets the x, y position that the new braille segment should be on the page based on the size of the matrix and how much of the page is taken up (from the page object)
        Args: size of segment, how much of page is currently being taken up
        '''

        return 0

    def should_split(self, size, postion):
        '''
        Determines whether or not the segment should be split over multiple pages based on the starting position and size of entire segment
        Args: size of segment and position on page
        Returns: Boolean which is True if the segment should be split over multiple pages and False if not
        '''

        return 0

    def split_line(self):
        '''
        If the string should be split, determines what line the matrix/segment should be split at and stores that in variable line in the form of a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        Args: size of the segment, how many lines the segment is (from translator)
        Returns: the value of line: a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        '''

        return 0
