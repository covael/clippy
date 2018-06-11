import re
import pyperclip

text_input = input('Insert copy text here: ')

pyperclip.copy(text_input)

paste = pyperclip.paste()

print (paste)
                       
                       
