prepare:
	sudo apt-get install python3 python3-dev \
	build-essential libssl-dev libffi-dev \
	libxml2-dev libxslt1-dev zlib1g-dev \
	python3-pip python3-venv
	curl -sSL https://install.python-poetry.org | python3 -

install:
	poetry install --no-dev

run-smoke-test:
	poetry run locust \
	    --locustfile ./test_suite/smoke_test.py --csv=./reports/smoke_test.csv \
			--logfile=./reports/smoke_test.log \
			--html ./reports/smoke_test.html

run-test:
	poetry run locust \
	    --locustfile ./test_suite/test.py --csv=./reports/test.csv \
			--logfile=./reports/test.log \
			--html ./reports/test.html