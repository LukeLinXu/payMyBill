import os

import shutil
from functools import reduce

DOWNLOAD_PATH = '/Users/llin/Downloads'
MOVETO_PATH = '/Users/llin/Documents/Bills'

def renameFile(file_new_name, download_path=DOWNLOAD_PATH):
    files = os.listdir(download_path)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_path, x)), reverse=True)
    file = files[0]
    try:
        shutil.move(os.path.join(download_path, file), os.path.join(MOVETO_PATH, file_new_name))
    except Exception as e:
        print(e)

def getBroswerProfile():
    profile = {}
    profile["browser.download.panel.shown"] = False
    profile["browser.download.manager.showWhenStarting"] = False
    profile["browser.helperApps.neverAsk.openFile"] = "application/pdf"
    profile["browser.helperApps.neverAsk.saveToDisk"] = "application/pdf"
    profile["browser.download.folderList"] = 2
    profile["browser.download.dir"] = DOWNLOAD_PATH
    profile["pdfjs.disabled"] = True
    profile["plugin.scan.plid.all"] = True
    profile["plugin.scan.Acrobat"] = "99.0"
    return profile

def seperate_with(arrays):
    return reduce(lambda x, y : x + '_' + y, arrays)

def get_num(string):
    return float (string.replace('$', '').replace(',', ''))