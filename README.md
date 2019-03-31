## Post-Project Update:
Final project for my CS 265 class. Originally meant as a learning experience for web scraping and the initial stages of a project to study machine learning through predicting athlete's future times based on past results. Unfortunately, as I worked on this project, I was unfamiliar with scraping etiquette and the standard robots.txt. I believe that athletic.net does not allow scraping as stated in their robots.txt, so this project ends here. I'm adding it as a reminder to follow common courtesy and to not forget the work I put into it.

## Original Project README:
This program scrapes https://www.athletic.net for information on athletes
depending on the sport, age, state, district, and location. It then calculates
various top 5 lists and averages depending on user input. The main difficulties 
come from parsing the HTML of each page and generalizing it to apply to every 
potential application. Clubs and colleges are not available due to the 
differences in scraping them. Depending on the number of schools and athletes, 
the scraping can take approximately 5-10 minutes.


## Inputs:
./scrape Sport Age State District Location </br>
<b>Sport</b> 	    - "CrossCountry", "TrackAndField".</br>
<b>Age</b> 	    - "High School", "Middle School", "College".</br>
<b>State</b> 	    - Full name, no spaces, e.g. NewJersey.</br>
<b>Section</b>     - Depends on state, exact match as seen on athletic.net, e.g.
	      for New Jersey: "Group IV", use "" as placeholder if none.</br>
<b>Location</b>    - Depends on state, exact match as seen on athletic.net, e.g.
	      for New Jersey: South, use "" as placeholder if none.
	    
./parse_inputs File Year/Season Events Gender Function</br>
<b>File</b> 	    - The data file output from the scrape script.</br>
<b>Year/Season</b> - Full name of the year and season you would like as seen in the
	      data file, use "all" for every one in file. 
	      IMPORTANT: track and field specifies indoor vs outdoor while cross 
	      country does not, e.g. "2018 Outdoor Season".</br>
<b>Events</b>      - Full event name as seen in data file, use "all" for every  one
	      in file.</br>
<b>Gender</b>      - Gender of athletes, either "M", "F", or "all".</br>
<b>Function</b>    - Available functions, either "all", "avg", " or "top".


## Makefile:
<b>build</b>	    - Gives permission to all script and python files to be executed.</br>
<b>run</b>	    - Runs sample execution traces as seen below</br>
<b>view</b>	    - Displays source code for scrape, ping, validinput, parse_inputs, 
	      and data_calculation.</br>
<b>test</b>	    - Executes test scripts that are used to ensure the program runs properly.
	      Each script outputs a sample file with data, which is subsequently opened
              with vim for the user to make sure all data is valid.</br>
<b>clean</b>	    - Removes all intermediate files used for generating and analyzing the
	      data. Does not remove the data file. You should either rename or
	      delete it after if you do not want to append datasets together.

## Sample Executions:
Sample execution trace 1 - gets top 5 male times for xc for every event, every year</br>
make </br>
./scrape CrossCountry "High School" NewJersey "Group IV" South</br>
./parse_inputs data "all" "all" "M" "top"</br>
make clean</br>

Sample execution trace 2 - gets avg and top female times for track and field for 
			   200m for 2018 outdoor</br>
make</br>
./scrape TrackAndField "Middle School" NewJersey "" ""</br>
./parse_inputs data "2018 Outdoor Season" "200 Meters" "F" "all"</br>
make clean</br>

Outputs: data, results - files containing the data from the scrape and
	 analyzed output from the python scripts, respectively.
