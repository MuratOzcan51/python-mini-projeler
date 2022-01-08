from translate import Translator

while True:
    translator= Translator(from_lang="turkish",to_lang="english")
    x= input("Bir Kelime girin:  ")
    print("İnglizcesi ...... \n ")
    if(x=="q"):
        break
    translation = translator.translate(x)
    print(translation)
    