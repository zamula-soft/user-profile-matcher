build:
	docker compose build

up:
	docker compose up -d --force-recreate

down:
	docker compose down --remove-orphans

restart:
	docker compose down --remove-orphans  -v --rmi all
	docker compose build
	docker compose up

down_and_up:
	docker compose down --remove-orphans
	docker compose build
	docker compose up -d --force-recreate
#

test:
	pytest --tb=short

black:
	black -l 86 $$(find * -name '*.py')