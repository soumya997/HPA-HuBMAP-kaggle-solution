import xml.etree.ElementTree as ET

with open("/home/lakshita/fcw-single-keyboard-demo/virtual_obstacles/alive-dev/virtual_obj_simulator/common_road_xml/temp1.xml") as fobj:
        xml = fobj.read()
        # getting the root tag from the xml
        commonRoad = ET.fromstring(xml)
        all_static_obj = commonRoad.getchildren()
        print(all_static_obj)