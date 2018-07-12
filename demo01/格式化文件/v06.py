import xml.etree.ElementTree as et

etree = et.ElementTree()

e = et.Element('Student')

etree._setroot(e)

e_name = et.SubElement(e, 'Name')
e_name.text = 'jim'

etree.write("Student.xml")