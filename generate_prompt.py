class Generator:
	def __init__(self, prompt = ""):
		self.prompt = prompt
	
	def generate_prompt(self, length):
		prompt = ""
		prompt += f"你是一个擅长中文的汉语言学家,你的汉语发音也十分标准,我将给你一些线索，请你猜测我正在说什么。像你知道的那样，中文的一个汉字由一个声母音节和一个韵母音节构成,例如,\"虐\"的拼音是 \"nve\"。\n"
		prompt += f"下面我将给出我说的话的所有可能性，当然，这些可能性是用拼音给出的，请你找出逻辑最清晰，语意最连贯的可能。\n"
		prompt += f"注意\"/\"代表空韵母。例如\"爱\"的拼音是\"/ai\"\n"
		prompt += self.prompt
		prompt += f"这句话一共有{length}个字。\n"
		prompt += f"注意我说的话一定与拼音的数量相同，不要增加，删除或修改任何的拼音，不要根据不存在我给出的拼音去生成答案。\n"
		prompt += f"请你给出最有可能的一句话。\n"
		prompt += f"你的回答格式只应该有我所需要的话，不需要任何别的内容。例如\"wo xi huan ni\"，你只需要输出\"我喜欢你\"而没有任何其他内容。"
		return prompt