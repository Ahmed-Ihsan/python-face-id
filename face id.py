import face_recognition
import cv2
import numpy as np
import time
import datetime
import os
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from PIL import Image,ImageFont,ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display

rsl=''
video_capture = cv2.VideoCapture(0)
name=""


def send_email():
 try: 
     subject = "Hi Ahmed"
     body = "created by ahmed ihsan ali"
     sender_email = ""
     receiver_email = ""
     password = ""

     message = MIMEMultipart()
     message["From"] = sender_email
     message["To"] = receiver_email
     message["Subject"] = subject
     message["Bcc"] = receiver_email 
     message.attach(MIMEText(body, "plain"))

     filename = "//home//pi//Desktop//ahmed_ihsan//save file for script//"+rsl+"-"+file_name+"-"+str(dt.day)+".text"
     with open(filename, "rb") as attachment:
         part = MIMEBase("application", "octet-stream")
         part.set_payload(attachment.read())
   
     encoders.encode_base64(part)

     part.add_header(
     "Content-Disposition",
     f"attachment; filename= {filename}",
      )

     message.attach(part)
     text = message.as_string()
     context = ssl.create_default_context()
     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email,text)
          server.quit()
     print("send email %100")
     agin="ss"
     return agin
 except:
     print("is not connected or is not time for start")
     agin="there is error"
     return agin

    
def make_720p():
    video_capture.set(3,1208)
    video_capture.set(4,720)

dt=datetime.datetime.now()
day=dt.strftime("%a")
print(day)
file_name=" "
dt=datetime.datetime.now()
dt2=datetime.datetime(1999,1,13,22,dt.minute)
print(dt,"        ",dt2)
name2=""

ahmed_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//ahmed.jpg")
ahmed_face_encoding = face_recognition.face_encodings(ahmed_image)[0]
print(4)
AMD_4709_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4709.jpg")
AMD_4709_face_encoding = face_recognition.face_encodings(AMD_4709_image)[0]
print(4*2)
AMD_4710_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4710.jpg")
AMD_4710_face_encoding = face_recognition.face_encodings(ahmed_image)[0]
print(4*3)
AMD_4711_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4711.jpg")
AMD_4711_face_encoding = face_recognition.face_encodings(AMD_4711_image)[0]
print(4*4)
AMD_4712_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4712.jpg")
AMD_4712_face_encoding = face_recognition.face_encodings(AMD_4712_image)[0]
print(4*5)
AMD_4713_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4713.jpg")
AMD_4713_face_encoding = face_recognition.face_encodings(AMD_4713_image)[0]
print(4*6)
AMD_4714_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4714.jpg")
AMD_4714_face_encoding = face_recognition.face_encodings(AMD_4714_image)[0]
print(4*7)
AMD_4715_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4715.jpg")
AMD_4715_face_encoding = face_recognition.face_encodings(AMD_4715_image)[0]
print(4*8)
AMD_4716_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4716.jpg")
AMD_4716_face_encoding = face_recognition.face_encodings(AMD_4716_image)[0]
print(4*9)
AMD_4717_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4717.jpg")
AMD_4717_face_encoding = face_recognition.face_encodings(AMD_4717_image)[0]
print(4*10)
AMD_4718_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4718.jpg")
AMD_4718_face_encoding = face_recognition.face_encodings(AMD_4718_image)[0]
print(4*11)
AMD_4719_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4719.jpg")
AMD_4719_face_encoding = face_recognition.face_encodings(AMD_4719_image)[0]
print(4*12)
AMD_4720_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4720.jpg")
AMD_4720_face_encoding = face_recognition.face_encodings(AMD_4720_image)[0]
print(4*13)
AMD_4721_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4721.jpg")
AMD_4721_face_encoding = face_recognition.face_encodings(AMD_4721_image)[0]
print(4*14)
AMD_4722_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4722.jpg")
AMD_4722_face_encoding = face_recognition.face_encodings(AMD_4722_image)[0]
print(4*15)
AMD_4723_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4723.jpg")
AMD_4723_face_encoding = face_recognition.face_encodings(AMD_4723_image)[0]
print(4*16)
AMD_4724_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4724.jpg")
AMD_4724_face_encoding = face_recognition.face_encodings(AMD_4724_image)[0]
print(4*17)
AMD_4725_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4725.jpg")
AMD_4725_face_encoding = face_recognition.face_encodings(AMD_4725_image)[0]
print(4*18)
AMD_4726_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4726.jpg")
AMD_4726_face_encoding = face_recognition.face_encodings(AMD_4726_image)[0]
print(4*19)
AMD_4727_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4727.jpg")
AMD_4727_face_encoding = face_recognition.face_encodings(AMD_4727_image)[0]
print(4*20)
AMD_4728_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4728.jpg")
AMD_4728_face_encoding = face_recognition.face_encodings(AMD_4728_image)[0]
print(4*21)
AMD_4729_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4729.jpg")
AMD_4729_face_encoding = face_recognition.face_encodings(AMD_4728_image)[0]
print(4*22)
AMD_4730_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_47230.jpg")
AMD_4730_face_encoding = face_recognition.face_encodings(AMD_4730_image)[0]
print(4*22)
AMD_4731_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4731.jpg")
AMD_4731_face_encoding = face_recognition.face_encodings(AMD_4731_image)[0]
print(4*23)
AMD_4732_image = face_recognition.load_image_file("//home//pi//Desktop//ahmed_ihsan//image for script//AMD_4732.jpg")
AMD_4732_face_encoding = face_recognition.face_encodings(AMD_4732_image)[0]
print(100)
dt=datetime.datetime.now()
print("%100 loading image ",dt)
known_face_encodings = [
    ahmed_face_encoding,
    AMD_4709_face_encoding,
    AMD_4710_face_encoding,
    AMD_4711_face_encoding,
    AMD_4712_face_encoding,
    AMD_4713_face_encoding,
    AMD_4714_face_encoding,
    AMD_4715_face_encoding,
    AMD_4716_face_encoding,
    AMD_4717_face_encoding,
    AMD_4718_face_encoding,
    AMD_4719_face_encoding,
    AMD_4720_face_encoding,
    AMD_4721_face_encoding,
    AMD_4722_face_encoding,
    AMD_4723_face_encoding,
    AMD_4724_face_encoding,
    AMD_4725_face_encoding,
    AMD_4726_face_encoding,
    AMD_4727_face_encoding,
    AMD_4728_face_encoding,
    AMD_4729_face_encoding,
    AMD_4730_face_encoding,
    AMD_4731_face_encoding,
    AMD_4732_face_encoding,
    ]

known_face_names = [
    
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
    "Unknown",
]
print("%100 loading name ",dt)
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
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
            if name in name2:
                break
            dt=datetime.datetime.now()
            file_2=open('//home//pi//Desktop//ahmed_ihsan//save file for script//'+rsl+"-"+file_name+"-"+str(dt.day)+".text","a")
            file_2.writelines(name+"  "+file_name+"   "+str(dt.year)+"/"+str(dt.month)+"/"+str(dt.day)+"  "+str(dt.hour)+":"+str(dt.minute)+'\n')
            name2=name2+"  "+name
            file_2.close()

        fontFile = "//home//pi//Desktop//ahmed_ihsan//font for script//arial.ttf"
        imageFile = "//home//pi//Desktop//ahmed_ihsan//image for script//k.h.g_800.jpg"
        font2= ImageFont.truetype(fontFile,20)
        image = Image.open(imageFile)
        text =name
        if "....." not in name:
         text2 ="......"
         text3 ="......"
         text4 =str(dt.year)+"/"+str(dt.month)+"/"+str(dt.day)+"  "+str(dt.hour)+":"+str(dt.minute)        
         reshaped_text = arabic_reshaper.reshape(text)    
         bidi_text = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text2)    
         bidi_text2 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text3)    
         bidi_text3 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text4)    
         bidi_text4 = get_display(reshaped_text)
         draw = ImageDraw.Draw(image)
         draw.text((290, 255), bidi_text, (255,0,0), font=font2,)
         draw.text((350, 320), bidi_text2, (255,0,0), font=font2,)
         draw.text((400, 285), bidi_text3, (255,0,0), font=font2,)
         draw.text((650, 390), bidi_text4, (255,0,0), font=font2,)
         img=np.array(image)
        else:
         text2 ="my creator"
         text3 ="......"
         text4 =str(dt.year)+"/"+str(dt.month)+"/"+str(dt.day)+"  "+str(dt.hour)+":"+str(dt.minute)        
         reshaped_text = arabic_reshaper.reshape(text)    
         bidi_text = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text2)    
         bidi_text2 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text3)    
         bidi_text3 = get_display(reshaped_text)
         reshaped_text = arabic_reshaper.reshape(text4)    
         bidi_text4 = get_display(reshaped_text)
         draw = ImageDraw.Draw(image)
         draw.text((290, 255), bidi_text, (255,0,0), font=font2,)
         draw.text((350, 320), bidi_text2, (255,0,0), font=font2,)
         draw.text((400, 285), bidi_text3, (255,0,0), font=font2,)
         draw.text((650, 390), bidi_text4, (255,0,0), font=font2,)
         img=np.array(image)
       
      
    process_this_frame = not process_this_frame
    
    dt=datetime.datetime.now()
    
    day=dt.strftime("%a")
    
    if "Sat" in day:
        stude_time=datetime.datetime.now()
        start_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,8,29)
        end_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,9,28)
        if stude_time>start_stude_time and stude_time<end_stude_time:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,9,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
          dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
          dt_1=datetime.datetime(dt.year,dt.month,dt.day,9,29)
          dt=datetime.datetime.now()
          if "there is error" in agin or "go" in agin :
            agin=send_email()
            send_email()
            name2=""
          time.sleep(1)
                
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,9,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,30)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,9,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,15,00)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
         dt1=datetime.datetime(dt.year,dt.month,dt.day,9,45)
         dt_1=datetime.datetime(dt.year,dt.month,dt.day,15,00)
         dt=datetime.datetime.now()
         if "there is error" in agin or "go" in agin :
           send_email()
           agin=send_email()
           name2=""
         time.sleep(1)

    if "Sun" in day:
        
        stude_time=datetime.datetime.now()
        start_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,8,29)
        end_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,00)
        if stude_time>start_stude_time and stude_time<end_stude_time:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,10,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
          dt=datetime.datetime.now()
          if "there is error" in agin or "go" in agin :
            send_email()
            agin=send_email()
            name2=""
          time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,28)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,10,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,11,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
          dt=datetime.datetime.now()
          if "there is error" in agin or "go" in agin :
            send_email()
            agin=send_email()
            name2=""
          time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,28)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,11,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,12,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        start_stude_time_3=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,29)
        end_stude_time_3=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,14,30)
        if stude_time>start_stude_time_3 and stude_time<end_stude_time_3:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,12,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,14,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
                send_email()
                agin=send_email()
                name2=""
            time.sleep(1)

    if "Mon" in day:
        stude_time=datetime.datetime.now()
        start_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,8,29)
        end_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,9,28)
        if stude_time>start_stude_time and stude_time<end_stude_time:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,9,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,9,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,30)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,9,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,15,00)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)

    if "Tue" in day:
        stude_time=datetime.datetime.now()
        start_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,8,29)
        end_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,00)
        if stude_time>start_stude_time and stude_time<end_stude_time:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,10,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              print(agin)
              name2=""
            time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,28)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,10,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,11,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              print(agin)
              name2=""
            time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,30)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,11,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,15,00)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              print(agin)
              name2=""
            time.sleep(1)

    if "Wed" in day:
        stude_time=datetime.datetime.now()
        start_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,8,29)
        end_stude_time=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,00)
        if stude_time>start_stude_time and stude_time<end_stude_time:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,8,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,10,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        start_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,10,29)
        end_stude_time_2=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,28)
        if stude_time>start_stude_time_2 and stude_time<end_stude_time_2:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,10,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,11,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        start_stude_time_4=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,11,29)
        end_stude_time_4=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,28)
        if stude_time>start_stude_time_4 and stude_time<end_stude_time_4:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,11,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,12,29)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        start_stude_time_5=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,12,29)
        end_stude_time_5=datetime.datetime(stude_time.year,stude_time.month,stude_time.day,14,30)
        if stude_time>start_stude_time_5 and stude_time<end_stude_time_5:
            file_name="....."
        dt1=datetime.datetime(dt.year,dt.month,dt.day,12,45)
        dt_1=datetime.datetime(dt.year,dt.month,dt.day,15,00)
        dt=datetime.datetime.now()
        agin="go"
        while dt>dt1 and dt<dt_1:
            dt=datetime.datetime.now()
            if "there is error" in agin or "go" in agin :
              send_email()
              agin=send_email()
              name2=""
            time.sleep(1)
        
    
    
    dt=datetime.datetime.now()
    day=dt.strftime("%a")
    try:
     cv2.imshow("created by Ahmed-Ihsan-Ali",img)
     name="**************"
    except:
        print(ok)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    time_2=time.time() 
    
    dt1=datetime.datetime(dt.year,dt.month,dt.day,8,29)
    dt=datetime.datetime.now()
    while dt<dt1:
        dt=datetime.datetime.now()
    print(time_2-time_1)
    

video_capture.release()
cv2.destroyAllWindows()
