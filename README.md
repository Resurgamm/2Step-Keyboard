# 2Step-Keyboard

## Introduction 

2Step-Keyboard is an attempt of a new type of Chinese input method which based on LLMs. All you need is two clicks on the keyboard, and what you want to say will be displayed on the screen.

![img](https://img2023.cnblogs.com/blog/2931579/202406/2931579-20240614194140866-625756654.png)

## Getting start

2Step-Keyboard uses the `Pinyin2Hanzi` repository. For getting start, you should install it.

```bash
pip install Pinyin2Hanzi
```

Then, clone the our repository to your computer.

```bash
git clone https://github.com/Resurgamm/2Step-Keyboard.git
```

You also need a ChatGPT API key and API base in order to link to ChatGPT.

In `chat_bot.py`

```py
def __init__(self, api_key = "YOUR_API_KEY", api_base = "YOUR_API_BASE"):
		self.api_key = os.getenv('OPENAI_KEY', default=api_key)
		self.api_base = api_base
		openai.api_key = self.api_key 
		openai.api_base = self.api_base
```

Just change `YOUR_API_KEY` and `YOUR_API_BASE` to your API key and API base.

Now, run `virtual_keyboard.py` and have a try! 