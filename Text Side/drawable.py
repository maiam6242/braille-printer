#This should figure out the position on the page and determine if the content needs to be split over multiple pages
import serial
from physical import physical
import translator

class drawable:

    physical = physical('/dev/ttyACM0')
    page_left = 0
    page_length = 279.4
    y_margin_size = 25.4
    x_margin_size = 25.4
    line_height = 6.3
    line_spacing = 8.66 #FIXME!!!
    character_width = 3.9
    chars_per_line = translator.charactersPerLine

    def get_end_position_on_page(self, size):
        '''
        Gets the x, y position that the new braille segment should be on the page (based on the size of the matrix and how much of the page is taken up from the page object)
        Returns: an x and y starting position for the new segment to be written
        '''
      
        y_size = size[1]
        y = self.physical.current_position()[1]
        x = self.x_margin_size
        end_y = y + y_size
        
        return x, end_y

    def should_split(self, end_y_position):
        '''
        Determines whether or not the segment should be split over multiple pages based on the starting position and size of entire segment
        Args: size of segment and position on page
        Returns: Boolean which is True if the segment should be split over multiple pages and False if not
        '''

        if self.page_length - end_y_position >= self.y_margin_size:
            return True
        else:
            return False

    def split_line(self, segment, num_lines, size, lines_written, lines_per_page):
        '''
        If the string should be split, determines what line the matrix/segment should be split at and stores that in variable line in the form of a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        Args: size of the segment, how many lines the segment is (from translator)
        Returns: the value of line: a list of dot matrices, with the first entry being the portion which should be written on the first page and the second entry being the portion to be written on the next page
        '''

        #TODO: Write me, dude!! SHould probably put in tolerancing of some kind?
        #FIXME: STOP PLAYING FAST AND LOOSE WITH LINES VS MMS

        lines_on_first = lines_per_page - lines_written
        lines_on_second = num_lines - lines_on_first

        #FIXME: Figure this one out!
        first = []
        second = []
        print(segment[0])
        for row1 in range(0,lines_on_first*3):
            first.append(segment[row1]) #TODO: make this work
        for row2 in range(lines_on_first*3, lines_on_second*3):
            second.append(segment[row2])

        # np.shape(segment)

        return [first, second]

    def is_full(self):
        if self.page_length - physical.current_position()[1] >= self.y_margin_size:
            return False
        else:
            return True 

    def size_on_page(self, number_lines):
        '''
        Determines the amount of space on a page which the segment will take up and converts that to an amount of millimeters, sets the variable size to the dimensions in millimeters in the form of a list
        Args: number of lines in a segment
        Returns: the dimensions in millimeters in the form of a list
        '''
    
        # A braille line is .28 inches in height
        # Braille lines are typically spaced .04 inches from top to top (not .04 apart)

        # |____|  | is y_size and _ is x_size

        # TODO: Check this
        

        y_size = self.line_height * number_lines + self.line_spacing * number_lines
        x_size = self.chars_per_line * self.character_width # NEED TO ACTUALLY CALC AND FIND THIS
        size = [round(x_size,2), round(y_size,2)]
        print(size)
        return size

