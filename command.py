from nltk.tokenize import RegexpTokenizer
from textblob import TextBlob

tokenizer = RegexpTokenizer(r'\w+')

class Command(object):
	def __init__(self):
		self.commands = { 
			"sentiment": self.sentiment,
			"jump" : self.jump,
			"help" : self.help
		}

	def handle_command(self, user, command):
		response = "<@" + user + ">: "
		words = tokenizer.tokenize(command)
		command = words[0]
		query = str(words[1:])

		print(command)
		print(query)


		if command in self.commands:
			response += self.commands[command](query)
		else:
			response += "Sorry I don't understand the command: " + command + ". " + self.help("dummy")
		
		return response
		
	def sentiment(self,query):
		from textblob import TextBlob
		blob = TextBlob(query)
		blob.sentiment.polarity
		resp = "Sentiment score is: " + str(blob.sentiment.polarity)
		return resp
		

	def jump(self,query):
		return query
		
	
	def help(self,query):
		response = "Currently I support the following commands:\r\n"
		
		for command in self.commands:
			response += command + "\r\n"
			
		return response