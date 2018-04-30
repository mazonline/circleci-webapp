#!/bin/sh 

mkdir /work
cd /wprk
wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux32.tar.gz 
tar xfvz geckodriver-v0.20.1-linux32.tar.gz 
chmod +x geckodriver
mv geckodriver /usr/local/bin
