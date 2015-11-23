# This file is run as the vagrant user to setup the project

apt-get -y update
echo "=======Pip installing pip3"
apt-get install -y python3 build-essential libpq-dev python3-pip