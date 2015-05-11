"""
Split each string of the output file of Chef engine
Output of this function is a string that is input of HTMLParser function
"""
def splitInput(file_name, args_values):
	read_file = open(file_name,'r')
	write_file = open(args_values, 'w')
	counter = 4

	for line in read_file :	
		if (len(line.split(" arg")) == 5):
			#split each variable
			arg1_name = line.split(" arg")[1]
			arg2_name = line.split(" arg")[2]
			arg1 = line.split(" arg")[3]
			arg2 = line.split(" arg")[4]
			output_arg1_name = output_arg2_name = output_arg1 = output_arg2 = "default"
			#split value of each variable
			if(arg1_name[:6] == '1_name'):
				output_arg1_name = arg1_name.split("=>")[1]
			
			elif (arg1_name[:6] == '2_name'):
				output_arg2_name = arg1_name.split("=>")[1]

			elif (arg1_name[0] == '1'):
				output_arg1 = arg1_name.split("=>")[1]
			
			elif (arg1_name[0] == '2'):
				output_arg2 = arg1_name.split("=>")[1]
			
			if(arg2_name[:6] == '1_name'):
				output_arg1_name = arg2_name.split("=>")[1]
			
			elif (arg2_name[:6] == '2_name'):
				output_arg2_name = arg2_name.split("=>")[1]
			
			elif (arg2_name[0] == '1'):
				output_arg1 = arg2_name.split("=>")[1]
			
			elif (arg2_name[0] == '2'):
				output_arg2 = arg2_name.split("=>")[1]


			if(arg1[:6] == '1_name'):
				output_arg1_name = arg1_name.split("=>")[1]
			
			elif (arg1[:6] == '2_name'):
				output_arg2_name = arg1_name.split("=>")[1]
			
			elif (arg1[0] == '1'):
				output_arg1 = arg1_name.split("=>")[1]
			
			elif (arg1[0] == '2'):
				output_arg2 = arg1_name.split("=>")[1]

			if(arg2[:6] == '1_name'):
				output_arg1_name = arg2_name.split("=>")[1]
			
			elif (arg2[:6] == '2_name'):
				output_arg2_name = arg2_name.split("=>")[1]
			
			elif (arg2[0] == '1'):
				output_arg1 = arg2_name.split("=>")[1]
			
			elif (arg2[0] == '2'):
				output_arg2 = arg2_name.split("=>")[1]

			#write value of each variable to file
			if (output_arg1_name is not "default" and output_arg1_name is not "default" 
				and output_arg1 is not "default" and output_arg2 is not "default"):
				write_file.write(output_arg1_name)
				write_file.write("and")
				write_file.write(output_arg2_name)
				write_file.write("and")
				write_file.write(output_arg1)
				write_file.write("and")
				write_file.write(output_arg2)
				write_file.write("\n")

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
	counter = 1
	#write function to file
	write_file.write("import unittest\n")
	write_file.write("import argparse\n")
	write_file.write("\n")
	write_file.write("class ArgarseTestFunction(arg1_name, arg2_name, arg1, arg2):\n"
	+ "\t" + "parser = argparse.ArgumentParser(description=\"Symtest\")" + "\n"
	+ "\t" + "parser.add_argument(arg1_name)" + "\n"
	+ "\t" + "parser.add_argument(arg2_name)" + "\n"
	+ "\t" + "parser.parse_args(arg1, arg2)"	+ "\n\n")
	#end write function to file
	write_file.write("class ArgparserTest(unittest.TestCase):\n")
	#for each 4 inputs
	for line in read_file:
		write_file.write("\t")
		write_file.write("def test_" + str(counter) + "(self):")  #name of test case
		write_file.write("\n")
		counter = counter + 1 # increase counter of test cases
		input_string = line.split("and") #split to comput input values
		last_input = input_string[3].split("\n")[0]  #last input with \n
		#compute result
		write_file.write("\t\t")
		write_file.write("result = ArgarseTestFunction(" + str(input_string[0]) + ", " + str(input_string[1])
							+ ", " +str(input_string[2]) + ", " + str(last_input) + ")" + "\n")
		#write assert 
		write_file.write("\t\t")
		write_file.write("self.assertEqual(result, expected_result)")
		write_file.write("\n")
		write_file.write("\n")

	#main function
	write_file.write("\n")
	write_file.write("if __name__ == '__main__':\n")
	write_file.write("\t")
	write_file.write("unittest.main()")
	write_file.close()
	read_file.close()


#splitInput("hl_test_cases.dat", "arg_1.txt", "arg_2.txt", "arg_3.txt", "arg_4.txt")
splitInput("all_test_cases.dat", "args_values.txt")
create_test_cases("args_values.txt", "test_cases.py")

