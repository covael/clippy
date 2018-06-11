import pyperclip

text_input = raw_input('Insert copy text here: ')

pyperclip.copy(text_input)

paste = pyperclip.paste()

print (paste)
                       
                       
