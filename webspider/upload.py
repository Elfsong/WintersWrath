import os
from google.cloud import storage
from google.cloud.storage import Blob

class Uploder():
    def __init__(self):
        self.IMAGE_DIR = "/home/dumingzhex/Projects/WintersWrath/webspider/Image/"
        self.storage_client = storage.Client()
        try:
            self.bucket = self.storage_client.get_bucket('argus_space')
            print("bucket")
        except Exception as e:
            print(e)
            print('Sorry, that bucket does not exist!')

    def generator(self, file_name):
        #encryption_key = 'c7f32af42e45e85b9848a6a14dd2a8f6'
        self.blob = Blob( file_name, self.bucket, encryption_key=None )
        self.blob.upload_from_filename( self.IMAGE_DIR + file_name )
        self.blob.make_public()

    def get_media_link(self):
        return self.blob.media_link

    def get_public_link(self):
        return self.blob.public_url

    def get_dir(self, dir_name):
        return os.listdir(dir_name)

if __name__ == "__main__":
    uploder = Uploder()
    dir_list = uploder.get_dir(uploder.IMAGE_DIR)
    for image in dir_list:
        uploder.generator(image)
        print(uploder.get_public_link())

