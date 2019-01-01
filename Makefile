down:
	docker-compose down --remove-orphans

clean:
	make down
	docker-compose build --pull

dev:
	docker-compose up --build

test:
	docker-compose run --rm api pytest --cov=deep --cov=apps --pep8 --cov-report term-missing -v $(args)
