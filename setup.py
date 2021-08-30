import os

try:
    os.mkdir('downloads')
except FileExistsError:
    pass
try:
    os.mkdir('reload_files')
except FileExistsError:
    pass
