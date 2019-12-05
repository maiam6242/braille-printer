"""This needs to say how much of the page is currently taken up, what
the page number should be and handle spacing on a page"""


# TODO: Find right default value for the two vars below!!
# space_bw_lines = 0 # 8.66 mm
# margins = 0

class Page:
    """This needs to say how much of the page is currently taken up, what
    the page number should be and handle spacing on a page"""
   

    def __init__(self, page_number):
        '''
        Set up the page object by setting the page number of the page
        '''
        self.page_num = page_number
        self.lines_written = 0
        self.content = []

    def add_content(self, content_to_add, num_lines):
        '''
        Adds content in the form of a numpy array to a page
        Args: The array of content to add to the page and the number of lines that content takes up
        '''
        #FIXME: Lines written isn't actually working with l_w += num_lines
        self.lines_written += num_lines
        print(self.lines_written)
        self.content.extend(content_to_add)
        print(self.page_num)
        print('Lines written on the page: '+ str(self.lines_written))
