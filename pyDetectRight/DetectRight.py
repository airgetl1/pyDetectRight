__author__ = 'chenxm'


from py4j.java_gateway import JavaGateway
from py4j.java_collections import SetConverter, MapConverter, ListConverter


class DetectRight(object):

	def __init__(self, dbstring):
		self.gateway = JavaGateway()
		self.entry = self.gateway.entry_point
		self.gateway.entry_point.initializeDetectRight(dbstring)


	def getAllDevices(self):
		return self.entry.getAllDevices()


	def getAllDevicesByIDs(self, ids):
		java_list = ListConverter().convert(ids, self.gateway._gateway_client)
		return self.entry.getAllDevices(java_list)


	def getProfileFromUA(self, ua):
		return self.entry.getProfileFromUA(ua)
