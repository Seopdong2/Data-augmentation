import cv2
import os

video_name = "movie31"
path = 'C:/Users/ADMIN/Desktop/test1/' + video_name
os.mkdir(path)

vidcap = cv2.VideoCapture('C:/Users/ADMIN/Desktop/test1/' + video_name + '.mp4')
success, image = vidcap.read()

count = 0
success = True

while success:
    success, image = vidcap.read()

    if (int(vidcap.get(1)) % 30 == 0):
        cv2.imwrite(path + '/' + video_name + '_%d.jpg' % count, image)
       #cv2.imwrite('C:/Users/ADMIN/Desktop/' + video_name + "_%d.jpg" % count, image)
        print("saved image %d.jpg" % count)

        count += 1

    if cv2.waitKey(10) == 27:
        break
