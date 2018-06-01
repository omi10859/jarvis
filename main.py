from text_speach import speak_this
from asset.something import anything
import re



def input_taking(input_text_msg):
	str(input_text_msg)

input_text=input('hello,, say something \n ')
input_taking(input_text)

if input_text == 'hi':
	speak_this("hello world. I'm jarvis. I'm here to help you")
	print("hello world. I'm jarvis. I'm here to help you.")
elif input_text == 'how are you':
	speak_this("I'm good , what about you?")
	print("I'm good , what about you")
elif input_text == 'open facebook':
	anything('ummmmm....')
	speak_this('hang on.....')

else:
	speak_this("look's like i don't know what you are saying")
	input_taking(input())
