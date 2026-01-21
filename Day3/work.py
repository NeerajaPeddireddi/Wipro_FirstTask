import xml.etree.ElementTree as ET
root=ET.Element("employee")
emp1=ET.SubElement(root,"employee")
ET.SubElement(emp1,"Id").text="101"
ET.SubElement(emp1,"name").text="ram"

tree = ET.ElementTree(root)
tree.write("test.xml")