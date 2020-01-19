clear
figlet John The Ripper 
echo "                                                           by Bananaj00e"
read -p "Enter Your SHA1 Hash to Crack : " hash
read -p "Enter Your Wordlist Path : " word
clear
touch hash
echo Your Hash is  :$hash >> hash
clear
john hash --wordlist=$word --format=raw-sha1
clear
echo "[*] Success "
john --show --format=Raw-SHA1 hash
rm -rf hash
