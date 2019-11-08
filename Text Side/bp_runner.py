#This will become the "main" runner class
from text_parse import text_parse
import drawable
from translator import translator
import document
from page import page

file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/Text Side/test_story.txt"

parser = text_parse()
segmented = parser.break_up_text_input(parser.read_text_file(file_path))

translator = translator()

formatted = []
total_num_lines = 0

for segment in segmented:
    count = 1
    braille_tx, num_lines = translator.convert_to_braille(segment)
    size = translator.size_on_page(num_lines)

    locals()['page_'+ str(count)] = page(count)
    n = 'page_'+ str(count)
    print(count)
    print(locals().get(n).page_num)
    

    formatted.append(braille_tx)
    total_num_lines += num_lines


# print(total_num_lines)
# size = translator.size_on_page(total_num_lines)
# print(size)

# drawable = drawable()
# drawable.get_position_on_page()


