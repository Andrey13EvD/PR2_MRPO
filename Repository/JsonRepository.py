from Repository.FakeRepository import FakeRepository
import json


class JsonRepository(FakeRepository):

    def __init__(self, file_path):
        self.file_path = file_path

    def serialize(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def deserialize(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def add(self, obj):
        data = self.deserialize()
        if data is None:
            data = []

        class_name = obj.__class__.__name__
        obj_id = str(obj.id)
        obj_data = obj.__dict__



        if class_name not in data:
            data[class_name] = {}

        if obj_id in data[class_name]:
            print(f"Object with id {obj_id} already exists in class {class_name}. Skipping...")
            return

        if obj_id not in data[class_name]:
            data[class_name][obj_id] = {'data': obj_data}
        self.serialize(data)

    def remove(self, obj):
        data = self.deserialize()
        if data is None:
            print("No data found.")
            return

        class_name = obj.__class__.__name__
        obj_id = str(obj.id)  # Преобразование ID в строку для корректного сравнения

        if class_name not in data:
            print(f"No objects of type {class_name} found.")
            return

        if obj_id not in data[class_name]:
            print(f"No object with id {obj_id} found in class {class_name}.")
            return

        del data[class_name][obj_id]

        self.serialize(data)

    def get_all(self):
        data = self.deserialize()
        if data is None:
            print("No data found.")
            return []

        # Преобразование словаря в список объектов
        all_objects = []
        for class_name, objects in data.items():
            for obj_id, obj_data in objects.items():
                obj = self._create_object_from_dict(class_name, obj_id, obj_data)
                all_objects.append(obj)

        return all_objects

    def get_by_id(self, name):
        pass