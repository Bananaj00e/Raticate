clear
read -p "Enter Base64 Hash : " var
touch hash
echo $var >> hash
echo -e "\e[31m==========================================================="
echo ""
echo ""
base64 -d hash
rm -rf hash
echo ""
echo ""
echo ""
echo -e "\e[31m==========================================================="
