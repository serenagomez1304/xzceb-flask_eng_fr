import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-01-11',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    if len(english_text) == 0:
        return ''
    french_json = language_translator.translate(text=english_text, source='en', target='fr-CA')
    french_text = french_json.get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    #write the code here
    if len(french_text) == 0:
        return ''
    english_json = language_translator.translate(text=french_text, source='fr-CA', target='en')
    english_text = english_json.get_result()
    return english_text['translations'][0]['translation']
