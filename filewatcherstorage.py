

class WatchedFile:
    def __init__(self, file_url: str):
        self.url = file_url
        self.last_sum = 0
        self.last_checked = 0


class FileWatchingGuild:
    def __init__(self, guildid: int):
        self.id = guildid
        self.watching = []
        self.filerev