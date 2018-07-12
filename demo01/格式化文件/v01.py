import xml.dom.minidom

from xml.dom.minidom import parse

DOMtree = parse("school.xml")
doc = DOMtree.documentElement

print("Root Nodename is {0}".format(doc.nodeName))
Attr = doc.getAttribute("type")
print(Attr)

v = doc.childNodes[1].childNodes[1]
v1 = v.childNodes[0].nodeValue
    #.nodeValue
print(v)
print(v1)

print("-" * 30)
for ele in doc.childNodes:
    if ele.nodeName == "Teacher":
        print("Node: {0}".format(ele.nodeName))
        child = ele.childNodes
        for i in child:
            if i.nodeName == "Name":
                print("Name is {0}".format(i.childNodes[0].data))
            if i.nodeName == "Course":
                print("Course is {0}".format(i.childNodes[0].data))
            if i.nodeName == "Age":
                print("Age is {0}".format(i.childNodes[0].nodeValue))
                if i.hasAttribute("detail"):
                    print("Age detail is {0}".format(i.getAttribute("detail")))
        print("Nodeid is {0}".format(ele.getAttribute("id")))