import psycopg2
from pyflock import FlockClient, verify_event_token
# You probably want to copy this entire line
from pyflock import Message, SendAs, Attachment, Views, WidgetView, HtmlView, ImageView, Image, Download, Button, OpenWidgetAction, OpenBrowserAction, SendToAppAction
import jwt


def main():
	app_id = ''
	user_token = '' 
	flock_client = FlockClient(token=user_token, app_id=app_id)
	group_id = ''
	print flock_client.get_group_info(group_id)
	print flock_client.get_group_members(group_id)
	print flock_client.get_groups()


main()
