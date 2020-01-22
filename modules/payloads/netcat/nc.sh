
read -p "Enter Port You Want To Listen : " port

clear
xterm -geometry 90x30+3+10 -hold -e "python3 ~/../usr/share/Raticate/modules/payloads/netcat/logo.py &&  nc -nlvp $port" &



