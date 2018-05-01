#!/bin/sh 

sudo mkdir /work
cd /wprk
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux32.tar.gz 
tar xfvz geckodriver-v0.20.1-linux32.tar.gz 
pwd
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
echo "Confirming geckodriver is in $PATH"
which geckodriver
