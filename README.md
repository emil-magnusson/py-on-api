# py-on-api
 ***py-on-api** Open Networks API (ON-API) written in python.
 


## API Documentation ##
https://github.com/on-api/on-api

## Installing ##
Check out the latest development version:
```bash
$ https://github.com/emil-magnusson/py-on-api.git
$ cd py-on-api
```
To install dependencies run:
```bash
$ pip install -r requirements.txt
```

## Usage 
Set up an admin account.
```python
    >>> python manage.py createsuperuser --username admin --email admin@example.com
```

```python
    >>> python manage.py makemigrations
```
Migrate database.
```python
    >>> python manage.py migrate
```

```python
    >>> python manage.py runserver
```

Go to http://127.0.0.1:8000/admin and add your data.

Available endpoints

http://127.0.0.1:8000/2.4
http://127.0.0.1:8000/2.4/accesses
http://127.0.0.1:8000/2.4/orders
http://127.0.0.1:8000/2.4/subscriptions
http://127.0.0.1:8000/2.4/accesses
http://127.0.0.1:8000/2.4/orders
http://127.0.0.1:8000/2.4/option82
http://127.0.0.1:8000/2.4/dhcplookup
#
