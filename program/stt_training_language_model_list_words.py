from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL, LANGUAGE_CUSTOMIZATION_ID

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# 登録されている用語の確認
response = stt.list_words(customization_id=LANGUAGE_CUSTOMIZATION_ID, word_type=None, sort=None).get_result()
print(response)

