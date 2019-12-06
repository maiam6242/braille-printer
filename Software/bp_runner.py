"""This will become the "main" runner class"""
import serial
import numpy as np
from Text_Side.text_parse import Text_Parse
from Text_Side.drawable import Drawable
from Text_Side.translator import Translator
from Text_Side.document import Document
from Text_Side.page import Page
from Physical_Interface.interface import Interface
from Text_Side.physical import Physical
from Recognizing_Input import select_file

# FILE = select_file.select_file()




PORT = '/dev/ttyACM0'

#setting up all of the things
SER = serial.Serial(PORT, baudrate=115200, timeout=1)
INTERFACE = Interface(SER)

# FILE_PATH = 'Text_Side/test_story.txt'
FILE_PATH = select_file.select_file(INTERFACE)
PARSER = Text_Parse(INTERFACE)
SEGMENTED = PARSER.break_up_text_input(PARSER.read_text_file(FILE_PATH))

select_file.clear(FILE_PATH)

TRANSLATOR = Translator(INTERFACE)

FORMATTED = []
TOTAL_NUM_LINES = 0

DRAWABLE = Drawable(SER, INTERFACE)

DOC = Document(INTERFACE)

# This loop analyzes the texts as well as places it on various pages
# (and splits text lines accordingly). It places all from one page in a
# page object with that page number associated with it. Once a page is
# full or if the last segment in the entire array of text is processed,
# these pages are added to a document object
count = 1
locals()['page_'+ str(count)] = Page(count)
n = 'page_'+ str(count)
print('[bp_runner.py] ', count)
print('[bp_runner.py] ', locals().get(n).page_num)

for segment in SEGMENTED:
    count = 1
    braille_tx, num_lines = TRANSLATOR.convert_to_braille(segment)
    size_in_mm = DRAWABLE.size_on_page(num_lines) #[x,y]

    end_x, end_y = DRAWABLE.get_end_position_on_page(size_in_mm)
    print('[bp_runner.py] ', end_x)
    print('[bp_runner.py] ', end_y)

    if DRAWABLE.should_split(end_y):
        splits = DRAWABLE.split_line(braille_tx, num_lines)
        print('[bp_runner.py] ', splits)
        locals().get(n).add_content(splits[0], splits[1])
        DOC.add_page_object(locals().get(n))
        count += 1

        DRAWABLE.position_on_page = 0
        locals()['page_'+ str(count)] = Page(count)
        n = 'page_'+ str(count)
        print('[bp_runner.py] ', 'next page: ' + str(n))
        print('[bp_runner.py] ', locals().get(n))
        locals().get(n).add_content(splits[2], splits[3])
    else:
        print('[bp_runner.py] ', locals().get(n))
        locals().get(n).add_content(braille_tx, num_lines)
        print('[bp_runner.py] ','yooo added, baby!')

        #TODO: Check these measurements! This should be 25 lines, right now, with measurements. it is only 17...
    if DRAWABLE.is_full():
        count += 1
        DRAWABLE.position_on_page = 0
        DOC.add_page_object(locals().get(n))

    if(DOC.num_pages != count and segment is SEGMENTED[-1]):
        DOC.add_page_object(locals().get(n))
        print('[bp_runner.py] ', 'added page to the end of the document')
        


# drawable.physical.disable()
print('[bp_runner.py] ', DOC.num_pages)

# This loop handles the actual punching of the characters. 
# It waits for interface feedback at each step in the process
#  (most of this logic is contained in the actual methods of the physical class)

#FIXME: Get this working with the interface!
#TODO: Test this logic, wrapped the if and else differently
while not INTERFACE.is_start_print():
    INTERFACE.wait_for_print()
    
if not INTERFACE.is_cancel():
    print('[bp_runner.py] ','did we get here')
    if INTERFACE.is_play:
        print('[bp_runner.py] ','how about here')
        print('[bp_runner.py] ',DOC.doc_list)
        print('[bp_runner.py] ',len(DOC.doc_list))
        
        for page in DOC.doc_list:
            DRAWABLE.physical.enable()
            DRAWABLE.physical.load_paper()
            DRAWABLE.physical.home() #TODO: Comment me back in (please!)
            curr_x, curr_y = DRAWABLE.physical.current_position()
            content_matrix = page.content
            print('[bp_runner.py] ',np.shape(content_matrix))
            print('[bp_runner.py] ',len(content_matrix))
            print('[bp_runner.py] ',page.page_num)
            

            for row in range(0,len(content_matrix),2):
                print('[bp_runner.py]', 'the top row is: ' + str(row))
                if len(content_matrix) != row+1:
                    DRAWABLE.physical.write_row(content_matrix[row], \
                        content_matrix[row+1], curr_x, curr_y)
                    curr_y += 2 * DRAWABLE.line_spacing + 2 * DRAWABLE.line_height
                    print('[bp_runner.py] ', curr_y)
                else:
                    DRAWABLE.physical.write_row(content_matrix[row], \
                        None, curr_x, curr_y)
            DRAWABLE.physical.unload_paper()
            #FIXME: should this be different to feed the method call?
    else:
        INTERFACE.wait_for_play()

