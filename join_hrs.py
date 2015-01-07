""" join_hrs.py
	This script will read the data from the binary file. Since each file contains
	data for 3-hours and 24 hrs make a day, we will read 8 files, that makes 24hrs/1day, 
	and then take a slice from each file and output a file for 1 day.
	This will make the data standard for 12 noon for each day.

	Terminal Command
	python join_hrs.py 83010100 83123121
	83 01 01 00
	83 12 31 21

"""
import sys
import os
import numpy as np
from tempfile import TemporaryFile

i = 0
def format_data(ary, yyyymmddhh):
	global i
	ary.shape = (72, 144)
	ary = np.rot90(ary)
	ary = np.rot90(ary)
	ary[ary == -999] = 13
	return ary

temp_path = 'binary_data/19'

def doWork(start_year, start_month, start_day, start_hr, three_hour_counter, numA, numB):
	# file_path = binary_data/2005/yyyymmddhh.84010100
	file_path = (temp_path + start_year +'/yyyymmddhh.' + 
				 	start_year + start_month + start_day + start_hr)
	
	if os.path.exists(file_path):
		_file = np.fromfile(file_path, dtype='int32')
		_file = format_data(_file, str(start_year + start_month + start_day + start_hr))
		slice_1 = _file[0:72, numA:numB]
		three_hour_counter.append(slice_1)
		
	return

def main():
	# read the terminal input for the initial date
	start_year = sys.argv[1][0:2]
	start_month = sys.argv[1][2:4]
	start_day = sys.argv[1][4:6]
	start_hr = sys.argv[1][6:8]

	# read the terminal input for the end date
	end_year = sys.argv[2][0:2]
	end_month = sys.argv[2][2:4]
	end_day = sys.argv[2][4:6]
	end_hr = sys.argv[2][6:8]

	# saving initial date
	_start_year = start_year
	_start_month = start_month
	_start_day = start_day
	_start_hr = start_hr

	# saving end date
	_end_year = end_year
	_end_month = end_month
	_end_day = end_day
	_end_hr = end_hr

	# print start_year, start_month, start_day, start_hr
	# print end_year, end_month, end_day, end_hr

	three_hour_counter = []

	while (int(start_year + start_month + start_day + start_hr) 
			<= int(end_year + end_month + end_day + end_hr)):
		
		# 144/8 = 18
		if (int(start_hr) == 0):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 0, 18)

		elif (int(start_hr) == 3):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 18, 36)

		elif (int(start_hr) == 6):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 36, 54)

		elif (int(start_hr) == 9):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 54, 72)

		elif (int(start_hr) == 12):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 72, 90)

		elif (int(start_hr) == 15):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 90, 108)

		elif (int(start_hr) == 18):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 108, 126)

		elif (int(start_hr) == 21):
			doWork(start_year, start_month, start_day, start_hr, three_hour_counter, 126, 144)

		if (len(three_hour_counter) == 8):
			complete_day = np.concatenate((three_hour_counter[0], three_hour_counter[1], three_hour_counter[2], 
				three_hour_counter[3], three_hour_counter[4], three_hour_counter[5], 
				three_hour_counter[6], three_hour_counter[7]), axis=1)

			# print start_month, start_day, start_year
			# print len(complete_day), len(complete_day[0])
			
			np.savetxt(start_month+"-"+start_day+"-"+start_year+".csv", complete_day, delimiter=",", fmt='%1.3f')
			break
			three_hour_counter = []

		start_hr = int (start_hr)
		start_hr = start_hr + 3
		start_hr = str(start_hr).zfill(2)

		if (int(start_month + start_day + start_hr) > 123121):
			start_year = int (start_year)
			start_year = start_year + 1
			start_year = str(start_year).zfill(2)
			start_month = '01'
			start_day = '01'
			start_hr = '00'

		if (int(start_day + start_hr) > 3121):
			start_month = int (start_month)
			start_month = start_month + 1
			start_month = str(start_month).zfill(2)
			start_day = '01'
			start_hr = '00'

		if (int(start_hr) > 21):
			start_day = int (start_day)
			start_day = start_day + 1
			start_day = str(start_day).zfill(2)
			start_hr = '00'

if __name__ == '__main__':
	main()