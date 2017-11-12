hygfull.csv:
	curl -LO 'https://github.com/astronexus/HYG-Database/raw/master/hygfull.csv'

hyg.json: hygfull.csv
	python parse-catalog.py
