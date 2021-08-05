import googletrans
from googletrans import Translator
class Language_Translator:
    def trans_word(self):
        translator = Translator()
        i= input("Enter the language of the word : ")
        j= input("Enter the language to be translated : ")
        word=input("Enter the word to be translated: ")
        output= translator.translate(word, src=i , dest=j)
        print("Translated word :", output.text)
    def trans_text(self):
        translator = Translator()
        i= input("Enter the language of the sentence : ")
        j= input("Enter the language to be translated : ")
        text =input("Enter the text to be translated: ")
        output= translator.translate(text, src=i , dest=j)
        print("Translated text :",output.text)
    def trans_paragraph(self):
        translator = Translator()
        i= input("Enter the language in which paragraph is written : ")
        j= input("Enter the language to be translated : ")
        paragraph =input("Enter the paragraph to be translated: ")
        output = translator.translate(paragraph, src=i , dest=j)
        print("Translated paragraph :",output.text)
L= Language_Translator()
print("                       $$**********\033[1m"+"Welcome to Language Translator"+"\033[0m""*********$$")
print("\nAvailable Languages For Conversion :\n\n", googletrans.LANGUAGES.values() )
print("\nAvailable Options :\n \n1.Word Translation\n2.Text Translation\n3.Paragraph Translation\n4.Exit\n")

while True:
    choice=int(input("Enter the function to be performed: "))
    if choice==1:
        L.trans_word()
        print("------------------------------------------------")
    if choice==2:
        L.trans_text()
        print("------------------------------------------------")
    if choice==3:
        L.trans_paragraph()
        print("------------------------------------------------")
    if choice==4:
        break
