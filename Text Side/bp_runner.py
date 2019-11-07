#This will become the "main" runner class
from text_parse import text_parse
import drawable
from translator import translator
import document
import page

file_path = "/home/maia/Documents/School/19-20/PoE/braille-printer/Text Side/test_story.txt"

parser = text_parse()
segmented = parser.break_up_text_input(parser.read_text_file(file_path))

translator = translator()

formatted = []
total_num_lines = 0

for segment in segmented:
    br_tx, num_lines = translator.convert_to_braille(segment)
    formatted.append(br_tx)
    total_num_lines += num_lines

print(total_num_lines)
size = translator.size_on_page(total_num_lines)
print(size)
