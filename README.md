# simpleSite
I,m trying to build my first simpleSite on Python with Flask framework :)

## venv activating

sudo python3 -m venv venv
sudo virtualenv venv
source venv/bin/activate

## database adding support

pip3 install flask-sqlalchemy
pip3 install flask-migration

## create migrations under (venv) mode
flask db init

### first migration under (venv) mode
flask db migrate -m "users table"

### first upgrade migration under (venv) mode
flask db upgrade

### complete of migration under (venv) mode
flask db migrate -m "content table"


###### test

Thats all
