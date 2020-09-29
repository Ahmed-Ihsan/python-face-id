import face_recognition
import cv2
import numpy as np
import time
import datetime
import os
from PIL import Image,ImageFont,ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

rsl='Face ID'
video_capture = cv2.VideoCapture(0)
    
def make_720p():
    video_capture.set(3,1208)
    video_capture.set(4,720)

dt=datetime.datetime.now()

print(1)
file_name=" "
dt=datetime.datetime.now()
dt2=datetime.datetime(1999,1,13,22,1)
print(dt2)
name2=""
name=""
frame=None

ahmed_image = face_recognition.load_image_file("C:/Users/LE/Pictures/Camera Roll/ahmed.jpg")
ahmed_face_encoding = face_recognition.face_encodings(ahmed_image)[0]

dt=datetime.datetime.now()
print("%100 loading image ")
known_face_encodings = [
    ahmed_face_encoding 
    ]

known_face_names = [
    
    "احمداحسان علي حسين"

    ]

print("%100 loading name ")
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    time_=datetime.datetime.now()
    
    time_1=time.time()
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)    
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)        
            if name in name2 or "احمداحسان علي حسين" not in name :
                break
            dt=datetime.datetime.now()
            name2=name2+"  "+name
        
            print(name)
        fontFile = "C:/Users/LE/Desktop/face/arial.ttf"
        imageFile = "12.jpg"
        font2= ImageFont.truetype(fontFile,20)
        image = Image.open(imageFile)
        text = name
        if "احمداحسان علي حسين" not in name:
         text2 ="كلية الحكمة الجامعة"
         text3 ="Unknown"
         reshaped_text = arabic_reshaper.reshape(text)    
         bidi_text = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text2)    
         bidi_text2 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text3)    
         bidi_text3 = get_display(reshaped_text)
         draw = ImageDraw.Draw(image)
         draw.text((290, 255), bidi_text, (255,0,0), font=font2,)
         draw.text((350, 320), bidi_text2, (255,0,0), font=font2,)
         draw.text((400, 285), bidi_text3, (255,0,0), font=font2,)
         img=np.array(image)
         img=np.array(image)
         img = img[:, :, ::-1].copy()
        else:
         text2 ="my creator"
         text3 ="الثالثة"      
         reshaped_text = arabic_reshaper.reshape(text)    
         bidi_text = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text2)    
         bidi_text2 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text3)    
         bidi_text3 = get_display(reshaped_text)
         draw = ImageDraw.Draw(image)
         draw.text((290, 255), bidi_text, (255,0,0), font=font2,)
         draw.text((350, 320), bidi_text2, (255,0,0), font=font2,)
         draw.text((400, 285), bidi_text3, (255,0,0), font=font2,)
         
         img=np.array(image)
         img = img[:, :, ::-1].copy() 
         ''' img = Image.fromarray(img)
                                 img.show()'''   
    process_this_frame = not process_this_frame
    
    dt=datetime.datetime.now()

    day=dt.strftime("%a")
    #img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    try:
     cv2.imshow("created by Ahmed-Ihsan-Ali",img)
     name="#########################"
    except:
        print(ok)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(20) & 0xFF == ord('a'):
        file_object  = open("add.text", "a")
        r=input("Enter name")
        file_object.write(r+"\n")
        cv2.imwrite("frame.png",frame)
        ahmed_image2 = face_recognition.load_image_file("frame.png")
        ahmed_face_encoding2 = face_recognition.face_encodings(ahmed_image2)[0]
        known_face_encodings.append(ahmed_face_encoding2)
        known_face_names.append(r)

    time_2=time.time()
    print(time_2-time_1)
    

video_capture.release()
cv2.destroyAllWindows()
