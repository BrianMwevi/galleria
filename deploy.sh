pip freeze > requirements.txt
git add .
git commit -m "deployment"
git push heroku main


# Django Settings
# heroku config:set SECRET_KEY='django-insecure-h-4_vq % @6x462t8ly = k = +8os_54n7_lziad!i4 *$_rey9b@1mb'
# heroku config:set CLOUD_NAME=da7srpwm6
# heroku addons:create heroku-postgresql

# heroku config:set API_KEY=123334979696849
# heroku config:set API_SECRET=Jvd78nFKUziejHAW-b5Qn0gLuHk
# heroku config:set CLOUDINARY_URL=cloudinary://123334979696849:Jvd78nFKUziejHAW-b5Qn0gLuHk@da7srpwm6
# # pythone manage

heroku run python manage.py makemigrations
heroku run python manage.py migrate