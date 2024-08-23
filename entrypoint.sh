#!/bin/sh

echo 'Waiting PostgreSQL'

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.5
done

echo 'PostgreSQL started'

python3 warehouses/manage.py migrate

exec "$@"