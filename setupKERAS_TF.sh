#!/bin/bash
echo "Update VM..."
sudo apt-get update
sudo apt-get upgrade

echo "Installation de Python3.8..."
sudo apt install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2

echo "Installation de pip3..."
sudo apt install python3-pip
sudo pip3 install --upgrade pip

echo "Installation de keras..."
pip3 install keras

echo "Installation de tensorflow >2.2..."
pip3 install tensorflow

echo "Installation de numpy..."
pip3 install numpy
