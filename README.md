alexa_pi_ynh
============
Package YunoHost - Alexa Python pour RaspberryPI

Commande d'installation :

    sudo yunohost app install https://github.com/pbillerot/alexa_pi_ynl

RaspberryPI Rev 2 Model B
-------------------------
Processeur Armv6
Ram 500 Mo

YunoHost
--------
    Linux my.domain 4.19.69+ #1261 Tue Sep 3 20:21:01 BST 2019 armv6l GNU/Linux


Les librairies python de l'assistant **Alexa** ont pour prérequis la version Python 3.6
- raspian-stretch héberge la version python 3.5
- --> il faut installer la version 3.6 sur PI

```python
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev
sudo apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
sudo apt-get install -y libncurses5-dev  libncursesw5-dev xz-utils tk-dev

wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
tar xvf Python-3.6.9.tgz
cd Python-3.6.9
./configure --enable-optimizations
sudo make altinstall
python3.6

```