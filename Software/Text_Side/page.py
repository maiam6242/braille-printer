"""This needs to say how much of the page is currently taken up, what
the page number should be and handle spacing on a page"""


# TODO: Find right default value for the two vars below!!
# space_bw_lines = 0 # 8.66 mm
# margins = 0

class Page:
    """This needs to say how much of the page is currently taken up, what
    the page number should be and handle spacing on a page"""
    # page_num = 0

    def __init__(self, page_number):
        '''
        Set up the page object by setting the page number of the page
        '''
        self.lines_written = 0
        self.lines_per_page = 25
        self.content = []
        self.page_num = page_number

    def add_content(self, content_to_add, num_lines):
        '''
        Adds content in the form of a numpy array to a page
        Args: The array of content to add to the page and the number of lines that content takes up
        '''
        self.content.extend(content_to_add)
        self.lines_written += num_lines
        print(self.lines_written)
