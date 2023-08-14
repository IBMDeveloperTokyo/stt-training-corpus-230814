from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL, LANGUAGE_CUSTOMIZATION_ID

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# トレーニングステータスの取得
response = stt.get_language_model(customization_id=LANGUAGE_CUSTOMIZATION_ID).get_result()

print(response)

