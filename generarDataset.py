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



def dividirDataset(rutaDataset, nombreCarpeTrain, nombreCarpeTest, rutaSalida, porcenVali):
    imagenes = sorted(glob.glob(rutaDataset + "*.jpg"))

    numImgTrain = len(imagenes)
    numImgTest = int(numImgTrain * porcenVali)

    carpetaTrain = rutaSalida + nombreCarpeTrain
    carpetaTest = rutaSalida + nombreCarpeTest

    try:
        os.mkdir(carpetaTrain)
    except FileExistsError:
        shutil.rmtree(carpetaTrain)
        os.mkdir(carpetaTrain)
        
    try:
        os.mkdir(carpetaTest)
    except FileExistsError:
        shutil.rmtree(carpetaTest)
        os.mkdir(carpetaTest)

    validation = []

    for i in range(numImgTest):
        img = random.choice(imagenes)
        validation.append(img)
        imagenes.remove(img)

    train = imagenes

    for img in train:
        shutil.copy(img, carpetaTrain)
        nombreImg = img.split('.')[0]
        shutil.copy(nombreImg + ".txt", carpetaTrain)
        
    for img in validation:
        shutil.copy(img, carpetaTest)
        nombreImg = img.split('.')[0]
        shutil.copy(nombreImg + ".txt", carpetaTest)

    return carpetaTrain, carpetaTest


def generarTrain(carpetaTrain, archivoTrain):
    image_files = []
    cwdIni = os.getcwd()

    os.chdir(carpetaTrain)

    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            image_files.append(carpetaTrain + "/" + filename)

    os.chdir("..")

    with open(archivoTrain, "w+") as outfile:
        for image in image_files:
            outfile.write(image)
            outfile.write("\n")
        outfile.close()
    
    os.chdir(cwdIni)

    return archivoTrain


def generarTest(carpetaTest, archivoTest):
    image_files = []
    cwdIni = os.getcwd()

    os.chdir(carpetaTest)

    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            image_files.append(carpetaTest + "/" + filename)

    os.chdir("..")

    with open(archivoTest, "w+") as outfile:
        for image in image_files:
            outfile.write(image)
            outfile.write("\n")
        outfile.close()

    os.chdir(cwdIni)

    return archivoTest


def obtenerClases(rutaDataset, archivoClases):
    with open(rutaDataset + archivoClases, "r") as file:
        contenido = file.read()
        file.close()

    listaClases = contenido.split('\n')
    numClases = len(listaClases)

    return contenido, numClases


def generarNames(rutaSalida, nombreCarpeTrain, clases):
    archivoNames = nombreCarpeTrain + ".names"
    with open(rutaSalida + archivoNames, "w+") as outfile:
        outfile.write(clases)
        outfile.close()

    return archivoNames


def generarData(rutaSalida, nombreCarpeTrain, numClases, archivoTrain, archivoTest, archivoNames, carpetaBackup):
    archivoData = nombreCarpeTrain + ".data"
    with open(rutaSalida + archivoData, "w+") as outfile:
        outfile.write("classes = " + str(numClases) + "\n")
        outfile.write("train = " + rutaSalida + archivoTrain + "\n")
        outfile.write("valid = " + rutaSalida + archivoTest + "\n")
        outfile.write("names = " + rutaSalida + archivoNames + "\n")
        outfile.write("backup = " + carpetaBackup)
        outfile.close()



if __name__=="__main__":
    rutaDataset = sys.argv[1]
    rutaSalida = sys.argv[2]
    porcenVali = float(sys.argv[3])

    nombreCarpeTrain = "obj"
    nombreCarpeTest = "test"

    archivoTrain = "train.txt"
    archivoTest = "test.txt"

    archivoClases = "classes.txt"

    carpetaBackup = "backup"

    carpetaTrain, carpetaTest = dividirDataset(rutaDataset, nombreCarpeTrain, nombreCarpeTest, rutaSalida, porcenVali)

    generarTrain(carpetaTrain, archivoTrain)

    generarTest(carpetaTest, archivoTest)

    clases, numClases = obtenerClases(rutaDataset, archivoClases)

    archivoNames = generarNames(rutaSalida, nombreCarpeTrain, clases)

    generarData(rutaSalida, nombreCarpeTrain, numClases, archivoTrain, archivoTest, archivoNames, carpetaBackup)
