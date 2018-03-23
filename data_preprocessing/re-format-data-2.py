#this file is to re-format the data
read_file = open("back_up_data.txt", 'r')
write_file = open("complete_data_2.txt", 'a')

for lines in read_file:
	lines = lines.strip() # Chop the end line
	lines = lines.split(",")
	#Switch the array with last column
	last = lines[len(lines) -1]
	lines[len(lines) - 1] = lines[0]
	lines[0] = last
	#create the str to hold the format
	string = ""
	for i in range(1,len(lines)):
		index = str(i)
		value = str(lines[i])
		combine = index + ":" + value
		string = string + combine + " "
	if lines[0] == '0':
		append_string = "5" + " "
		append_string += string
	else:
		append_string = lines[0] + " "
		append_string += string	
	append_string+="\n"
	write_file.write(append_string)

read_file.close()
write_file.close()
