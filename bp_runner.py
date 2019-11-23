# This will become the "main" runner class

from Text_Side.text_parse import Text_Parse
from Text_Side.drawable import Drawable
from Text_Side.translator import Translator
from Text_Side.document import Document
from Text_Side.page import Page
from Interface.interface import Interface
from Text_Side.physical import Physical
# importlib.import_module('./braille-printer/Interface', package=None)
import numpy as np


file_path = 'Text_Side/test_story.txt'
port = '/dev/ttyACM0'

interface = Interface()
parser = Text_Parse()
segmented = parser.break_up_text_input(parser.read_text_file(file_path))

translator = Translator()

formatted = []
total_num_lines = 0

drawable = Drawable(port)

doc = Document()

print(np.shape(segmented))
for segment in segmented:
    count = 1
    braille_tx, num_lines = translator.convert_to_braille(segment)
    size_in_mm = drawable.size_on_page(num_lines) #[x,y]

    locals()['page_'+ str(count)] = Page(count)
    n = 'page_'+ str(count)
    print(count)
    print(locals().get(n).page_num)

    end_x, end_y = drawable.get_end_position_on_page(size_in_mm)
    print(end_x)
    print(end_y)

    if(drawable.should_split(end_y)):
        splits = drawable.split_line(braille_tx, num_lines)
        print(splits)
        locals().get(n).add_content(splits[0], splits[1])
        count += 1
        doc.add_page_object(locals().get(n))

        drawable.position_on_page = 0
        locals()['page_'+ str(count)] = Page(count)
        n = 'page_'+ str(count)
        locals().get(n).add_content(splits[2], splits[3])
    else:
        locals().get(n).add_content(braille_tx, num_lines)
        print('yooo added, baby!')

        #TODO: Check these measurements! This should be 25 lines, right now, with measurements. it is only 20...
        if drawable.is_full():
            count += 1
            drawable.position_on_page = 0
            doc.add_page_object(locals().get(n))
    #TODO: Make it so that the last page is also added, if all the other pages are full and this loop is done, add the last page basically
    # TODO: Test me!
        if(doc.num_pages != count and segment is segmented[-1]):
            doc.add_page_object(locals().get(n))




# FIXME: Enable instead of disable when ready to use
# drawable.physical.disable()
print(doc.num_pages)

#TODO: Test with interface!
interface.wait_for_print()
if(interface.is_start_print()):
    while(interface.is_play_pause() and not interface.is_cancel()):
        for page in doc.doc_list:
            drawable.physical.enable()
            drawable.physical.load_paper()
            drawable.physical.home() #TODO: Comment me back in (please!)
            curr_x, curr_y = drawable.physical.current_position()
            content_matrix = page.content
            print(page.page_num)

            for row in range(0,len(content_matrix),2):
                print('the top row is: ' + str(row))
                drawable.physical.write_row(content_matrix[row], content_matrix[row+1], curr_x, curr_y)
                curr_y += 2 * drawable.line_spacing + 2 * drawable.line_height
                print(curr_y)
            #FIXME: should this be different to feed the method call?
    # if (interface.is_cancel())
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
