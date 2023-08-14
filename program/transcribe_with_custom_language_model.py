from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import datetime
from config import STT_APIKEY, STT_URL, LANGUAGE_CUSTOMIZATION_ID

# IBM Watson Speech to Textサービスの設定
stt_authenticator = IAMAuthenticator(STT_APIKEY)
stt = SpeechToTextV1(authenticator=stt_authenticator)
stt.set_service_url(STT_URL)

# 音声ファイルの指定
audio_name = "./wav/ai_wikipedia.wav"

# タイムスタンプの生成
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

# 音声をテキストに変換する
with open(audio_name, 'rb') as audio_file:
    result = stt.recognize(
        audio=audio_file,
        content_type='audio/wav',
        model='ja-JP_Multimedia', # 標準モデルの使用
        language_customization_id=LANGUAGE_CUSTOMIZATION_ID, # カスタムモデルの使用
        speaker_labels=True,
        ).get_result()

# debug
print(result)

# テキストをファイルに保存する
transcript_name = f"./transcript/transcript_{timestamp}.txt"
transcripts = []
for item in result['results']:
    transcripts.append(item['alternatives'][0]['transcript'])

formatted_transcript = ' '.join(transcripts).replace(' ', '')  # スペースで区切られた単語を連結

with open(transcript_name, 'w') as f:
    f.write(formatted_transcript)
    