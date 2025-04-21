from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
import os

def authenticate_youtube(credentials_path):
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)
    credentials = flow.run_console()
    return build("youtube", "v3", credentials=credentials)

def upload_video(video_file, title, description):
    youtube = authenticate_youtube("config/credentials.json")

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_file)
    )
    response = request.execute()
    return response["id"]
