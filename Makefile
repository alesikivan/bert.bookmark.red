all:
	echo hello, this is makefile 

install:
	pip install -r requirements.txt

up:
	docker-compose up -d

down:
	docker-compose down

run:
	python3 manage.py runserver 0.0.0.0:80