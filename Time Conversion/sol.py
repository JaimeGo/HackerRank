#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    hour=int(s[0:2])

    if s.endswith("PM"):
    	
    	if hour!=12:
    		hour+=12

    	hour_str=completeStr(hour)

    	return hour_str+s[2:-2]

    else:
    	if hour==12:
    		hour=0

    	hour_str=completeStr(hour)
    	
    	return hour_str+s[2:-2]
    	

def completeStr(hour):
	hour_str=str(hour)

	if len(hour_str)==1:
		hour_str="0"+hour_str

    return hour_str



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
