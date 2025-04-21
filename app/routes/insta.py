from flask import Blueprint, request, render_template, redirect, flash, current_app
from app.services.instagram_downloader import download_instagram_video
from app.services.youtube_uploader import upload_video
import os

insta_bp = Blueprint('insta', __name__)

@insta_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('insta_link')
        if not link:
            flash("Instagram link is required!", "danger")
            return redirect('/')
        
        try:
            video_path = download_instagram_video(link, current_app.config['DOWNLOAD_FOLDER'])
            upload_video(video_path, "Repost from Instagram", "Auto-uploaded via Flask app")
            flash("Video uploaded to YouTube successfully!", "success")
        except Exception as e:
            flash(f"Error: {e}", "danger")
    
    return render_template('index.html')
