__author__ = 'chenxm'

from pyDetectRight import DetectRight


## Modify to load detectright database
######################################
db = "/media/tera/workspace/eclipse/uadetector/db/detectright.data"
######################################


handler = DetectRight(db)
devmap = handler.getProfileFromUA("Android 4.1")
print devmap