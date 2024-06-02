from FakeRepository import FakeRepository
import xml.etree.ElementTree as ET


class XmlRepository(FakeRepository):

    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.root = None

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def get_all(self):
        pass

    def get_by_id(self, name):
        pass

    def load_data(self):
        self.tree = ET.parse(self.file_path)
        self.root = self.tree.getroot()

    def save_data(self):
        self.tree.write(self.file_path)

    def get_element_by_xpath(self, xpath_expression):
        return self.root.find(xpath_expression)

    def set_element_value_by_xpath(self, xpath_expression, value):
        element = self.root.find(xpath_expression)
        if element is not None:
            element.text = value