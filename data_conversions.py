#!/usr/bin/env python

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
