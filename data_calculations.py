#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys

def convert_to_base_units(data):
    '''
    Takes the times/distances of each athlete
    and converts them to the lowest base unit.
    '''
    
    times = data["Time"]
    
    #New column for keeping track of units
    data["Units"] = "seconds"

    #Replace with lowest base unit
    for index, time in enumerate(times.values):
        #Heights/distances
        if "'" in time:
            feet = float(time.split("'")[0]) * 12
            inches = float((time.split("'")[1]).strip())
            new_time = feet + inches

            unit = "inches"
        #Times > 1 min
        elif ":" in time:
            minutes = float(time.split(":")[0]) * 60
            seconds = float(time.split(":")[1])
            new_time = minutes + seconds
        
            unit = "seconds"
        #Times < 1 min
        else:
            unit = "not converted"
            new_time = float(time)

        #Replace valuse
        data.loc[index, "Units"] = unit
        data.loc[index, "Time"] = new_time
    return data

def convert_to_original_time(data):
    '''
    Takes the times of each athlete
    and converts them back to their original
    times
    '''
    
    #Replace times with seconds
    times = data["Time"]
    for index, time in enumerate(times.values):
        time = str(float(time) / 60)
        minutes = time.split(".")[0]
        seconds = round(float("0." + time.split(".")[1]) * 60, 2)
        
        #MM:SS.s
        new_time = "{}:{:04.1f}".format(minutes, seconds)
        
        data.loc[index, "Time"] = new_time   
    return data

def convert_to_original_length(data):
    '''
    Takes the distances/heights of each athlete
    and converts them back to their original
    units
    '''
    
    #Replace inches with feet + inches
    times = data["Time"]
    for index, time in enumerate(times.values):
        measurement = str(float(time) / 12)
        feet = measurement.split(".")[0]
        inches = round(float("0." + measurement.split(".")[1]) * 12, 2)
        
        #FF' II.i
        new_time = "{}' {:04.1f}".format(feet, inches)
        
        data.loc[index, "Time"] = new_time
    return data

def calculate_avg(data, year, distance, gender):
    '''
    Given the year, distance, and gender, this
    function takes that specific group of athletes
    and calculates the average of their times.
    '''
    
    #Group data by date, event, gender
    dates = data.loc[data["Year"] == year]
    events = dates.loc[data["Distance"] == distance]
    genders = events.loc[data["Gender"] == gender]

    #Nothing fits criteria
    if genders.empty:
        return

    #Open file to write
    f = open("results", "a")

    if events["Units"].values[0] == "inches":
        #Calculate average distance and covert back to FF' II.i
        measurements = genders["Time"].values
        measurement = str(np.mean(measurements) / 12)
        feet = measurement.split(".")[0]
        inches = round(float("0." + measurement.split(".")[0]) * 12, 2)

        print >>f, "Avg distance for {} {} in {}: {}' {:04.1f}".format(distance, gender, year,
                                                                       feet, inches)
    elif events["Units"].values[0] == "seconds":
        #Calculate average time and convert back to MM:SS.MS
        times = genders["Time"].values
        time = str(np.mean(times) / 60)
        minutes = time.split(".")[0]
        seconds = round(float("0." + time.split(".")[1]) * 60, 2)
        
        print >>f, "Avg time for {} {} in {}: {}:{:04.1f}".format(distance, gender, year,
                                                                  minutes, seconds)
    elif events["Units"].values[0] == "not converted":
        #Calculate average time
        times = genders["Time"].values
        time = str(np.mean(times))
        seconds = round(float(time), 2)
        
        print >>f, "Avg time for {} {} in {}: {:04.1f}".format(distance, gender, year,
                                                               seconds)
    #Close file
    print >>f, ""
    f.close()

def calculate_top(data, year, distance, gender):
    '''
    Given the year, distance, and gender, this
    function takes the specific group of athletes
    and outputs a list of the top 5 individuals.
    '''
    
    #Group data by date, event, gender
    dates = data.loc[data["Year"] == year]
    events = dates.loc[data["Distance"] == distance]
    genders = events.loc[data["Gender"] == gender]
   
    #Nothing fits criteria
    if genders.empty:
        return
    
    #Split between times and lengths
    if events["Units"].values[0] == "inches":
        #Sort Descending
        rankings = genders.sort_values(by = ["Time"], ascending = False)
        rankings = rankings.reset_index(drop = True)
        
        #Convert to original units
        rankings = convert_to_original_length(rankings)
    elif events["Units"].values[0] == "seconds":
        #Sort Ascending
        rankings = genders.sort_values(by = ["Time"])
        rankings = rankings.reset_index(drop = True)
        
        #Convert to original units
        rankings = convert_to_original_time(rankings)
    elif events["Units"].values[0] == "not converted":
        #Sort Ascending
        rankings = genders.sort_values(by = ["Time"])
        rankings = rankings.reset_index(drop = True)

    #Now output top 5
    f = open("results", "a")
    print >>f, rankings.iloc[0:5, [0, 2, 3, 4, 5, 6,]]
    print >>f, ""
    f.close()
