.PHONY : build test run clean

build :
	@chmod +x ping
	@chmod +x scrape
	@chmod +x validInput
	@chmod +x testSingleAthlete
	@chmod +x testMultipleAthletes
	@chmod +x parse_inputs
	@chmod +x data_calculations.py

run :
	@echo "Execution trace 1" #Execution trace 1
	@make -s
	@echo "Scraping..."
	@./scrape CrossCountry "High School" NewJersey "Group IV" South
	@echo "Parsing..."
	@./parse_inputs data "all" "all" "M" "top"
	@mv data data_exec1
	@mv results results_exec1
	@make -s clean
	@echo "Execution trace 2" #Execution trace 2
	@make -s
	@echo "Scraping..."
	@./scrape TrackAndField "Middle School" NewJersey "" ""
	@echo "Parsing..."
	@./parse_inputs data "2018 Outdoor Season" "200 Meters" "F" "all"
	@mv data data_exec2
	@mv results results_exec2
	@make -s clean

view :
	@less scrape
	@less ping
	@less validInput
	@less parse_inputs
	@less data_calculations.py

test :
	@./testSingleAthlete
	@./testMultipleAthletes
	@vi singleAthlete.test
	@vi multipleAthletes.test
	@./parse_inputs singleAthlete.test all all all all
	@./parse_inputs multipleAthletes.test "2018 Season" "5,000 Meters" M top
clean :
	@rm -f index.html
	@rm -f *IDS
	@rm -f *.test
	@rm -f *.pyc
