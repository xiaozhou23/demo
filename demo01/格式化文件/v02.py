import xml.etree.ElementTree
from collections import Iterable
from collections import Iterator

root = xml.etree.ElementTree.parse("school.xml")
root_iter =root.iter()
nodes = root.getiterator()
print(type(nodes))
print(isinstance(root_iter, Iterable))
print(isinstance(root_iter, Iterator))

for i in root_iter:
    print(i)

for node in nodes:
    print("{0}--{1}--{2}".format(node.tag, node.text, node.attrib))

print("-" * 30)

ele_teacher = root.find("Teacher")
print(type(ele_teacher))
for node in ele_teacher:
    print("{0}--{1}--{2}".format(node.tag, node.text, node.attrib))

print("-" * 30)

ele_student = root.findall("Student")
print(type(ele_student))
for node in ele_student:
    print("{0}--{1}--{2}".format(node.tag, node.text, node.attrib))
    for sub in node.getiterator():
        print("{0}--{1}".format(sub.tag, sub.text))
