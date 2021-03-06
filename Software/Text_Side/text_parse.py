'''Reads in a file and breaks it into sections'''
class Text_Parse:
    '''Reads in a file and breaks it into sections'''

    def __init__(self, interface):
        self.interface = interface


    def read_text_file(self, path):
        '''
        Opens and Reads in Text File
        Args: the file path of a text file
        Returns the string of a file that has been read in
        '''
        self.interface.check_buttons()
        open_file = open(path, 'r')
        text = open_file.read()
        print(text)
        return text

    def break_up_text_input(self, text):
        '''
        Breaks the text into space based separations (title, paragraph etc)
        Args: string of text or other input
        Returns: text in a list which is broken up BY SECTION and
        ready to pass to the translator class

        # >>> break_up_text_input('Hello hi there')
        # 'Hello hi there'
        '''
        segments = []
        section = []
        for char in text:
            self.interface.check_buttons()

            if char == '\n':
                segments.append(section)
                section = ''
            else:
                section += char
        segments.append(section)

        output = ''
        for segment in segments:
            self.interface.check_buttons()

            segment = output.join(segment)

        return segments

    def set_segment_type(self, segment):
        '''
        Sets the type of segment being looked at or taken in (paragraph, title, image, table etc)
        Args: Segment of Document
        '''
        return 0

    def get_segment_type(self):
        '''
        Returns the type of segment being looked at or taken in
        Returns: Type (paragraph, title, image, table) etc
        '''
        # TODO: Figure out if this is what we want. Do we need this? Is it a later sprint? Does it make sense to do this? What is our application?
        return 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    parser = Text_Parse()
    open_file = parser.read_text_file(file_path)
    parser.break_up_text_input(open_file)
# Some Pseudocode for my feelings on how this might look:
# for segment in segments:
#     translator.translate_baby!
