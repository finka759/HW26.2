import re

from rest_framework.serializers import ValidationError


# def validate_youtube(value):
#     reg = re.compile(
#         '^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(?:-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|live\/|v\/)?)([\w\-]+)(\S+)?$')
#     if bool(reg.match(value)):
#         raise ValidationError('The URL must start with https://www.youtube.com')

class YTValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, video_track):
        youtube = 'https://youtube.com/'

        if video_track.get('video_track'):
            if youtube not in video_track.get('video_track'):
                raise ValidationError('Необходимо вставить ссылку на youtube')
        else:
            return None
