file_path = '/home/maia/Documents/School/19-20/PoE/braille-printer/test_story.txt'

def read_text_file(file_path):
    file = open(file_path, 'r')
    text = file.read()
    print(text)
    print("let's see what this does")
    break_up_input(text)

def break_up_input(text):

    for char in text:
        # this is every char in the text sequence


read_text_file(file_path)
