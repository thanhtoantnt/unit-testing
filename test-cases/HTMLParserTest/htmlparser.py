"""
Split each string of the output file of Chef engine
Output of this function is a string that is input of HTMLParser function
"""
def splitInput(file_name, output_file):
	read_file = open(file_name,'r')
	write_file = open(output_file, 'w')
	for line in read_file:
		if (len(line.split(" html")) == 2):
			split_line = line.split(" html")[1]
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
	write_file.write("import HTMLParser\n")
	write_file.write("\n")
	write_file.write("class HTMLParserTestFunction(unittest.TestCase):\n"
	+ "\t" + "parser = HTMLParser.HTMLParser()	" + "\n"
	+ "\t" + "parser.feed(input_string)" + "\n"
	+ "\t" + "parser.close()"	+ "\n\n")
	# end writing function

	#start writing test cases
	write_file.write("class HTMLParserTest(unittest.TestCase):\n")
	for line in read_file:
		write_file.write("\t")
		write_file.write("def test_" + str(counter) + "(self):\n")
		counter = counter + 1
		input_string = line.split("\n")[0]
		write_file.write("\t\t")
		write_file.write("result = HTMLParserTestFunction("+ str(input_string) + ")")
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

#start calling functions
splitInput("all_test_cases.dat", "input_string.txt")
create_test_cases("input_string.txt", "test_cases.py")