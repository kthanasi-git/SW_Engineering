pytest -v # Run the tests
coverage -m pytest -v #Run the tests and collect stats
coverage report -m #Show statement coverage

coverage run --branch -m pytest -v #Collect branch coverage
coverage report -m
