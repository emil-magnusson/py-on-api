# py-on-api
 ***py-on-api** Open Networks API (ON-API) written in python.
 A dummy service to rapid up development for service providers. No logic just ont-to-one mapping betwen endpoints and sql tables.
 

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

```python
    >>> python manage.py migrate
```

```python
    >>> python manage.py runserver
```

Go to http://127.0.0.1:8000/admin and add your data.

Available endpoints.

```python
/2.4
/2.4/accesses
/2.4/orders
/2.4/subscriptions
/2.4/accesses
/2.4/orders
/2.4/option82
/2.4/dhcplookup
```

#
