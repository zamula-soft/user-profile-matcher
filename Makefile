build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down --remove-orphans

restart:
	docker compose down --remove-orphans
	docker compose build
	docker compose up -d

#

black:
	black -l 86 $$(find * -name '*.py')