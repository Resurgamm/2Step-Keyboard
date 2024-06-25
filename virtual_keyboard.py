import tkinter as tk
from itertools import product
from generate_prompt import Generator
from chat_bot import ChatBot
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import simplify_pinyin
from Pinyin2Hanzi import is_pinyin
from Pinyin2Hanzi import dag
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()
dagparams = DefaultDagParams()

class VirtualKeyboard:
	def __init__(self, master):
		self.master = master
		self.buffer = [[] for i in range(2)]
		self.cnt = 0
		self.combinations = []
		self.chatbot = ChatBot()  
		self.create_keyboard()

	def create_keyboard(self):
		initials = [
			' ', 'm', 'b p', 'g k', 'd t', 'f h', 'w y', 'l n r', 'j q x', 'z zh', 'c ch', 's sh'
		]
		finals = [
			'a o e', 'ai ei', 'ao ou', 'an ang', 'en eng ong', 'i in ing', 'ia ie', 'iu iong', 'ian iang', 'u uo', 'uai ui', 'ü ue', 'ua un', 'uan uang'
		]
		
		row = 0
		col_initial = 0
		 

		for initial in initials:
			button = tk.Button(self.master, text=initial, width=10, height=4, command=lambda k=initial: self.key_press(k))
			button.grid(row=row, column=col_initial, padx=5, pady=5)
			col_initial += 1
			if col_initial >= 2:  
				row += 1
				col_initial = 0

		row = 0
		col_final = col_initial + 10
		 
		for final in finals:
			button = tk.Button(self.master, text=final, width=10, height=4, command=lambda k=final: self.key_press(k))
			button.grid(row=row, column=col_final, padx=5, pady=5)
			col_final += 1
			if col_final >= col_initial + 13:  
				row += 1
				col_final = col_initial + 10

		self.end_button = tk.Button(self.master, text="END", width=10, height=4, command=self.end_input)
		self.end_button.grid(row=10, column=col_final, padx=5, pady=5)

	def key_press(self, key):

		if key == ' ':
			self.buffer[self.cnt % 2] = key
		else:
			self.buffer[self.cnt % 2] = key.split()
		
		combination = []
		
		if self.cnt % 2:
			for initial in self.buffer[0]:
				for final in self.buffer[1]:
					pinyin = ""
					if initial == ' ':
						pinyin = simplify_pinyin(f"{final}")
					else:
						pinyin = simplify_pinyin(f"{initial}{final}")
					if is_pinyin(pinyin):
						combination.append(pinyin)
			self.combinations.append(combination)
			# self.generate_combinations()
		
		self.cnt += 1
		self.display()

	def end_input(self):
		output = ""
		combinations = self.generate_combinations()
		
		cnt = 1
		for combination in combinations:
			result = viterbi(hmm_params=hmmparams, observations=combination, path_num=1)
			# result = dag(dagparams, combination, path_num=1)
			output += f"第{cnt}种可能性是: {' '.join(combination)} {''.join(result[0].path)}\n"
			cnt += 1
		
		prompt = Generator(output).generate_prompt(self.cnt / 2)
		answer = self.chatbot.generate_answer(prompt)
		
		# print(prompt)
		print(answer)
		
		self.buffer = [[] for i in range(2)]
		self.cnt = 0
		self.combinations = []
	
	def display(self):
		print(self.combinations)

	def generate_combinations(self):
		return list(product(*self.combinations))

if __name__ == "__main__":
	root = tk.Tk()
	root.title("Virtual Keyboard")
	keyboard = VirtualKeyboard(root)
	root.mainloop()
	
