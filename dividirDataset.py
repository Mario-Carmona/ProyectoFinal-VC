#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 02:22:21 2021

@author: Mario Carmona Segovia
"""

import glob
import os
import sys
import shutil
import random

random.seed(0)


rutaDataset = sys.argv[1]
rutaSalida = sys.argv[2]
porcenVali = float(sys.argv[3])

imagenes = sorted(glob.glob(rutaDataset + "*.jpg"))

numImgTrain = len(imagenes)
numImgVali = int(numImgTrain * porcenVali)

carpetaTrain = rutaSalida + "train"
carpetaVali = rutaSalida + "validation"

try:
    os.mkdir(carpetaTrain)
except FileExistsError:
    shutil.rmtree(carpetaTrain)
    os.mkdir(carpetaTrain)
    
try:
    os.mkdir(carpetaVali)
except FileExistsError:
    shutil.rmtree(carpetaVali)
    os.mkdir(carpetaVali)

validation = []

for i in range(numImgVali):
    img = random.choice(imagenes)
    validation.append(img)
    imagenes.remove(img)

train = imagenes

for img in train:
    shutil.copy(img, carpetaTrain)
    nombreImg = img.split('.')[0]
    shutil.copy(nombreImg + ".txt", carpetaTrain)
    
for img in validation:
    shutil.copy(img, carpetaVali)
    nombreImg = img.split('.')[0]
    shutil.copy(nombreImg + ".txt", carpetaVali)

