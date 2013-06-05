__author__ = 'chenxm'

from pyDetectRight import DetectRight
from py4j.protocol import Py4JJavaError


## Modify to load detectright database
######################################
db = "/Users/chenxm/Jamin/workspace/eclipse/uadecoder/db/detectright.data"
######################################


dr = DetectRight(db)
dr.start_server()
devmap = dr.getProfileFromUA("Android 4.1")
print devmap


uaprofile = "http://nds1.nds.nokia.com/uaprof/N6303iclassicr100.xml"
print dr.getProfileFromUAProfile(uaprofile)


# detectright.jar in the library folder is under evalution.
# some functions are disabled and exception will be raised.
# try:
# 	handler.getAllDevices()
# except Py4JJavaError as e:
# 	print e


dr.stop_server()