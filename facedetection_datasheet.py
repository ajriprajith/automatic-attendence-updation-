import cv2
import os

def crt_facerecognition(name):
    dataset = r"face detection\dataset"  #change directory 
    path = os.path.join(dataset,name) #dataset/champ
    if not os.path.isdir(path):
        os.mkdir(path)
    (width,height)=(130,100)
    alg =r"face detection\haarcascade_frontalface_default.xml"   #change directory
    haar_cascade = cv2.CascadeClassifier(alg)

    cam = cv2.VideoCapture(0) 

    count=1
    while count<100:
        print(count)
        _,img = cam.read()
        grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        face=haar_cascade.detectMultiScale(grayImg,1.3, 4)
        for(x,y,w,h) in face:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            faceOnly = grayImg[y:y+h,x:x+w]
            resizeImg=cv2.resize(faceOnly,(width,height))
            cv2.imwrite("%s/%s.jpg" %(path,count),resizeImg)
            count+=1
        cv2.imshow("FaceDetection",img)
        key=cv2.waitKey(10)

        if key == 27:
            break
    print("Image Captured Successfully",img)
    cam.release()
    cv2.destroyAllWindows()
                
if __name__ == '__main__':
    name=input("Enter the name ")
    crt_facerecognition(name)