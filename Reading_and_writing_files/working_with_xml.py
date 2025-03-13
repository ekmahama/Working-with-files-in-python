import xml.etree.cElementTree as ET

def parse_xml_et(fn):
    tree = ET.parse(fn)
    root = tree.getroot()
    print(f'Domains for : {root.attrib["name"]}')
    for child in root:
        print(f'\t {child.attrib["name"]}, {child.tag}')

def add_xml_element_et(fn, el, attr, val):
    tree = ET.parse(fn)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(fn)

def change_xml_element_et(fn, el, attr, oldVal, newVal):
    tree = ET.parse(fn)
    root = tree.getroot()
    ch = "./" + el + "[@" + attr + "='" + oldVal + "']"
    print(ch)
    child = root.find("./" + el + "[@" + attr + "='" + oldVal + "']")
    child.attrib[attr] = newVal
    tree.write(fn)


# parse_xml_et('./files_to_read/ef_author.xml')
# add_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java')
change_xml_element_et('./files_to_read/ef_author.xml','domain', 'name', 'Java', 'C#')
