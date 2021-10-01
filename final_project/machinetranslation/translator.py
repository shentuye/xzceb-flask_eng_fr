"""This is a module to translate the text from en to fr and from fr to en via IBM Watson"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
VERSION='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION,authenticator=authenticator)
language_translator.set_service_url(url)
def english_to_french(english_text):
    """
    input: english text in string
    output: french text in string
    """
    if english_text != "":
        translation_response = language_translator.translate(\
        text=english_text, model_id='en-fr')
        translate_result = translation_response.get_result()
        french_text = translate_result["translations"][0]["translation"]
    else:
        french_text = ""
    return french_text
def french_to_english(french_text):
    """
    input: french text in string
    output: english text in string
    """
    if french_text != "":
        translation_response = language_translator.translate(\
        text=french_text, model_id='fr-en')
        translate_result = translation_response.get_result()
        english_text = translate_result["translations"][0]["translation"]
    else:
        english_text = ""
    return english_text
print(french_to_english(""))
