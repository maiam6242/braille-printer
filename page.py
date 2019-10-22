# This needs to say how much of the page is currently taken up, what the page number should be and handle spacing on a page

# TODO: Some sort of init function? Can I talk through some logic with someone when people get a chance

page_number = 0
# TODO: Find right default value for the two vars below!!
space_bw_lines = 0
margins = 0

def set_page_number(page_num):
    '''
    Sets the page number of the page object
    Args: Integer which is the page number of the given page
    '''

    return 0

def get_page_number():
    '''
    Returns the page number of the current page
    Returns: Integer which is the page number of the given page
    '''

    return 0

def current_amount_filled():
    '''
    This should calculate the amount of the page which is currently filled up and return that amount (in lines)
    NOTE: To get the current position of the puncher, use get_position_on_page in the drawable class. This class is specifically to handle attributes of a page
    Returns: the amount of lines which are written on the page
    '''

    return 0

def set_space_between_lines(spacing):
    '''
    This should take in the amount of space which should be between lines in inches(?! CHECK THIS UNIT) and set the space_bw_lines variable accordingly
    Args: desired space between lines (in inches)
    '''

    return 0

def get_space_between_lines():
    '''
    This should return the amount of space which should be between lines in inches(?! CHECK THIS UNIT) 
    Returns: desired space between lines (in inches)
    '''

    return 0

def set_page_margins(margins):
    '''
    This should take in the desired page margin width in inches(?! CHECK THIS UNIT) and set the margins variable accordingly
    Args: desired margin widths (in inches)
    '''
    return 0

def get_page_margins():
    '''
    This should return the desired margin width in inches(?! CHECK THIS UNIT)
    Returns: margin size (in inches)
    '''
    return 0