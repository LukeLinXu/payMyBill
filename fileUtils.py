import os

import shutil

DOWNLOAD_PATH = '/home/llin'

def renameFile(file_new_name, download_path=DOWNLOAD_PATH):
    files = os.listdir(download_path)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_path, x)), reverse=True)
    file = files[0]
    try:
        shutil.move(os.path.join(download_path, file), os.path.join(download_path, file_new_name))
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