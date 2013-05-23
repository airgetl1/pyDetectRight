package omnilab.bd.chenxm;

import java.util.List;
import java.util.Map;

import com.detectright.core.ConnectionLostException;
import com.detectright.core.DetectRight;
import com.detectright.core.DetectRightException;
import com.detectright.core.DeviceNotFoundException;

import py4j.GatewayServer;


public class DetectRightEntry {
	private static int PORT = 25333;

	public static void main(String[] args) throws DetectRightException, ConnectionLostException, DeviceNotFoundException {
        GatewayServer gatewayServer = new GatewayServer(new DetectRightEntry(), PORT);
        gatewayServer.start();
        System.out.println("Gateway Server Started at port " + PORT);
    }

	public void initializeDetectRight(String dbString) throws DetectRightException, ConnectionLostException{
		DetectRight.initialize("SQLite//"+dbString);
	}
	
	public static Map<String, Object> getAllDevices() throws DetectRightException, ConnectionLostException{
		return DetectRight.getAllDevices();
	}
	
	public Map<String, Object> getAllDevices(List<String> deviceIDs) throws DetectRightException, ConnectionLostException{
		return DetectRight.getAllDevices(deviceIDs);
	}
	
	public Map<String, Object> getProfileFromUA(String useragent) throws DeviceNotFoundException, DetectRightException, ConnectionLostException{
		return DetectRight.getProfileFromUA(useragent);
	}
}
