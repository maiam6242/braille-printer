file_path = '/home/maia/Documents/School/19-20/PoE/braille-printer/test_story.txt'

def read_text_file(file_path):
    file = open(file_path)
    text = file.read()
    print(text)

read_text_file(file_path)