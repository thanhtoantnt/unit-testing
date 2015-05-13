import cStringIO
import ConfigParser

class ConfigParserTestFunction(input_string):
	string_file = cStringIO.StringIO(input_string)
	config = ConfigParser.ConfigParser()
	config.readfp(string_file)

	for s in config.sections():
		config.options(s)

		