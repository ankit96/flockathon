import psycopg2
from pyflock import FlockClient, verify_event_token
# You probably want to copy this entire line
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction
import jwt

def set(name,userId,token):
    

    conn = psycopg2.connect(
        database='',
        user='',
        password='',
        host='',
        port=''

    )
    cur = conn.cursor()
    
    cur.execute("INSERT INTO appinstall (name,userid,token) VALUES ('"+str(name)+"','"+str(userId)+"','"+str(token)+"');")
    conn.commit()
    conn.close()
    return "Successfully registered"

def addplaylist(userId,playlistId):
    conn = psycopg2.connect(
        database='',
        user='',
        password='',
        host='',
        port=''

    )
    cur = conn.cursor()
    
    cur.execute("INSERT INTO playlist (userid,playlistid) VALUES ('"+str(userId)+"','"+str(playlistId)+"');")
    conn.commit()
    conn.close()

