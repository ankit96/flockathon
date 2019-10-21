#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import os
def searchsongs(songname):
	try:
		os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ''

		DEVELOPER_KEY = ""
		YOUTUBE_API_SERVICE_NAME = "youtube"
		YOUTUBE_API_VERSION = "v3"


		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
		developerKey=DEVELOPER_KEY)

		search_response = youtube.search().list(
		q=songname + "song",
		part="id,snippet",
		maxResults=1
		).execute()

		videos = []
	
		for search_result in search_response.get("items", []):
			if search_result["id"]["kind"] == "youtube#video":
				return str(search_result["id"]["videoId"])
		return "1010"
	except e:
		return "1010"
	
	



  
