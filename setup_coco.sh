#!/bin/bash
sudo mkdir -p /mt/sda1
cd /mnt

sudo apt install python-pip
sudo pip install --upgrade pip

echo "/!\ Installation pour COCO"
echo "Installation de Cython..."
pip install Cython

echo "Installation de matplotlib..."
pip install matplotlib

echo "Installation de PIL"
pip install pillow

echo "Installation de unzip..."
sudo apt install zip unzip

echo "Installation de API coco..."
pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI

echo "Telechargement des annotations de coco..."
sudo wget http://images.cocodataset.org/annotations/annotations_trainval2017.zip

echo "unzip annotations_trainval2017.zip..."
sudo unzip annotations_trainval2017.zip

echo "Suppression de annotations_trainval2017.zip..."
sudo rm annotations_trainval2017.zip

echo "Creation dossier images..."
mkdir images

cd images/
echo "Telechargement des images pour la validation..."
sudo wget http://images.cocodataset.org/zips/val2017.zip

echo "Telechargement des images pour l entrainement..."
sudo wget http://images.cocodataset.org/zips/train2017.zip

echo "unzip val2017..."
sudo unzip val2017.zip

echo "unzip train2017..."
sudo unzip train2017.zip

echo "Suppression de val2017.zip..."
sudo rm val2017.zip

echo "Suppression de train2017.zip..."
sudo rm train2017.zip