"""
Split each string of the output file of Chef engine
Output of this function is a string that is input of HTMLParser function
"""
def splitInput(file_name, output_file):
	read_file = open(file_name,'r')
	write_file = open(output_file, 'w')
	for line in read_file:
		if (len(line.split(" input")) == 2):
			split_line = line.split(" input")[1]
			if (len(split_line.split("=>")) == 2) :
				output_line = split_line.split("=>")[1]
				write_file.write(output_line)

	read_file.close()
	write_file.close()

"""
this function reads input from input file
each input string is input for HTMLParserTest
this function will create test cases like in unittest module
"""
def create_test_cases(input_file, output_file):
	read_file = open(input_file, 'r')
	write_file = open(output_file, 'w')
	counter = 1  # counter of test cases

	# write modified python file 
	# modified symbolic test into file that can run concrete testing
	write_file.write("import unittest\n")
	write_file.write("import cStringIO\n")
	write_file.write("import ConfigParser\n")
	write_file.write("\n")
	write_file.write("class ConfigParserTestFunction(input_string):\n"
	+ "\t" + "string_file = cStringIO.StringIO(input_string)" + "\n"
	+ "\t" + "config = ConfigParser.ConfigParser()" + "\n"
	+ "\t" + "config.readfp(string_file)"	+ "\n\n"
	+ "\t" + "for s in config.sections():" + "\n"
	+ "\t\t" + "config.options(s)" + "\n\n"
	)
	# end writing function

	#start writing test cases
	write_file.write("class HTMLParserTest(unittest.TestCase):\n")
	for line in read_file:
		write_file.write("\t")
		write_file.write("def test_" + str(counter) + "(self):\n")
		counter = counter + 1
		input_string = line.split("\n")[0]
		write_file.write("\t\t")
		write_file.write("result = ConfigParserTestFunction("+ str(input_string) + ")")
		write_file.write("\n")
		write_file.write("\t\t")
		write_file.write("self.assertEqual(result, expected_result)")
		write_file.write("\n")
		write_file.write("\n")

	# end loop for writing test cases

	#write main function
	write_file.write("\n")
	write_file.write("if __name__ == '__main__':\n")
	write_file.write("\t")
	write_file.write("unittest.main()")
	#close input output
	write_file.close()
	read_file.close()


def checking(file_name, output_file):
	
	read = open(file_name, 'r')
	write = open(output_file, 'w')
	checking_line = read.readline()
	write.write(checking_line)
	for line in read:
		if not(line == checking_line):
			write.write(line)


#start calling functions
splitInput("all_test_cases.dat", "input_string.txt")
checking("input_string.txt", "checked_input.txt")
create_test_cases("checked_input.txt", "test_cases.py")