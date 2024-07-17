import cv2
import os
import numpy as np
from PIL import Image
import sqlite3

camera = 0
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r'D:\Kuliah\Semester 6\AI\UAS AI Face\training\training.xml')
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 0.5
fontcolor = (0, 0, 255)
backgroundcolor = (248, 247, 243)
fontthickness = 1

def getProfile(id):
    conn = sqlite3.connect(r'D:\Kuliah\Semester 6\AI\UAS AI Face\store.db')
    cmd = "SELECT * FROM customer WHERE id=" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

def draw_text_with_background(frame, text, x, y, font, scale, color, thickness, bgcolor):
    (text_width, text_height), baseline = cv2.getTextSize(text, font, scale, thickness)
    cv2.rectangle(frame, (x, y - text_height - baseline), (x + text_width, y + baseline), bgcolor, cv2.FILLED)
    cv2.putText(frame, text, (x, y), font, scale, color, thickness)

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        profile = getProfile(id)
        if profile is not None:
            draw_text_with_background(frame, f"Nama: {profile[1]}", x, y + h + 30, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
            draw_text_with_background(frame, f"Usia: {profile[2]} Tahun", x, y + h + 60, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
            draw_text_with_background(frame, f"Jenis Kelamin: {profile[3]}", x, y + h + 90, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
            draw_text_with_background(frame, f"Waktu Kunjungan Terakhir: {profile[4]}", x, y + h + 120, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
            draw_text_with_background(frame, f"Top 3 Produk: {profile[5]}", x, y + h + 150, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
            draw_text_with_background(frame, f"Rekomendasi Produk: {profile[6]}", x, y + h + 180, fontface, fontscale, fontcolor, fontthickness, backgroundcolor)
    cv2.imshow("wajah", frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
