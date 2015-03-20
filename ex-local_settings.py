# if you want to use this file, rename to `local_settings.py`

# example of using database from lampp's mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<YOUR-DATABASE-NAME>', # database name, ideally equals to project name
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '/opt/lampp/var/mysql/mysql.sock', # database host
    }
}