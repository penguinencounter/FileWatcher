import time
import requests
import hashlib
import os


class WatchedFile:
    def __init__(self, file_url: str):
        self.url = file_url
        self.folder_name = hashlib.sha256(bytes(self.url, encoding='UTF-8')).hexdigest()
        self.file_name = self.url.split('/')[-1]
        try:
            os.mkdir(f'downloads/{self.folder_name}')
        except FileExistsError:
            print('Directory already exists. Is something wrong?')
        self.last_sum = ''
        self.last_checked = time.time()  #Linux
        self.last_status = 200
        self.version = 0
        self.local_path = ''

    def download(self):
        r = requests.get(self.url)
        self.last_checked = time.time()
        self.last_status = r.status_code
        if r.status_code != 200:
            print(f'WatchedFile.download: Error; status code is {r.status_code} not 200; cancelling download')
            return
        print(f'WatchedFile.download: File recieved, hashing')
        this_sum = hashlib.sha256(r.content).hexdigest()
        print(f'WatchedFile.download: Hash is {this_sum[:16]}... (comparing to {self.last_sum[:16]})')
        if this_sum != self.last_sum:
            self.version += 1
            print(f'WatchedFile.download: File changed, saving')
            self.last_sum = this_sum
            file_path = f'downloads/{self.folder_name}/v{self.version}_{self.file_name}'
            with open(file_path, 'wb') as f:
                f.write(r.content)
            print(f'Saved')


class FileWatchingGuild:
    def __init__(self, guildid: int):
        self.id = guildid
        self.watching = []
        
if __name__ == '__main__':
    print('TESTING MODE')
    f = WatchedFile('https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-1-traditional-events.pdf')
    f2 = WatchedFile('https://www.firstinspires.org/sites/default/files/uploads/resource_library/ftc/game-manual-part-1-remote-events.pdf')
    f.download()
    f2.download()
