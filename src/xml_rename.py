import argparse
import os
import glob
import xml.etree.ElementTree as ET


def formal_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename')
    file_image = filename.text
    file_xml = os.path.split(xml_file)
    xml_n = file_xml[-1].split(".")[0]
    if file_image.split(".")[0] != xml_n:
        print('renaming: ', file_image, file_xml)
        filename.text = xml_n + '.jpg'

    tree.write(xml_file)



def args_input():
    parser = argparse.ArgumentParser(description="Give scale and folder to format xml with stretch")
    parser.add_argument("-f", "--folder", default="images", help="Specify folder from runnable")
    return parser.parse_args()


def main():
    args = args_input()

    image_path = os.path.join(os.getcwd(), args.folder)
    print('Calling script with: ')
    print(f'path = {image_path}')

    xmls = glob.glob(image_path + '/*.xml')
    length = len(xmls)
    if length == 0:
        raise Exception("No files provided")

    for xml_file in xmls:
        formal_xml(xml_file)
    print(f'Successfully checked {length} xml')


main()

