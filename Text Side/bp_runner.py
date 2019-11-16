

#This will become the "main" runner class
from text_parse import Text_Parse
from drawable import Drawable
from translator import Translator
from document import Document
from page import Page
from physical import Physical
import numpy as np

file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/Text Side/test_story.txt"
port = '/dev/ttyACM0'

parser = Text_Parse()
segmented = parser.break_up_text_input(parser.read_text_file(file_path))

translator = Translator()

formatted = []
total_num_lines = 0

drawable = Drawable(port)
# physical = physical('/dev/ttyACM0')
doc = Document()

# drawable.physical.current_position()

# braille_tx, num_lines = translator.convert_to_braille(segmented[-1])
# print(np.shape(segmented[-1][0][0]))
# print(np.size(segmented[-1][0][0]))
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
        
        if drawable.is_full():
            count += 1
            drawable.position_on_page = 0
            doc.add_page_object(locals().get(n))


# FIXME: Enable instead of disable when ready to use
drawable.physical.disable()
print(doc.num_pages)
# print(doc.doc[0].content)

for page in doc.doc_list:
    drawable.physical.load_paper()
    # drawable.physical.home() #TODO: Comment me back in (please!)
    curr_x, curr_y = drawable.physical.current_position()
    content_matrix = page.content
    # print(content_matrix)
    count = 0
    #FIXME: this line is wrong!
    drawable.physical.write_row(content_matrix[count], content_matrix[count+3], curr_x, curr_y)

        
        

