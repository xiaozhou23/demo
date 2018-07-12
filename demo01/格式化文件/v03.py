import xml.etree.ElementTree as et

tree = et.parse(r'to_edit.xml')

root = tree.getroot()
print(type(root))

ele = root.iter("Name")
print(type(ele))
for i in ele:
    print(i.text)
print("-" * 30)

for stu in root.iter("Student"):
    name = stu.find("Name")
    print(name.text)
    if name != None:
        print(name.text)
        name.set("test", name.text * 2)

stu1 = root.find("Student")
e = et.Element("Addr")
e.attrib = {'a':'b'}
e.text = "address"
stu1.append(e)

tree.write('to_edit.xml')