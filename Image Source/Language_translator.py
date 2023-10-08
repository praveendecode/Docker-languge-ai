import googletrans

from googletrans import Translator

from googletrans import LANGUAGES

languages = []

for code, name in LANGUAGES.items():
    languages.append({name:code})

print("Languages and thier Codes below\n")

for i in languages:
    print(i)

print()
print()

user_text = input("Provided Text : ")

target_language = input('Provide Your Target Language : ')

translator = Translator()

translated = translator.translate(user_text, dest=target_language)

translated_text = translated.text

print('Converted Text :',translated_text)
