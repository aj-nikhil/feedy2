- Make a virtualenv `virtualenv feedy2_env`
- Activate the virtualenv 
- Install all packages `pip install -r requirements.txt`
- Create PostGresql Db `createdb feedy2`
- Create User `createuser feedy2`
- Change the rights of the user and assign feedy2 db's owner to feedy2 use following commands
- `psql -U postgres`
- `postgres=# ALTER ROLE feedy2 SUPERUSER;`
- `postgres=# ALTER DATABASE feedy2 OWNER TO feedy2;`
- run migrations `python manage.py migrate`
- create superuser using `python manage.py createsuperuser`