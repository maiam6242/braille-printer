# This will become the "main" runner class
from text_parse import Text_Parse
from drawable import Drawable
from translator import Translator
from document import Document
from page import Page
from physical import Physical
import numpy as np

file_path = '/home/maia/Documents/School/19-20/PoE/braille-printer/Text Side/test_story.txt'
port = '/dev/ttyACM0'

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

for page in doc.doc_list:
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
        

