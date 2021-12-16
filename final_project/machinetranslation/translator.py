# import json
import os
from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# """
# translator.py connects to ibm_watson
# language translator and converts English
# to French and vice versa using functions
# frenchToEnglish and englishToFrench
# """

load_dotenv('.env')

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    translate English to French
    """
    if english_text is None:
        raise ValueError("Please enter a valid text in English")
    else:
        #write the code here
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']
        # print(json.dumps(translation, indent=2, ensure_ascii=False))
        return french_text
        

def frenchToEnglish(french_text):
    """
    translate French to English
    """
    if french_text is None:
        raise ValueError("Please enter a valid text in French")
    else:
        #write the code here
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
        # print(json.dumps(translation, indent=2, ensure_ascii=False))
        return english_text
    