# This needs to say how much of the page is currently taken up, what the page number should be and handle spacing on a page

# TODO: Some sort of init function? Can I talk through some logic with someone when people get a chance

page_number = 0
# TODO: Find right default value for the two vars below!!
# space_bw_lines = 0 # 8.66 mm
# margins = 0 

class page:

    def __init__(self):
        '''
        '''

    def set_page_number(self, page_num):
        '''
        Sets the page number of the page object
        Args: Integer which is the page number of the given page
        '''

        return 0

    def get_page_number(self):
        '''
        Returns the page number of the current page
        Returns: Integer which is the page number of the given page
        '''

        return 0

    def current_amount_filled(self):
        '''
        This should calculate the amount of the page which is currently filled up and return that amount (in lines)
        NOTE: To get the current position of the puncher, use get_position_on_page in the drawable class. This class is specifically to handle attributes of a page
        Returns: the amount of lines which are written on the page
        '''

        return 0

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