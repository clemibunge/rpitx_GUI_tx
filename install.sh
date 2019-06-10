#!/bin/sh
#Install RPITX
cd ~

sudo apt-get update
sudo apt-get install git
git clone https://github.com/F5OEO/rpitx
cd rpitx
echo Install rpitx - some package need internet connection -
sudo apt-get install -y libsndfile1-dev git
sudo apt-get install -y imagemagick libfftw3-dev
#For rtl-sdr use
sudo apt-get install -y rtl-sdr buffer
# We use CSDR as a dsp for analogs modes thanks to HA7ILM
git clone https://github.com/simonyiszk/csdr
patch -i csdrpizero.diff csdr/Makefile
cd csdr || exit
make && sudo make install
cd ../ || exit
cd src || exit
git clone https://github.com/F5OEO/librpitx
cd librpitx/src || exit
make
cd ../../ || exit
cd pift8
git clone https://github.com/kgoba/ft8_lib
cd ../
make
sudo make install
cd .. || exit
printf "\n\n"
printf "In order to run properly, rpitx need to modify /boot/config.txt. Are you sure (y/n) "
read -r CONT
echo "Set GPU to 250Mhz in order to be stable"
LINE='gpu_freq=250'
FILE='/boot/config.txt'
grep -qF "$LINE" "$FILE"  || echo "$LINE" | sudo tee --append "$FILE"
echo "Installation completed !"
cd ~
echo Finished installing RPITX
#Install Dependencies
sudo apt-get install python python3 python-tk idle python-pmw python-imaging --yes
cd ~
cd rpitx_GUI_tx
python3 gui.py