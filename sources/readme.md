
 Test de l'application
 ---------------------
    ssh admin@server-yunohost
    sudo yunohost app upgrade alexa -u https://github.com/pbillerot/alexa_pi_ynh
    sudo systemctl stop alexa.service
    /var/www/alexa $ source venv/bin/activate
    gunicorn --bind 127.0.0.1:8000 wsgi:app
    curl http://127.0.0.1:8000/alexa/

Synoptique de l'application
===========================

Réception de la requête HTTP par `NGINX`
--------------------------------------
_NGINX: le serveur Web asynchrone qui traite les requêtes HTTP et HTTPS_

Via la commande `proxy_pass` routage de la requête HTTP sur un socket
```
proxy_pass http://unix:__YNH_APP_FSPATH__/sock;
```

Ecouteur des requêtes par `Gunicorn`
----------------------------------
_Gunicorn: un serveur Web python_
```
command = '__YNH_APP_PATH__/venv/bin/gunicorn'
...
bind = 'unix:__YNH_APP_PATH__/sock'
```
_À noter que Gunicorn utilise un environnement python virtuel avec tous les packages nécessaires à l'application._

Appel de l'application python via l'interface `WSGI`
----------------------------------------------------
_Ce appel se fait via le service système qui démarre `NGINX`_

    ExecStart=__YNH_APP_PATH__/venv/bin/gunicorn -c __YNH_APP_PATH__/gunicorn.py wsgi:app

_Le répertoire de l'application est donné en paramètre à `wsgi`_

