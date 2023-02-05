SHELL:=/bin/bash

gen_reqs:
	pipenv install --deploy
	pipenv lock -r > requirements.txt
	#pipenv lock -r --dev-only > requirements-dev.txt
