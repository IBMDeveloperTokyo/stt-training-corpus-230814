from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# カスタム言語モデルの作成
language_model = stt.create_language_model(
    name="Custom Language Model for Contest",
    base_model_name="ja-JP_BroadbandModel",
    description="A custom language model for Contest"
)
print("customization_id : " + language_model.get_result()['customization_id'])