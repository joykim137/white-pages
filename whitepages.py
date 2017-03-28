# imports argument variable into current name contxt
from sys import argv

# unpacks argument variable and the arguments are assigned to variables
script, filename = argv

# informs user what to do to save information
print "Write the information required and press Enter to save contact information."

# opens the text file that is the variable "filname" in write mode
target = open(filename, 'w')

# tells user to fill out information of the first person
print "\nFill out the information of the first person."

# prints "Name : " and defines line1 by raw input
line1 = raw_input("Name : ")
# prints "Birthday : " and defines line2 by raw input
line2 = raw_input("Birthday : ")
# prints "Phone Number : " and defines line3 by raw input
line3 = raw_input("Phone Number: ")

# informs user of input information being saved
print "\nThis contact information will be saved in the white pages."

# tells user to fill out information of the second person
print "\n\nFill out the information of the second person."

# skips a line and leave line 4 blank in the text file
line4 = ("\n")
# prints "Name : " and defines line5 by raw input
line5 = raw_input("Name : ")
# prints "Birthday : " and defines line2 by raw input
line6 = raw_input("Birthday : ")
# prints "Phone Number : " and defines line7 by raw input
line7 = raw_input("Phone Number: ")
# tells user to fill out information of the third person

print "\nThis contact information will be saved in the white pages."
# informs user of input information being saved
print "\n\nFill out the information of the third person."

# skips a line and leave line 8 blank in the text file
line8 = ("\n")
# prints "Name : " and defines line9 by raw input
line9 = raw_input("Name : ")
# prints "Birthday : " and defines line2 by raw input
line10 = raw_input("Birthday : ")
# prints "Phone Number : " and defines line11 by raw input
line11 = raw_input("Phone Number: ")

# writes line1 in the file
target.write(line1)
# moves line2 to a new line in the file
target.write("\n")
# writes line2 in the file
target.write(line2)
# moves line3 to a new line
target.write("\n")
# writes line3 in the file
target.write(line3)
# leaves a blank line
target.write(line4)
# moves line5 to a new line
target.write("\n")
# writes line5 in the file
target.write(line5)
# moves line6 to a new line
target.write("\n")
# writes line6 in the file
target.write(line6)
# moves line7 to a new line
target.write("\n")
# writes line7 in the file
target.write(line7)
# writes line8 in the file
target.write(line8)
# moves line9 to a new line
target.write("\n")
# writes line9 in the file
target.write(line9)
# moves line10 to a new line
target.write("\n")
# writes line10 in the file
target.write(line10)
# moves line11 to a new line
target.write("\n")
# writes line11 in the file
target.write(line11)

# informs user of input information being saved
print "This contact information will be saved in the white pages."

# closes the text file
target.close()
