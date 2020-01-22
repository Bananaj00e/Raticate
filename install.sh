ch = "pwd"
clear
 
echo -e "\e[92m      Linux         Termux"
echo -e "   \e[92m    (1)            (2)"
echo "[*] Enter Your System"
read var
      


if [ $var == "1" ]
then
alias pikachu='python3 /usr/share/Raticate/Main/Raticate.py'
echo -e "\033[0;31m This Installer must run with root"

cp -r $ch /usr/share
echo "alias raticate='python3 /usr/share/Raticate/Main/Raticate.py'" >> /root/.bashrc

fi


if [ $var == "2" ]
then
alias pikachu='python3 //data/data/com.termux/files/usr/share/Raticate/Main/Raticate.py'
echo "termux" >> version
cp -r $ch //data/data/com.termux/files/usr/share
echo "alias raticate='python3 //data/data/com.termux/files/usr/share/Raticate/Main/Raticate.py'" >> //data/data/com.termux/files/usr/etc/bash.bashrc

fi

pip3 install colorama
pip3 install urllib.request
pip3 install urllib
pip3 install progress.bar
pip3 install progress
pip2 install requests
pip2 install json
pip2 install colorama
pip2 install urlparse



clear
echo ""

echo -e "\033[1;37m[\033[0;31m*\033[1;37m] Raticate Has been Installed succesfully"

echo -e "\033[1;37m[\033[0;31m*\033[1;37m] Type 'raticate' In Another Terminal To RUN "

