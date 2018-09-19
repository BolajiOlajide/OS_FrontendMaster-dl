import os
import click

from dotenv import load_dotenv

from extractor.spider import Spider


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

@click.command()
@click.option('--course', prompt='Course ID', help='Course ID (e.g. `firebase-react`)')
# @click.option('--id', prompt='Username', help='Frontend Master Username')
# @click.option('--password', prompt='Password', help='Frontend Master Password')
@click.option('--mute-audio', help='Mute Frontend Master browser tab', is_flag=True)
@click.option('--high-resolution', help='Download high resolution videos', is_flag=True)
@click.option('--video-per-video', help='Download one video at a time', is_flag=True)
def downloader(course, mute_audio, high_resolution, video_per_video):
    spider = Spider(mute_audio)
    click.secho('>>> Login with your credential', fg='green')
    id = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    spider.login(id, password)

    click.secho('>>> Downloading course: ' + course, fg='green')
    spider.download(course, high_resolution, video_per_video)

    click.secho('>>> Download Completed! Thanks for using frontendmasters-dl', fg='green')

# TODO: (Xinyang) Switching to setuptools
#   http://click.pocoo.org/5/quickstart/#switching-to-setuptools
if __name__ == '__main__':
    downloader()
