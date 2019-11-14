# This needs to say how much of the page is currently taken up, what the page number should be and handle spacing on a page

# TODO: Some sort of init function? Can I talk through some logic with someone when people get a chance

page_number = 0
# TODO: Find right default value for the two vars below!!
# space_bw_lines = 0 # 8.66 mm
# margins = 0 

class page:
    page_num = 0
    lines_written = 0
    lines_per_page = 25
    content = []

    def __init__(self, page_number):
        '''
        '''
        self.page_num = page_number
       
    def add_content(self, content_to_add, num_lines):

        self.content.append(content_to_add)
        self.lines_written += num_lines

    # def current_amount_filled(self):
    #     '''
    #     This should calculate the amount of the page which is currently filled up and return that amount (in lines)
    #     NOTE: To get the current position of the puncher, use get_position_on_page in the drawable class. This class is specifically to handle attributes of a page
    #     Returns: the amount of lines which are written on the page
    #     '''

    #     return lines_written

    def is_full(self):

        if lines_written == lines_per_page:
            return True
        else:
            return False

    # def set_space_between_lines(self, spacing):
    #     '''
    #     This should take in the amount of space which should be between lines in millimeters(?! CHECK THIS UNIT) and set the space_bw_lines variable accordingly
    #     Args: desired space between lines (in millimeters)
    #     '''

    #     return 0

    # def get_space_between_lines(self):
    #     '''
    #     This should return the amount of space which should be between lines in millimeters(?! CHECK THIS UNIT) 
    #     Returns: desired space between lines (in millimeters)
    #     '''

    #     return 0

    # def set_page_margins(self, in_margins):
    #     '''
    #     This should take in the desired page margin width in millimeters(?! CHECK THIS UNIT) and set the margins variable accordingly
    #     Args: desired margin widths (in millimeters)
    #     '''
        
    #     margins = in_margins
        

    # def get_page_margins(self):
    #     '''
    #     This should return the desired margin width in millimeters(?! CHECK THIS UNIT)
    #     Returns: margin size (in millimeters)
    #     '''
    #     return 0