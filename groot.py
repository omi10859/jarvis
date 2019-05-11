from texttospeech import speak_this
from random import randint
from asset.modules.OpenUrl.openurl import openweb
from asset.modules.playvideo.play import playthis
import re


def input_taking(input_text_msg):

	if re.findall("^news",input_text_msg):
		keywords = str(input_text_msg).split()
		return [keywords[0],keywords[1:]]



	if re.match(".*[open mail|mail|groot mail|shoot mail|gmail|mail it].*",input_text_msg):
		return ["mail", "Mail Tab"]


	if re.match(".*[open docs|docs|groot docs|open notes|take note|take notes].*",input_text_msg):
		return ["notes", "Note Tab"]

	if re.match(".*[bored|surprise me|surprise].*", input_text_msg):
		return ["surprise", "Link Exploration"]

		
	didyousay=('hi groot',
			  'how are you',
			  'what is love',
			  'open facebook',
			  'how are you so smart'
			  )

	ansisthis=("hello, What can i do for you",
			   "I'm still hot and sexy. Tell me something about you hotty",
			   "It's is something you should not do",
			   "oh, It is because my Creator is so smart."
			   )

	whenidontknow=("I am Groot",
				   "what you are saying bro",
				   "What the fuck, say again",
				   "ok, lets try again")

	if re.findall('[A-Z|a-z]{2,}[.][a-z]{2,}', input_text_msg):
		urls=re.findall('[A-Z|a-z]{2,}[.][a-z]{2,}', input_text_msg)
		url=urls[0]
		url_sk=re.findall('([a-z|A-Z]{2,})[.]', url)
		s='opening %s please wait'%str(url_sk[0])
		speak_this(s)
		returnvar=s
		openweb(url)

	elif re.findall('[o][n][ ][y][o][u][t][u][b][e]', input_text_msg):
		 urls=re.findall('[p][l][a][y](.+)[o][n][ ][y][o][u][t]', input_text_msg)
		 url=str(urls)
		 speak_this("Let's play"+ url)
		 returnvar=("Let's play"+ url)
		 playthis(url)

	else:
		l=0
		for i in range(0,3):
			if didyousay[i]==input_text_msg.lower():
				speak_this(ansisthis[i])
				returnvar=ansisthis[i]
				l=1

		if l==0:
			i=randint(0, 3)
			speak_this(whenidontknow[i])
			returnvar=whenidontknow[i]
			
	return ["not news",returnvar]
