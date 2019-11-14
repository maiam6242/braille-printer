

#This will become the "main" runner class
from text_parse import text_parse
from drawable import drawable
from translator import translator
from document import document
from page import page
from physical import physical
import numpy as np

file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/Text Side/test_story.txt"

parser = text_parse()
segmented = parser.break_up_text_input(parser.read_text_file(file_path))

translator = translator()

formatted = []
total_num_lines = 0

drawable = drawable()
# physical = physical('/dev/ttyACM0')
doc = document()

# drawable.physical.current_position()

# braille_tx, num_lines = translator.convert_to_braille(segmented[-1])
# print(np.shape(segmented[-1][0][0]))
# print(np.size(segmented[-1][0][0]))
for segment in segmented:
    count = 1
    braille_tx, num_lines = translator.convert_to_braille(segment)
    size_in_mm = drawable.size_on_page(num_lines) #[x,y]
    
    locals()['page_'+ str(count)] = page(count)
    n = 'page_'+ str(count)
    print(count)
    print(locals().get(n).page_num)
    
    end_x, end_y = drawable.get_end_position_on_page(size_in_mm)
    print(end_x)
    print(end_y)
    if(drawable.should_split(end_y)):
        splits = drawable.split_line(braille_tx, num_lines, size_in_mm, locals().get(n).lines_written, locals().get(n).lines_per_page)
        print(splits)
        locals().get(n).add_content(splits[0], num_lines)
        count += 1
        doc.add_page_object(locals().get(n))

        locals()['page_'+ str(count)] = page(count)
        n = 'page_'+ str(count)
        locals().get(n).add_content(splits[1], num_lines)
    else:
        locals().get(n).add_content(braille_tx, num_lines)
        print('yooo added, baby!')
    
    #FIXME: PUT THIS IS TERMS OF MM NOT LINES, SHOULD PROBABLY BE IN THE DRAWABLE CLASS?
    if drawable.is_full():
            count += 1
            doc.add_page_object(locals().get(n))


# print(total_num_lines)
# size = translator.size_on_page(total_num_lines)
# print(size)

# drawable.physical.enable()
# for page in doc:
#     drawable.physical.load_paper()
#     drawable.physical.home()
#     curr_x, curr_y = drawable.physical.current_position()
#     content_matrix = page.content
    
#     count = 0

#     drawable.physical.write_row(content_matrix[count], content_matrix[count+3], curr_x, curr_y)

        
        

