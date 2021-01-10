import requests

filename = input("Enter file name: ")

key = "1db01788ad86488d90d573a7fe502c11 "
auth_url = "https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issueToken"
lang_url = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/voices/list"
tts_url = "https://eastasia.tts.speech.microsoft.com/cognitiveservices/v1"

auth_headers = { "Ocp-Apim-Subscription-Key": key, "Content-Length": "0", "Content-type": "application/x-www-form-urlencoded" }
auth_response = requests.post(auth_url, headers=auth_headers)
token = auth_response.text
print(token)

lang_headers= { "Authorization": "Bearer " + token }
lang_response = requests.get(lang_url, headers=lang_headers)
json_langs = lang_response.json()

for index, line in enumerate(json_langs):
    print(index, ".", line)

dictorId = int(input("Select dictor: "))
dictor = json_langs[dictorId]

tts_headers = {
    "Authorization": "Bearer " + token,
    "X-Microsoft-OutputFormat": "audio-24khz-160kbitrate-mono-mp3",
    "Content-Type": "application/ssml+xml",
    "Content-Length": "225",
}

with open(filename, mode="r", encoding='utf-8') as input_text:
    text = input_text.read()

tts_data = "<speak version='1.0' xml:lang='" + dictor["Locale"] + "'><voice xml:lang='" + dictor["Locale"] + "' xml:gender='" + dictor["Gender"] + "' name='" + dictor["ShortName"] + "'> " + text + " </voice></speak>"

tts_response = requests.post(tts_url, data=tts_data.encode('utf-8'), headers=tts_headers, stream=True)

with open(filename + ".mp3", "wb") as output_file:
    for chunk in tts_response.iter_content(chunk_size=128):
        output_file.write(chunk)