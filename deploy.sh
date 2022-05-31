pip freeze > requirements.txt
git add .
git commit -m "deployment"
git push heroku main


# Django Settings
# heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'
# heroku config:set CLOUD_NAME=da7srpwm6
# heroku addons:create heroku-postgresql
# heroku config:set DB_NAME=galleria
# heroku config:set DB_USER=brian
# heroku config:set DB_PASSWORD=pass1123
# heroku config:set API_KEY=123334979696849
# heroku config:set API_SECRET=Jvd78nFKUziejHAW-b5Qn0gLuHk
# heroku config:set CLOUDINARY_URL=cloudinary://123334979696849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
# # pythone manage
# heroku config:set MODE='dev'
heroku config:set DB_HOST='127.0.0.1'
heroku config:set ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'


# heroku run python manage.py makemigrations
# heroku run python manage.py migrate