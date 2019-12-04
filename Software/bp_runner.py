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
from Recognizing_Input.select_file import SelectFile

FILE_SELECTOR = SelectFile()

FILE = FILE_SELECTOR.select()




PORT = '/dev/ttyACM0'

#setting up all of the things
SER = serial.Serial(PORT, baudrate=115200, timeout=5)
INTERFACE = Interface(SER)

# FILE_PATH = 'Text_Side/test_story.txt'
FILE_PATH = SelectFile.select_file()
PARSER = Text_Parse()
SEGMENTED = PARSER.break_up_text_input(PARSER.read_text_file(FILE_PATH))

SelectFile.clear(FILE_PATH)



TRANSLATOR = Translator()

FORMATTED = []
TOTAL_NUM_LINES = 0

DRAWABLE = Drawable(SER, INTERFACE)

DOC = Document()

# This loop analyzes the texts as well as places it on various pages
# (and splits text lines accordingly). It places all from one page in a
# page object with that page number associated with it. Once a page is
#  full or if the last segment in the entire array of text is processed,
#  these pages are added to a document object
for segment in SEGMENTED:
    count = 1
    braille_tx, num_lines = TRANSLATOR.convert_to_braille(segment)
    size_in_mm = DRAWABLE.size_on_page(num_lines) #[x,y]

    locals()['page_'+ str(count)] = Page(count)
    n = 'page_'+ str(count)
    print(count)
    print(locals().get(n).page_num)

    end_x, end_y = DRAWABLE.get_end_position_on_page(size_in_mm)
    print(end_x)
    print(end_y)

    if DRAWABLE.should_split(end_y):
        splits = DRAWABLE.split_line(braille_tx, num_lines)
        print(splits)
        locals().get(n).add_content(splits[0], splits[1])
        count += 1
        DOC.add_page_object(locals().get(n))

        DRAWABLE.position_on_page = 0
        locals()['page_'+ str(count)] = Page(count)
        n = 'page_'+ str(count)
        locals().get(n).add_content(splits[2], splits[3])
    else:
        locals().get(n).add_content(braille_tx, num_lines)
        print('yooo added, baby!')

        #TODO: Check these measurements! This should be 25 lines, right now, with measurements. it is only 20...
        if DRAWABLE.is_full():
            count += 1
            DRAWABLE.position_on_page = 0
            DOC.add_page_object(locals().get(n))

    # TODO: Test me!
        if(DOC.num_pages != count and segment is SEGMENTED[-1]):
            DOC.add_page_object(locals().get(n))


# drawable.physical.disable()
print(DOC.num_pages)

# This loop handles the actual punching of the characters. 
# It waits for interface feedback at each step in the process
#  (most of this logic is contained in the actual methods of the physical class)

#FIXME: Get this working with the interface!
#TODO: Test this logic, wrapped the if and else differently
if not INTERFACE.is_start_print():
    INTERFACE.wait_for_print()
else:
    while not INTERFACE.is_cancel():
        print('did we get here')
        if INTERFACE.is_play_pause():
            print('how about here')
            for page in DOC.doc_list:
                DRAWABLE.physical.enable()
                DRAWABLE.physical.load_paper()
                DRAWABLE.physical.home() #TODO: Comment me back in (please!)
                curr_x, curr_y = DRAWABLE.physical.current_position()
                content_matrix = page.content
                print(page.page_num)

                for row in range(0,len(content_matrix),2):
                    print('the top row is: ' + str(row))
                    DRAWABLE.physical.write_row(content_matrix[row], \
                        content_matrix[row+1], curr_x, curr_y)
                    curr_y += 2 * DRAWABLE.line_spacing + 2 * DRAWABLE.line_height
                    print(curr_y)
            #FIXME: should this be different to feed the method call?
        else:
            INTERFACE.wait_for_play()
#within while loop
#if not interface.is_play_pause():
    #code to make things pause
    #stop motors
    #stop solenoids
    #pause internal printing functions
#if interface.is_cancel():
    #code to cancel things entirely
    #stop motors
    #stop solenoids
    #stop internal printing functions
    #reset any internal progress
    #roll out paper? is this a possibility?
