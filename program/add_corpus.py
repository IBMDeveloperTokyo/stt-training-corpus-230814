from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from config import STT_APIKEY, STT_URL, LANGUAGE_CUSTOMIZATION_ID

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# コーパスによるトレーニング
with open('corpus/ai_corpus_summary.txt','r',encoding="utf-8") as corpus_file:
    stt.add_corpus(
        customization_id=LANGUAGE_CUSTOMIZATION_ID, 
        corpus_name='My corpus',
        corpus_file=corpus_file,
        allow_overwrite=True).get_result()