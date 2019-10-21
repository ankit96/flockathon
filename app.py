__author__ = 'ankit'

import os
from flask import Flask,request, redirect, Response
from flask_wtf.csrf import CsrfProtect
from backend import set
from slashcommands import ndreminder,widgetview,echo
from radio import mirchi,gaana
import requests
import json
import re
from bs4 import BeautifulSoup
from pyflock import FlockClient, verify_event_token
# You probably want to copy this entire line
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction


app = Flask(__name__)
csrf = CsrfProtect(app)


@app.route('/events', methods=['post'])
@csrf.exempt
def doer():
    #return redirect('https://github.com/ankit96/flockathon')
    #body_unicode = request.body.decode("utf-8")
    content = request.get_json(silent=True)
    name = content['name']
    
    print str(name)
    if name=="app.install":
	userId = content['userId']
        token = content['token']
	
    #data = str(name)+","+str(userId)+","+str(token)
    	set(name,userId,token)
	return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
    
	
    elif name == "client.slashCommand":
	print "2nd elif"
	userId = content['userId']
	userName = content['userName']
	chat = content['chat']
	chatName = content['chatName']
	command = content['command']
	text = content['text']
	
	textarray=text.split(',')
	try:
		if textarray[0] == "list" and textarray[1] =="bollywood":
			data =  mirchi()
			songlist = ""
			for a in data:
				if len(songlist)<2:
					songlist = a[0]+" " +a[1]
				else:
					songlist = songlist + "," +a[0] +" "+ a[1]
			#print songlist
			echo(str(name),str(userId),str(userName),str(chat),str(chatName),str(command),str(songlist))
		elif textarray[0] == "list" and textarray[1] =="int":
			data =  gaana()
			echo(str(name),str(userId),str(userName),str(chat),str(chatName),str(command),str(data))
		else:
			echo(str(name),str(userId),str(userName),str(chat),str(chatName),str(command),str(text))
	
		return json.dumps({'success':True,'text':'Done'}), 200, {'ContentType':'application/json'} 
	except Exception as e: print str(e)


@app.route('/')
def hello():
    return redirect('https://github.com/ankit96/flockathon')




if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)

