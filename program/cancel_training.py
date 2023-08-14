from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL, LANGUAGE_CUSTOMIZATION_ID

stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# トレーニングのキャンセル
response = stt.reset_language_model(LANGUAGE_CUSTOMIZATION_ID)

print(response.get_result())
