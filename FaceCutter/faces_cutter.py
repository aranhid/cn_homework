import json
from PIL import Image

imageFileName = input("Enter image filename: ")
jsonFileName = input("Enter json filename: ")

im = Image.open(imageFileName)
with open(jsonFileName, 'r') as f:
    faces = json.load(f)

for face in faces:
    id = face['faceId']
    top, left, width, height = face['faceRectangle'].values()
    im_crop = im.crop((left, top, left+width, top+height))
    im_crop.save('resultImages/' + id + '.jpg')