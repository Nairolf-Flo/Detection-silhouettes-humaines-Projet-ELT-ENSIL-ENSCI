#!/bin/bash
echo "Update VM..."
apt-get update
apt-get upgrade
echo "Update OK"
echo ""
echo "Installation de Python3.8..."
apt install python3.8
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
echo "Python3.8 OK"
echo ""
echo "Installation de pip3..."
apt install python3-pip
pip3 install --upgrade pip
echo "pip3 OK"
echo ""
echo "Installation de tflite..."
pip3 install tflite
echo "tflite OK"
echo ""
echo "La machinne est ready ! ^_^"