#!/bin/bash

# Installation de keras
echo "Installation de python3-pip..."
sudo apt install python3-pip
echo "OK"
echo ""

echo "Installation de keras..."
sudo pip3 install keras
echo "OK"
echo ""

# Installation de l'API coco
echo "Installation de Cython..."
pip3 install Cython
echo "OK"
echo ""

echo "Installation de matplotlib..."
pip3 install matplotlib
echo "OK"
echo ""

echo "Installation de API coco..."
pip3 install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI
echo "OK"
echo ""

echo "Installation de unzip..."
sudo apt install zip unzip
echo "OK"
echo ""

echo "Telechargement des annotations de coco..."
wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip
echo "OK"
echo ""

echo "unzip annotations_trainval2017.zip..."
unzip annotations_trainval2017.zip
echo "OK"
echo ""

echo "Suppression de annotations_trainval2017.zip..."
rm annotations_trainval2017.zip
echo "OK"
echo ""

echo "Creation dossier images..."
mkdir images
echo "OK"
echo ""

cd images/

echo "Telechargement des images pour la validation..."
wget http://images.cocodataset.org/zips/val2017.zip
echo "OK"
echo ""

echo "Telechargement des images pour l'entrainement..."
wget http://images.cocodataset.org/zips/train2017.zip
echo "OK"
echo ""

echo "unzip val2017..."
unzip val2017.zip
echo "OK"
echo ""

echo "unzip train2017..."
unzip train2017.zip
echo "OK"
echo ""

echo "Suppression de val2017.zip..."
rm val2017.zip
echo "OK"
echo ""

echo "Suppression de train2017.zip..."
rm train2017.zip
echo "OK"
echo ""

cd ..

sudo apt-get install tree

tree

echo "La machinne est ready ! ^_^"