from translate import Translator
from tkinter import filedialog, simpledialog

# Select a file to translate
input_file = filedialog.askopenfile(mode="r", title="Select a text file to translate", filetypes=[("text file", "*.txt")])
if input_file:
    input_text = input_file.read()
# Select a language
language = simpledialog.askstring("Translator", "Select language code (ISO 639-1)")
translator = Translator(to_lang=language)

# Translate text
translation = translator.translate(input_text)

# Write to new file
with open(input_file.name.removesuffix(".txt") + "_translated_" + language + ".txt", "w") as output_file:
    output_file.write(translation)