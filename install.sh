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
sudo apt-get install -y rtl-sdr buffer
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
echo "Set GPU to 250Mhz in order to be stable"
LINE='gpu_freq=250'
FILE='/boot/config.txt'
grep -qF "$LINE" "$FILE"  || echo "$LINE" | sudo tee --append "$FILE"
echo "Installation completed !"
cd ~
echo Finished installing RPITX
cd ~
cd rpitx_GUI_tx
chmod +x startgui.sh
cd ~
#Install Dependencies
sudo apt-get install python python3 python-tk idle python-pmw python-imaging --yes
#Add to startup
printf "Add to Startup (y/n) "
read -r CONT
if [ "$CONT" = "y" ]; then
  echo "Adding to startup"
   (crontab -l 2>/dev/null; echo "@reboot python3 /home/pi/rpitx_GUI_tx/gui.py &") | crontab -
   echo "Added to Startup!"
else
  echo "Info : Automatic GUI startup disabled";
fi
