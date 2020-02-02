"""https://github.com/miguelgrinberg/flask-video-streaming"""
import io
import time
import picamera
from camera.base_camera import BaseCamera

class Camera(BaseCamera):
    """pi implementation of BaseCamera"""
    @staticmethod
    def frames():
        """yields a single frame of video"""
        with picamera.PiCamera() as camera:
            camera.rotation = 180
            # let camera warm up
            time.sleep(2)

            stream = io.BytesIO()
            for _ in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # return current frame
                stream.seek(0)
                yield stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()
