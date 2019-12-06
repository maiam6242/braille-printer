''' Wrapper for the Document class '''
class Document:
    ''' This is a collection of page objects, it tracks how much of the document is
    written and maybe does some analysis or controls. '''
    def __init__(self, interface):
        self.page_size = [8.5, 11]
        self.doc_list = []
        self.num_pages = len(self.doc_list)
        self.interface = interface

    def get_page_size_in_mm(self):
        '''
        Returns the size of the paper in the document (in millimeters)
        Returns: Array which is the x page dimension and the y
        page dimension IN MILLIMETERS [x_dim, y_dim] ie [215.9, 279.4]
        '''
        for count, dimension in enumerate(self.page_size):
            self.interface.check_buttons()
            self.page_size[count] = self.to_mm(dimension)
        return self.page_size

    def to_mm(self, val_in_inches):
        '''
        Converts a value in inches to the equivalent value in millimeters with two decimal points
        Returns: value in mms
        >>>to_mm(7)
        177.8
        >>>to_mm(8.73)
        221.742
        '''
        return round(val_in_inches*25.4, 2)

    def add_page_object(self, page):
        '''
        Adds a page object to the entire document
        Args: A page object to be added to the document
        '''
        self.doc_list.append(page)
        self.num_pages += 1
        # print(self.doc[0])
        print('page number: %s' %str(page.page_num))
