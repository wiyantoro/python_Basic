import mysql.connector
from tkinter import *
from tkinter import messagebox
from subprocess import call
import cv2
from simple_facerec import SimpleFacerec
global name

def periksawajah():
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            login(name)
        cv2.imshow("Frame", frame)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    
   
def  login(name):
    mysqldb=mysql.connector.Connect(host="Localhost", user="root",password="",database="latihan")
    mycursor=mysqldb.cursor()
    
    username=name
    #password=entry2.get()
    
    
    sql="select * from login where username= %s "
    mycursor.execute(sql,[(username)])
    result=mycursor.fetchall()
    
    
    if result:
        messagebox.showinfo("","Login Successs")
        root.destroy()
        
        
        return True
    
    else:
        messagebox.showinfo("", "Incorrect username and password")
        return False
    
root=Tk()
root.title("login")
root.geometry("300x200")

global entry1
global entry2

#Label(root,text="username").place(x=20,y=20)
#Label(root,text="password").place(x=20,y=70)

#entry1=Entry(root,bd=5)
#entry1.place(x=140,y=20)

#entry2=Entry(root,bd=5)
#entry2.place(x=140,y=70)

Button(root,text="login",command=periksawajah,height=3,width=13,bd=6).place(x=100,y=120)
root.mainloop()