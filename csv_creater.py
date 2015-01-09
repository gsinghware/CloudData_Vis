""" csv_creater.py 
	This script will generate csv files for each year.
	
	Columns 
		Date | WS1 | WS2 | WS3 | WS4 ...
	Row
		01/01/1984 | 132 | 32 | 13 | 213 ... 

	Terminal Command
	python csv_creater.py 83010100 83123121
	83 01 01 00
	83 12 31 21

"""
import os
import sys
import csv
import numpy as np
from collections import Counter

def main():
	# read the terminal input for the initial date
	start_year = sys.argv[1][0:2]
	start_month = sys.argv[1][2:4]
	start_day = sys.argv[1][4:6]

	# read the terminal input for the end date
	end_year = sys.argv[2][0:2]
	end_month = sys.argv[2][2:4]
	end_day = sys.argv[2][4:6]

	# saving initial date
	_start_year = start_year
	_start_month = start_month
	_start_day = start_day

	# saving end date
	_end_year = end_year
	_end_month = end_month
	_end_day = end_day

	# print start_year, start_month, start_day, start_hr
	# print end_year, end_month, end_day, end_hr

	fieldnames = ['date', 'WS1', 'WS2', 'WS3', 'WS4', 'WS5', 'WS6', 'WS7', 'WS8', 'WS9', 'WS10', 'WS11', 'WS12']
	with open('1990.csv', 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
				
		while (int(start_year + start_month + start_day) 
				<= int(end_year + end_month + end_day)):

			date = start_month + "-" + start_day + "-19" + start_year
			file_path = 'daily_data/1990/' + date + ".csv"
		
			if os.path.exists(file_path):
				map_ary = np.loadtxt(open(file_path, "rb"), delimiter = ",", skiprows = 1)
				ws_counter = Counter([j for i in map_ary for j in i])
				
				writer.writerow({'date': date, 'WS1': ws_counter[1], 'WS2': ws_counter[2], 'WS3': ws_counter[3],
									'WS4': ws_counter[4], 'WS5': ws_counter[5], 'WS6': ws_counter[6],
									'WS7': ws_counter[7], 'WS8': ws_counter[8], 'WS9': ws_counter[9],
									'WS10': ws_counter[10], 'WS11': ws_counter[11], 'WS12': ws_counter[12]})

				
			start_day = int(start_day) + 1
			start_day = str(start_day).zfill(2)

			if (int(start_month + start_day) > 1231):
				start_year = int (start_year)
				start_year = start_year + 1
				start_year = str(start_year).zfill(2)
				start_month = '01'
				start_day = '01'

			if (int(start_day) > 31):
				start_month = int (start_month)
				start_month = start_month + 1
				start_month = str(start_month).zfill(2)
				start_day = '01'

if __name__ == '__main__':
	main()