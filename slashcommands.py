import psycopg2
from pyflock import FlockClient, verify_event_token
# You probably want to copy this entire line
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction
import jwt
from create_playlist import createp
from backend import addplaylist
def ndreminder(name,userId,userName,chat,chatName,command,textdata):
	print "in chat func"
	conn = psycopg2.connect(
	database='',
	user='',
	password='',
	host='',
	port=''

	)


	cur = conn.cursor()
	cur.execute("SELECT token from appinstall where userid='"+str(userId)+"';")
	rows = cur.fetchall()

	token = str(rows[0])
	token = token[2:-3]
	print token
    #print token
	
	
	app_id = ''
	user_token = '' # Store the token against a guid during app install event and retreive it from the user id in event token

	#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
	flock_client = FlockClient(token=user_token, app_id=app_id)

	res = None

	# Send a simple send message
	simple_message = Message(to=chat,text=textdata)
	# returns a message id
	res = flock_client.send_chat(simple_message)
	print(res)
	
	
def echo(name,userId,userName,chat,chatName,command,textdata):
	print "in echo func"
	try:
	    #print token
	
	
		app_id = ''
		user_token = '' # Store the token against a guid during app install event and retreive it from the user id in event token
		user_t=''

		#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
		flock_client = FlockClient(token=user_token, app_id=app_id)
	
	
		res = None
		value=createp(userId,textdata)
		videoid=value[0]
		playlistid=value[1]
		print userId
		print playlistid
		playurl  = "https://www.youtube.com/watch?v="+videoid+"&list="+playlistid
		iframeurl = "https://www.youtube.com/embed/videoseries?list="+playlistid
		# Send a simple send message
		
		views = Views()
		inlinehtml = "<iframe src="+iframeurl+"></iframe>"
		html = HtmlView(inline=inlinehtml,height=150)
		views.add_html(html)
		flockmllink = "<flockml>click <action type='openWidget' url="+playurl+" desktopType='sidebar' mobileType='modal'>here</action> to launch a widget.</flockml>"
		views.add_flockml(flockmllink)
		
		
		
		attachment = Attachment(title="Your Playlist", description="Note :All Playlist gets  deleted by midnight", views=views)
		# NOTE: attachments is an array of attachment
		html_message = Message(to=userId, attachments = [attachment])
		res = flock_client.send_chat(html_message)
		addplaylist(userId,playlistid)
		print(res)
		"""
		views = Views()
		flockmllink = "<flockml>click <action type='openWidget' url="+playurl+" desktopType='sidebar' mobileType='modal'>here</action> to launch a widget.</flockml>"
		views.add_flockml(flockmllink)

		attachment = Attachment(title="Your Playlist", description="Note :All Playlist gets  deleted by midnight", views=views)
		# NOTE: attachments is an array of attachment
		flockml_message = Message(to=userId, attachments = [attachment])
		res = flock_client.send_chat(flockml_message)
		print(res)
		#click <action id="act1" type="openWidget" url="<url>" desktopType="sidebar" mobileType="modal">here</action> to launch a widget.
		"""
		'''
		simple_message = Message(to=userId,text=playurl)
		# returns a message id
		res = flock_client.send_chat(simple_message)
		print(res)
		
		send_as_hal = SendAs(name='Beats', profile_image='http://www.iconeasy.com/icon/png/File%20Type/Sinem/File%20Music.png')
		send_as_message = Message(to=userId,text=playurl,send_as=send_as_hal)
		res = flock_client.send_chat(send_as_message)
		print(res)
		'''
		''''
		views = Views()
		widget = WidgetView(src="http://www.radiomirchi.com/more/mirchi-top-20",width=400,height=250)
		views.add_widget(widget)

		attachment = Attachment(title="Your Playlist", description="Every playlist gets automatically deleted at midnight", views=views)
		# NOTE: attachments is an array of attachment
		widget_message = Message(to=userId, attachments = [attachment])
		res = flock_client.send_chat(widget_message)
		print(res)
		'''
		'''
		b1 = Button(name = "Harry Potter", id="harry", action=OpenWidgetAction(url=playurl, desktop_type="sidebar"))
		attachment = Attachment(title="playlist", buttons=[b1])
		button_message = Message(to=userId, text="cs", attachments = [attachment])
		res = flock_client.send_chat(button_message)
		print(res)
		
		views = Views()
		image = ImageView(original=Image(src="http://static.flock.co/flock/flock-logo-fb.png", width=400, height=400),filename="onering.png")
		views.add_image(image)

		attachment = Attachment(title="Test image", description="One Ring to rule them all, One Ring to find them, One Ring to bring them all and in the darkness bind them", views=views)
		# NOTE: attachments is an array of attachment
		image_message = Message(to=userId, attachments = [attachment])
		res = flock_client.send_chat(image_message)
		print(res)
		'''
	except Exception as e: print str(e)
#text = "humdard,bandeya tu muh modke na ja,humari adhuri kahani,phir kabhi"
#echo("sd","sd","sd","sd","sd","sd","humdard,bandeya tu muh modke na ja,humari adhuri kahani,phir kabhi")
def widgetview(name,user_guid,userName,chat,chatName,command,textdata):
	print "In widgetview"
	try:
		app_id = ''
		user_token = '' # Store the token against a guid during app install event and retreive it from the user id in event token

	#Create a flock client. Needs token and app id for this. You can get the token id and app id when you register. This is for a bot.
		flock_client = FlockClient(token=user_token, app_id=app_id)
		views = Views()
		widget = WidgetView(src="",height=250)
		views.add_widget(widget)

		attachment = Attachment(title="Test widget", description="Replace src with your own page", views=views)
		# NOTE: attachments is an array of attachment
		widget_message = Message(to=user_guid, attachments = [attachment])
		res = flock_client.send_chat(widget_message)
		flock_client1 = FlockClient(token='', app_id=app_id)
		print(res)
		print flock_client1.get_group_info(chat)
		print flock_client1.get_group_members(chat)
		print flock_client1.get_groups()
		print flock_client1.get_user_info()
		print flock_client1.get_contacts()
	except Exception as e: print str(e)
	

