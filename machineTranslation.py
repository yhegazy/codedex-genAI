from translate import Translator
translator = Translator(to_lang='ar')  # Arabic
# Text to be translated
text = 'Hello Beautiful, how are you?'    

# Perform the translation
translation = translator.translate(text)
# Print the translated text
print(translation)  # Output: مرحبا كيف حالك؟
