run:
	docker-compose run app ./wait-for-it.sh mysql:3306 -- python3 script.py ${file} ${table}
