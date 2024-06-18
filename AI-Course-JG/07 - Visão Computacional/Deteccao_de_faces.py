import cv2

imagem = cv2.imread("workplace-1245776_1920.jpg")

cv2.imshow("Workplace", imagem)

detector_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Workplace grey", imagem_cinza)

deteccoes = detector_face.detectMultiScale(imagem_cinza, scaleFactor=1.3, minSize=(30,30))

for (x, y, l, a) in deteccoes:
  #print(x, y, l, a)
  cv2.rectangle(imagem, (x, y), (x + l, y + a), (0,255,0), 2)
cv2.imshow("Win", imagem)

image = cv2.imread('/content/pessoas.jpg')
cv2.imshow("Win", image)

detector_corpo = cv2.CascadeClassifier('/content/fullbody.xml')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detections = detector_corpo.detectMultiScale(image_gray, scaleFactor=1.1, minSize=(50,50))
print(len(detections))
print(detections)
for (x, y, l, a) in detections:
  cv2.rectangle(image, (x, y), (x + l, y + a), (0,255,0), 2)
cv2.imshow("Win", image)
