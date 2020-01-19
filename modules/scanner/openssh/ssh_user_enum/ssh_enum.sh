
read -p "Enter The Target Host : " host
read -p "Enter Your Username Wordlist Path : " users
clear
python3 ~/../usr/share/Pikachu/modules/post/openssh/ssh_user_enum/ssh_enum.py $host -U $users
