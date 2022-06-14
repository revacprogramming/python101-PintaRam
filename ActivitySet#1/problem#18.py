from googletrans import Translator
translate = Translator()
text = input("enter your text")
ttext = translator.translate(text , dest = "hindi")
print(ttext.text)
from googletrans import translator