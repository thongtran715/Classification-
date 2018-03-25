import fileinput
import sys
read_file = open("data.txt", "r+")


def fill_average(name_file, index):
	f = open(name_file, 'r')
	sum = 0.0
	tracker = 0
	for lines in f:
		lines = lines.split(",")
		counter = 0
		for line in lines:
			if counter == index:
				if line != "?":
					sum += float(line)
				else:
					tracker -= 1

			counter += 1
		tracker += 1
	result = sum/tracker
	f.close()
	return result

def perform_median (data_set):
	data_set.sort()
	length = len(data_set)
	if length % 2 == 0: #this is the even
		mid = floor(length/2)
		return data_set[mid]
	else:
		mid_next = int(length/2)
		mid_prev = mid_next -1 
		return (float(data_set[mid_next]) + float(data_set[mid_prev]))/2
	return 0

def fill_median (name_file, index):
	f = open(name_file,'r')
	data_set = []
	for line in f:
		line = line.split(",")
		counter = 0 
		for data in line:
			if counter == index:
				if data != "?":
					data_set.append(data)
			counter += 1
	return perform_median(data_set)

#this method is to replace every missing value with median
try:
	lst = []
	for line in read_file:
		line = line.split(',')
		counter = 0
		for data in line:
			if data == "?":
				number = fill_median("data.txt", counter)
				lst.append(number)
				print(number)
				break
			counter += 1
finally:
	read_file.close()

index = 0
for line in fileinput.input("data.txt", inplace=1):
		if "?" in line:
			replace_text = str(lst[index])
			line = line.replace("?",replace_text)
			index += 1
		sys.stdout.write(line)
# This is the method to replace every missing value with average. Seems not to work well
"""
try:

	lst = []
	for line in read_file:
		line = line.split(',')
		counter = 0
		for data in line:
			if data == "?":
				number = fill_average("data.txt", counter)
				print (number)
				lst.append(number)
				break
			counter += 1

finally:
	read_file.close()

index = 0
for line in fileinput.input("data.txt", inplace=1):
		if "?" in line:
			replace_text = str(lst[index])
			line = line.replace("?",replace_text)
			index += 1
		sys.stdout.write(line)
"""
