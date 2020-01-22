
read -p "Enter Port You Want To Listen : " port

clear
python3 ~/../usr/share/Raticate/modules/payloads/netcat/logo.py &&  nc -nlvp $port &


