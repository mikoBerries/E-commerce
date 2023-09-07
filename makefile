server:
	./ecommerce/manage.py runserver

migration:
	py ./ecommerce/manage.py makemigrations

migrate:
	py ./ecommerce/manage.py migrate

shell:
	py ./ecommerce/manage.py shell

collectstatic:
	py ./ecommerce/manage.py collectstatic

depedency:
	py -m pip freeze > requirement.txt

container:
	docker build .

shells:
	docker exec -it app bin/sh

dockerbuild:
	docker-compose build

dockerup:
	docker-compose up

dockerdown:
	docker-compose down

test:
	docker-compose run --rm ecommerce sh -c "python manage.py test"

.phony: server migration migrate shell collectstatic depedency container shell test
