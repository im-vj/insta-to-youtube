import os
import instaloader

def download_instagram_video(url, download_path):
    post_shortcode = url.split("/")[-2]
    L = instaloader.Instaloader(dirname_pattern=download_path, download_videos=True)
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)
    L.download_post(post, target=post_shortcode)
    return os.path.join(download_path, post_shortcode, f"{post_shortcode}.mp4")
