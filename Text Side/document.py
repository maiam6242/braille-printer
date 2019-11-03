# This is a collection of page objects, it tracks how much of the document is written and maybe does some analysis or controls. 
#prob track page size?

page_size = [8.5,11] 
doc = []
def set_page_size(page_size_input):
    '''
    Sets the size of paper of each page in the document
    Args: Array which is the x page dimension and the y page dimension IN INCHES [x_dim, y_dim] ie [8.5, 11]    
    '''
    page_size = page_size_input
    
def get_page_size_in_mm():
    '''
    Returns the size of the paper in the document (in millimeters)
    Returns: Array which is the x page dimension and the y page dimension IN MILLIMETERS [x_dim, y_dim] ie [215.9, 279.4]
    '''
    for count, dimension in enumerate(page_size):
        page_size[count] = to_mm(dimension)
    return page_size

def to_mm(val_in_inches):
    '''
    Converts a value in inches to the equivalent value in millimeters with two decimal points
    Returns: value in mms
    >>>to_mm(7)
    177.8
    >>>to_mm(8.73)
    221.742
    '''
    return round(val_in_inches*25.4, 2)

def add_page_object(page):
    '''
    Adds a page object to the entire document
    Args: A page object to be added to the document
    '''
    doc.append(page)