REQUIREMENTS=requirements.txt
PACKAGE=doboto

install_modules:
	pip install -r ${REQUIREMENTS}

run_tests:
	nosetests --with-coverage --cover-package=${PACKAGE} tests

run_lint:
	@echo "Running PEP8:"
	pep8 --max-line-length=100 ${PACKAGE}
	@echo "Running pylint:"
	pylint ${PACKAGE}

precommit: run_tests run_lint
