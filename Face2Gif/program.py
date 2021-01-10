from PIL import Image
import requests
import cv2
import io

KEY = 'f12693bc12c7479d829a57734f145e24'
API_URL = 'https://westeurope.api.cognitive.microsoft.com'

def recognize_face(frame):
    url = API_URL + '/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&recognitionModel=recognition_03&detectionModel=detection_02'
    
    image = Image.fromarray(frame)
    output = io.BytesIO()
    image.save(output, format='JPEG')
    hex_data = output.getvalue()

    headers = {
        'Ocp-Apim-Subscription-Key': KEY,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(url, data=hex_data, headers=headers)

    face_frame = response.json()[0]['faceRectangle']
    return face_frame

cap = cv2.VideoCapture('video.mp4')
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count)
frame_number = 0

width = 0
height = 0

selectedFrames = []
currentStep = 0
frameStep = 15
selectedFramesCount = 0
maxSelectedFrames = 20

while frame_number <= frame_count:
    ret, frame = cap.read()
    frame_number += 1

    if (selectedFramesCount < maxSelectedFrames):
        if (currentStep == frameStep):
            selectedFramesCount += 1
            currentStep = 0
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            try:
                face_frame = recognize_face(frame)
                if width == 0:
                    width = face_frame['width'] * 2
                    height = face_frame['height'] * 2
                x = face_frame['left'] - width // 4
                y = face_frame['top'] - height // 4
                recognizedFace = Image.fromarray(frame[y : y + height, x : x + width])
            except:
                continue

            selectedFrames.append(recognizedFace)
        else:
            currentStep += 1
    else:
        break

cap.release()
selectedFrames[0].save('animation.gif', save_all=True, append_images=selectedFrames[1:], optimize=False, loop=0)
selectedFrames1 = selectedFrames.copy()
selectedFrames1.reverse()
for frame in selectedFrames1:
    selectedFrames.append(frame)
selectedFrames[0].save('animation_with_reverse.gif', save_all=True, append_images=selectedFrames[1:], optimize=False, loop=0)