Salvatore Zerbo
CS 265 Final Project
Winter 2019
Team Repository: https://gitlab.cci.drexel.edu/slz37/cs265-final-project

This program scrapes https://www.athletic.net for information on athletes
depending on the sport, age, state, district, and location. It then calculates
various top 5 lists and averages depending on user input. The main difficulties 
come from parsing the HTML of each page and generalizing it to apply to every 
potential application. Clubs and colleges are not available due to the 
differences in scraping them. Depending on the number of schools and athletes, 
the scraping can take approximately 5-10 minutes.

./scrape Sport Age State District Location
Sport 	    - "CrossCountry", "TrackAndField".
Age 	    - "High School", "Middle School", "College".
State 	    - Full name, no spaces, e.g. NewJersey.
Section     - Depends on state, exact match as seen on athletic.net, e.g.
	      for New Jersey: "Group IV", use "" as placeholder if none.
Location    - Depends on state, exact match as seen on athletic.net, e.g.
	      for New Jersey: South, use "" as placeholder if none.
	    
./parse_inputs File Year/Season Events Gender Function
File 	    - The data file output from the scrape script.
Year/Season - Full name of the year and season you would like as seen in the
	      data file, use "all" for every one in file. 
	      IMPORTANT: track and field specifies indoor vs outdoor while cross 
	      country does not, e.g. "2018 Outdoor Season".
Events      - Full event name as seen in data file, use "all" for every  one
	      in file.
Gender      - Gender of athletes, either "M", "F", or "all".
Function    - Available functions, either "all", "avg", " or "top".


Makefile target descriptions:
build	    - Gives permission to all script and python files to be executed.

run	    - Runs sample execution traces as seen below

view	    - Displays source code for scrape, ping, validinput, parse_inputs, 
	      and data_calculation.

test	    - Executes test scripts that are used to ensure the program runs properly.
	      Each script outputs a sample file with data, which is subsequently opened
              with vim for the user to make sure all data is valid.

clean	    - Removes all intermediate files used for generating and analyzing the
	      data. Does not remove the data file. You should either rename or
	      delete it after if you do not want to append datasets together.


Sample execution trace 1 - gets top 5 male times for xc for every event, every year
make 
./scrape CrossCountry "High School" NewJersey "Group IV" South
./parse_inputs data "all" "all" "M" "top"
make clean

Sample execution trace 2 - gets avg and top female times for track and field for 
			   200m for 2018 outdoor
make
./scrape TrackAndField "Middle School" NewJersey "" ""
./parse_inputs data "2018 Outdoor Season" "200 Meters" "F" "all"
make clean

Outputs: data, results - files containing the data from the scrape and
	 analyzed output from the python scripts, respectively.
