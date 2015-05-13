import HTMLParser

class HTMLParserTestFunction(unittest.TestCase):
	parser = HTMLParser.HTMLParser()	
	parser.feed(input_string)
	parser.close()

