import numpy as np
import cv2
import os

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized



class CFEVideoConf(object):
    STD_DIMENSIONS =  {
        "360p": (480, 360),
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    VIDEO_TYPE = {
        'avi': cv2.VideoWriter_fourcc(*'XVID'),
        'mp4': cv2.VideoWriter_fourcc(*'XVID'),
    }

    width           = 640
    height          = 480
    dims            = (640, 480)
    capture         = None
    video_type      = None
    def __init__(self, capture, filepath, res="480p", *args, **kwargs):
        self.capture = capture
        self.filepath = filepath
        self.width, self.height = self.get_dims(res=res)
        self.video_type = self.get_video_type()

    def change_res(self, width, height):
        self.capture.set(3, width)
        self.capture.set(4, height)

    def get_dims(self, res='480p'):
        width, height = self.STD_DIMENSIONS['480p']
        if res in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[res]
        self.change_res(width, height)
        self.dims = (width, height)
        return width, height

    def get_video_type(self):
        filename, ext = os.path.splitext(self.filepath)
        if ext in self.VIDEO_TYPE:
          return  self.VIDEO_TYPE[ext]
        return self.VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)

save_path           = './my1stvid.mp4'
frames_per_seconds  = 24
config              = CFEVideoConf(cap, filepath=save_path, res='720p')
out                 = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)
face_cascade        = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade        = cv2.CascadeClassifier('haarcascade_eye.xml')
nose_cascade        = cv2.CascadeClassifier('Nose18x15.xml')
mustache            = cv2.imread('mustache.png',-1)


while(True):
    ret, frame = cap.read()
    gray            = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces           = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    for (x, y, w, h) in faces:
        roi_gray    = gray[y:y+h, x:x+h] # rec
        roi_color   = frame[y:y+h, x:x+h]
        nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (nx, ny, nw, nh) in nose:
            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
            roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
            mustache2 = image_resize(mustache.copy(), width=nw)
            mw, mh, mc = mustache2.shape
            for i in range(0, mw):
                for j in range(0, mh):
                    if mustache2[i, j][3] != 0:
                        roi_color[ny + int(nh/2.0) + i, nx + j] = mustache2[i, j]

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()