# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:48:50 2021

@author: Angela
"""

# Unir contornos en uno solo
def countours_union(a,b):
    x = min(a[0], b[0])
    y = min(a[1], b[1])
    w = max(a[0]+a[2], b[0]+b[2]) - x
    h = max(a[1]+a[3], b[1]+b[3]) - y
    return (x, y, w, h)

# Convertir vídeo a frames, crop de la calle
# def vid2frames(filename, n_lane):
#     import cv2
#     cap = cv2.VideoCapture(filename)
#     original_width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   
#     original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
#     success,image = cap.read()
#     # Vídeos con escala 1/2
#     if original_width == 1292:
#         w_lane = 120                                                # Anchura de la calle (píxeles) 
#         lane_xy = {"1": 690,"2": 590,"3": 490,"4": 390,"5": 290}
#     # Vídeos con resolución máxima:
#     elif original_width == 2584:
#         w_lane = 220  
#         lane_xy = {"1": 1560,"2": 1370,"3": 1170,"4": 990,"5": 790}

# Sin discriminar calle
def vid2frames(filename):
    count = 0
    import cv2
    cap = cv2.VideoCapture(filename)
    success,image = cap.read() 
    # Extraer frames
    while success and count<2:
      # top = lane_xy[str(n_lane)]                                   # ROI (calle única)
      # bottom = top + w_lane
      image = image[:,:,:]            # Recorte de la calle de interés
      #path = 'C:/Users/angel/Desktop/AQUATICSLab/Visión artificial/Breaststroke/swimmer_frames/'
      cv2.imwrite("pool%d.jpg" % count, image)     # Guardar frame como JPEG      
      success,image = cap.read()
      print('Frame %d ' % count)
      count += 1
      k = cv2.waitKey(1) & 0xff
      # o hasta que se presiona la tecla ESC
      if k == 27 : 
          break
      
def list_files(directorio):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(directorio) if isfile(join(directorio, f))]
    return onlyfiles


# from tkinter import filedialog as fd
# import cv2
# vid = fd.askopenfilename()
# vid2frames(vid,2)

# import random
import shutil, os, random

direc = r'C:\Users\angel\Desktop\AQUATICSLab\Visión artificial\YOLOYOLO\crops_120x120'
direc2 = r'C:\Users\angel\Desktop\AQUATICSLab\Visión artificial\YOLO\TrainingSET'
destino = r'C:\darknet-master\build\darknet\x64\data\crops_120x120'
a = list_files(direc)  
b = list_files(direc2)
a = list(filter(lambda f: f.endswith('.jpg'), a))
a = sorted(a, key=lambda k: random.random())
b = list(filter(lambda f: f.endswith('.jpg'), b))
b = sorted(b, key=lambda k: random.random())
textfile1 = open("val.txt", "w")
textfile2 = open("train.txt", "w")
for elem in a:
    elem = 'data/images/' + elem
    textfile1.write(elem + "\n")
for elem in b:
    if '.jpg' in elem:
        elem = 'data/images/' + elem
        textfile2.write(elem + "\n")
    
textfile1.close()
textfile2.close()

# for elem in a:
#     if '.txt' in elem:
#         source = os.path.join(direc, elem)
#         shutil.copy(source, destino)

# vid2frames('Competition_2016_5_14_10_26_54_Breaststroke_50m_Male_Series_2_Scale_2_41.6667fps.avi')