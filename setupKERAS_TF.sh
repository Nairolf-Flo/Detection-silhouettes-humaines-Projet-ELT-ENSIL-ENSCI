#!/bin/bash
echo "Update VM..."
sudo apt-get update
sudo apt-get upgrade
echo "Update OK"
echo ""
echo "Installation de Python3.8..."
sudo apt install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
echo "Python3.8 OK"
echo ""
echo "Installation de pip3..."
sudo apt install python3-pip
pip3 install --upgrade pip
echo "pip3 OK"
echo ""
echo "Installation de keras..."
sudo pip3 install keras
echo "keras OK"
echo ""
echo "Installation de tensorflow >2.2..."
sudo pip3 install tensorflow
echo "tensorflow OK"
echo ""
echo "Installation de numpy..."
sudo pip3 install numpy
echo "numpy OK"
echo ""
echo "Installation de unzip..."
sudo apt install zip unzip
echo "unzip OK"
echo ""
echo "La machinne est ready ! ^_^"