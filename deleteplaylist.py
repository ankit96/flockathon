#!/usr/bin/python

import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

def deletep(playlistid):
	print "In deletep"
	
	
	CLIENT_SECRETS_FILE = "client_secrets.json"
	MISSING_CLIENT_SECRETS_MESSAGE = """
	WARNING: Please configure OAuth 2.0

	To make this sample run you will need to populate the client_secrets.json file
	found at:

	   %s

	with information from the {{ Cloud Console }}
	{{ https://cloud.google.com/console }}

	For more information about the client_secrets.json file format, please visit:
	https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
	""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
		                           CLIENT_SECRETS_FILE))

	
	YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"

	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
	  message=MISSING_CLIENT_SECRETS_MESSAGE,
	  scope=YOUTUBE_READ_WRITE_SCOPE)

	flow.params['access_type'] = 'offline'

	storage = Storage("create_playlist.py-oauth2.json")
	credentials = storage.get()

	if credentials is None or credentials.invalid:
	  flags = argparser.parse_args()
	  credentials = run_flow(flow, storage, flags)

	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
	  http=credentials.authorize(httplib2.Http()))

	# This code creates a new, private playlist in the authorized user's channel.
	playlists_delete_response = youtube.playlists().delete(
	  id=playlistid
	 
	).execute()
	
	


