import openai
import os

class ChatBot:
	def __init__(self, api_key = "YOUR_API_KEY", api_base = "YOUR_API_BASE"):
		self.api_key = os.getenv('OPENAI_KEY', default=api_key)
		self.api_base = api_base
		openai.api_key = self.api_key 
		openai.api_base = self.api_base


	def generate_answer(self, prompt):
		messages = [      
			{"role": "system", "content": "你是一个精通汉语言文学的AI"},
			{"role": "user", "content": prompt}
		]

		response = openai.ChatCompletion.create(
			model="gpt-4o",
			messages=messages,
			temperature=0.5,
		)

		result = ''
		for choice in response.choices:
			result += choice.message.content

		return result

if  __name__ == "__main__":
	bot = ChatBot()
	prompt = input()
	message = bot.generate_answer(prompt)
	print(message)