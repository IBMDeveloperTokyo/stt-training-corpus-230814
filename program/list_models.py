from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# 現在のカスタム言語モデルのリストを表示する
response = stt.list_language_models(language=None).get_result()
print(response)

