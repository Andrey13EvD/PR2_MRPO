import xml.etree.ElementTree as ET
import xml.dom.minidom
from Repository.FakeRepository import FakeRepository
from Models.Recommendations import Recommendations
from Models.Equipment import Equipment
from Models.Exercise import Exercise
from Models.MuscleGroup import MuscleGroup
import xml.etree.ElementTree as ET
from Repository.FakeRepository import FakeRepository
from Models.User import User
from Models.TrainingProgram import TrainingProgram
import xml.etree.ElementTree as ET

class XMLUserRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        users = []
        for user_element in self.root.findall(".//users/user"):
            users.append(self._xml_to_user(user_element))
        return users

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, user: User):
        users_element = self.root.find(".//users")
        if users_element is None:
            users_element = ET.SubElement(self.root, "users")
        new_user_element = ET.SubElement(users_element, "user")
        self._user_to_xml(user, new_user_element)
        self._save_xml()
        print(f"Пользователь {user.name} добавлен с ID={user.id}")

    def remove(self, user: User):
        user_element = self.root.find(".//users/user[id='{}']".format(user.id))
        if user_element is not None:
            self.root.find(".//users").remove(user_element)
            self._save_xml()

    def update(self, user: User):
        user_element = self.get(user.id)
        if user_element is not None:
            self.add(user)
            self.remove(user_element)
            self._save_xml()

    def _xml_to_user(self, user_element) -> User:
        id = int(user_element.find("id").text)
        age = int(user_element.find("age").text)
        gender = user_element.find("gender").text
        weight = float(user_element.find("weight").text)
        height = float(user_element.find("height").text)
        name = user_element.find("name").text
        purpose = user_element.find("purpose").text
        return User(id=id, age=age, gender=gender, weight=weight, height=height, name=name, purpose=purpose)

    def _user_to_xml(self, user: User, user_element):
        id_element = user_element.find("id")
        if id_element is not None:
            id_element.text = str(user.id)
        else:
            id_element = ET.SubElement(user_element, "id")
            id_element.text = str(user.id)

        age_element = user_element.find("age")
        if age_element is not None:
            age_element.text = str(user.age)
        else:
            age_element = ET.SubElement(user_element, "age")
            age_element.text = str(user.age)

        gender_element = user_element.find("gender")
        if gender_element is not None:
            gender_element.text = user.gender
        else:
            gender_element = ET.SubElement(user_element, "gender")
            gender_element.text = user.gender

        weight_element = user_element.find("weight")
        if weight_element is not None:
            weight_element.text = str(user.weight)
        else:
            weight_element = ET.SubElement(user_element, "weight")
            weight_element.text = str(user.weight)

        height_element = user_element.find("height")
        if height_element is not None:
            height_element.text = str(user.height)
        else:
            height_element = ET.SubElement(user_element, "height")
            height_element.text = str(user.height)

        name_element = user_element.find("name")
        if name_element is not None:
            name_element.text = user.name
        else:
            name_element = ET.SubElement(user_element, "name")
            name_element.text = user.name

        purpose_element = user_element.find("purpose")
        if purpose_element is not None:
            purpose_element.text = user.purpose
        else:
            purpose_element = ET.SubElement(user_element, "purpose")
            purpose_element.text = user.purpose

    def get_by_id(self, user_id):
        for user_element in self.root.findall(".//user"):
            id_element = user_element.find("id")
            if id_element is not None and int(id_element.text) == user_id:
                return self._xml_to_user(user_element)
        return None
    def get_by_name(self, user_name):
        for user_element in self.root.findall(".//user"):
            name_element = user_element.find("name")
            if name_element is not None and str(name_element.text) == user_name:
                return self._xml_to_user(user_element)
        return None

class XMLEquipmentRepository(FakeRepository):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        equipments = []
        for equipment_element in self.root.findall(".//equipment/equipments"):
            equipments.append(self._xml_to_dish(equipment_element))
        return equipments

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, equipment):
        equipment_element = self.root.find(".//equipments")
        if equipment_element is None:
            equipment_element = ET.SubElement(self.root, "equipments")
        new_equipment_element = ET.SubElement(equipment_element, "equipment")
        self._equipment_to_xml(equipment, new_equipment_element)
        self._save_xml()

    def remove(self, equipment: Equipment):
        equipment_element = self.root.find(".//equipments/equipment[id='{}']".format(equipment.id))
        if equipment_element is not None:
            self.root.find(".//equipments").remove(equipment_element)
            self._save_xml()

    def update(self, equipment: Equipment):
        equipment_element = self.get(equipment.id)
        if equipment_element is not None:
            self.add(equipment)
            self.remove(equipment_element)
            self._save_xml()

    def _xml_to_equipment(self, equipment_element):
        id = int(equipment_element.find("id").text)
        name = equipment_element.find("name").text
        description = str(equipment_element.find("description").text)

        return Equipment(id=id, name=name, description=description)

    def _equipment_to_xml(self, equipment, equipment_element):
        id_element = ET.SubElement(equipment_element, "id")
        id_element.text = str(equipment.id)

        name_element = ET.SubElement(equipment_element, "name")
        name_element.text = equipment.name

        description_element = ET.SubElement(equipment_element, "description")
        description_element.text = equipment.description


    def get_by_id(self, equipment_id):
        for equipment_element in self.root.findall(".//equipment"):
            id_element = equipment_element.find("id")
            if id_element is not None and int(id_element.text) == equipment_id:
                return self._xml_to_equipment(equipment_element)
        return None

    def get_by_name(self, name):
        for equipment_element in self.root.findall(".//equipment"):
            name_element = equipment_element.find("name")
            if name_element is not None and name_element.text == name:
                return self._xml_to_equipment(equipment_element)
        return None

class XMLRecommendationsRepository(FakeRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        recommendations = []
        for recommendation_element in self.root.findall(".//recommendations/recommendation"):
            recommendations.append(self._xml_to_recommendation(recommendation_element))
        return recommendations

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, recommendation: Recommendations):
        recommendations_element = self.root.find(".//recommendations")
        if recommendations_element is None:
            recommendations_element = ET.SubElement(self.root, "recommendations")
        new_recommendation_element = ET.SubElement(recommendations_element, "recommendation")
        self._recommendation_to_xml(recommendation, new_recommendation_element)
        self._save_xml()

    def remove(self, recommendation: Recommendations):
        recommendation_element = self.root.find(".//recommendations/recommendation[id='{}']".format(recommendation.id))
        if recommendation_element is not None:
            self.root.find(".//recommendations").remove(recommendation_element)
            self._save_xml()

    def _xml_to_recommendation(self, recommendation_element) -> Recommendations:
        id = int(recommendation_element.find("id").text)
        purpose = recommendation_element.find("purpose").text
        recommendations = recommendation_element.find("recommendations").text
        return Recommendations(id=id, purpose=purpose, recommendations=recommendations)

    def _recommendation_to_xml(self, recommendation: Recommendations, recommendation_element):
        id_element = recommendation_element.find("id")
        if id_element is not None:
            id_element.text = str(recommendation.id)
        else:
            id_element = ET.SubElement(recommendation_element, "id")
            id_element.text = str(recommendation.id)

        purpose_element = recommendation_element.find("purpose")
        if purpose_element is not None:
            purpose_element.text = recommendation.purpose
        else:
            purpose_element = ET.SubElement(recommendation_element, "purpose")
            purpose_element.text = recommendation.purpose

        recommendations_element = recommendation_element.find("recommendations")
        if recommendations_element is not None:
            recommendations_element.text = recommendation.recommendations
        else:
            recommendations_element = ET.SubElement(recommendation_element, "recommendations")
            recommendations_element.text = recommendation.recommendations

    def get_by_id(self, recommendation_id):
        for recommendation_element in self.root.findall(".//recommendation"):
            id_element = recommendation_element.find("id")
            if id_element is not None and int(id_element.text) == recommendation_id:
                return self._xml_to_recommendation(recommendation_element)
        return None

class XMLExerciseRepository(FakeRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        exercises = []
        for exercise_element in self.root.findall(".//exercises/exercise"):
            exercises.append(self._xml_to_exercise(exercise_element))
        return exercises

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, exercise: Exercise):
        exercises_element = self.root.find(".//exercises")
        if exercises_element is None:
            exercises_element = ET.SubElement(self.root, "exercises")
        new_exercise_element = ET.SubElement(exercises_element, "exercise")
        self._exercise_to_xml(exercise, new_exercise_element)
        self._save_xml()

    def remove(self, exercise: Exercise):
        exercise_element = self.root.find(".//exercises/exercise[id='{}']".format(exercise.id))
        if exercise_element is not None:
            self.root.find(".//exercises").remove(exercise_element)
            self._save_xml()

    def _xml_to_exercise(self, exercise_element) -> Exercise:
        id = int(exercise_element.find("id").text)
        name = exercise_element.find("name").text
        description = exercise_element.find("description").text
        repetitions = int(exercise_element.find("repetitions").text)
        return Exercise(id=id, name=name, description=description, repetitions=repetitions)

    def _exercise_to_xml(self, exercise: Exercise, exercise_element):
        id_element = exercise_element.find("id")
        if id_element is not None:
            id_element.text = str(exercise.id)
        else:
            id_element = ET.SubElement(exercise_element, "id")
            id_element.text = str(exercise.id)

        name_element = exercise_element.find("name")
        if name_element is not None:
            name_element.text = exercise.name
        else:
            name_element = ET.SubElement(exercise_element, "name")
            name_element.text = exercise.name

        description_element = exercise_element.find("description")
        if description_element is not None:
            description_element.text = exercise.description
        else:
            description_element = ET.SubElement(exercise_element, "description")
            description_element.text = exercise.description

        repetitions_element = exercise_element.find("repetitions")
        if repetitions_element is not None:
            repetitions_element.text = str(exercise.repetitions)
        else:
            repetitions_element = ET.SubElement(exercise_element, "repetitions")
            repetitions_element.text = str(exercise.repetitions)

    def get_by_id(self, exercise_id):
        for exercise_element in self.root.findall(".//exercise"):
            id_element = exercise_element.find("id")
            if id_element is not None and int(id_element.text) == exercise_id:
                return self._xml_to_exercise(exercise_element)
        return None
    def get_by_name(self, exercise_name):
        for exercise_element in self.root.findall(".//exercise"):
            name_element = exercise_element.find("name")
            if name_element is not None and str(name_element.text) == exercise_name:
                return self._xml_to_exercise(exercise_element)
        return None

class XMLMuscleGroupRepository(FakeRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        muscle_groups = []
        for muscle_group_element in self.root.findall(".//muscle_groups/muscle_group"):
            muscle_groups.append(self._xml_to_muscle_group(muscle_group_element))
        return muscle_groups

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, muscle_group: MuscleGroup):
        muscle_groups_element = self.root.find(".//muscle_groups")
        if muscle_groups_element is None:
            muscle_groups_element = ET.SubElement(self.root, "muscle_groups")
        new_muscle_group_element = ET.SubElement(muscle_groups_element, "muscle_group")
        self._muscle_group_to_xml(muscle_group, new_muscle_group_element)
        self._save_xml()

    def remove(self, muscle_group: MuscleGroup):
        muscle_group_element = self.root.find(".//muscle_groups/muscle_group[id='{}']".format(muscle_group.id))
        if muscle_group_element is not None:
            self.root.find(".//muscle_groups").remove(muscle_group_element)
            self._save_xml()

    def _xml_to_muscle_group(self, muscle_group_element) -> MuscleGroup:
        id = int(muscle_group_element.find("id").text)
        name = muscle_group_element.find("name").text
        category = muscle_group_element.find("category").text
        return MuscleGroup(id=id, name=name, category=category)

    def _muscle_group_to_xml(self, muscle_group: MuscleGroup, muscle_group_element):
        id_element = muscle_group_element.find("id")
        if id_element is not None:
            id_element.text = str(muscle_group.id)
        else:
            id_element = ET.SubElement(muscle_group_element, "id")
            id_element.text = str(muscle_group.id)

        name_element = muscle_group_element.find("name")
        if name_element is not None:
            name_element.text = muscle_group.name
        else:
            name_element = ET.SubElement(muscle_group_element, "name")
            name_element.text = muscle_group.name

        category_element = muscle_group_element.find("category")
        if category_element is not None:
            category_element.text = muscle_group.category
        else:
            category_element = ET.SubElement(muscle_group_element, "category")
            category_element.text = muscle_group.category

    def get_by_id(self, muscle_group_id):
        for muscle_group_element in self.root.findall(".//muscle_group"):
            id_element = muscle_group_element.find("id")
            if id_element is not None and int(id_element.text) == muscle_group_id:
                return self._xml_to_muscle_group(muscle_group_element)
        return None
    def get_by_name(self, muscle_group_name):
        for muscle_group_element in self.root.findall(".//muscle_group"):
            name_element = muscle_group_element.find("name")
            if name_element is not None and str(name_element.text) == muscle_group_name:
                return self._xml_to_muscle_group(muscle_group_element)
        return None

class XMLTrainingProgramRepository(FakeRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def get_all(self):
        programs = []
        for program_element in self.root.findall(".//programs/program"):
            programs.append(self._xml_to_training_program(program_element))
        return programs

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def add(self, program: TrainingProgram):
        programs_element = self.root.find(".//programs")
        if programs_element is None:
            programs_element = ET.SubElement(self.root, "programs")
        new_program_element = ET.SubElement(programs_element, "program")
        self._training_program_to_xml(program, new_program_element)
        self._save_xml()

    def remove(self, program: TrainingProgram):
        program_element = self.root.find(".//programs/program[id='{}']".format(program.id))
        if program_element is not None:
            self.root.find(".//programs").remove(program_element)
            self._save_xml()

    def _xml_to_training_program(self, program_element) -> TrainingProgram:
        id = int(program_element.find("id").text)
        week_day = program_element.find("week_day").text
        exercises = []
        exercises_element = program_element.find("exercises")
        if exercises_element is not None:
            for exercise_element in exercises_element.findall("exercise"):
                exercise_id = int(exercise_element.find("id").text)
                name = exercise_element.find("name").text
                description = exercise_element.find("description").text
                repetitions = int(exercise_element.find("repetitions").text)
                exercises.append(Exercise(id=exercise_id, name=name, description=description, repetitions=repetitions))
        return TrainingProgram(id=id, week_day=week_day, exercises=exercises)

    def _training_program_to_xml(self, program: TrainingProgram, program_element):
        id_element = program_element.find("id")
        if id_element is not None:
            id_element.text = str(program.id)
        else:
            id_element = ET.SubElement(program_element, "id")
            id_element.text = str(program.id)

        week_day_element = program_element.find("week_day")
        if week_day_element is not None:
            week_day_element.text = program.week_day
        else:
            week_day_element = ET.SubElement(program_element, "week_day")
            week_day_element.text = program.week_day

        exercises_element = program_element.find("exercises")
        if exercises_element is None:
            exercises_element = ET.SubElement(program_element, "exercises")
        else:
            exercises_element.clear()

        for exercise in program.exercises:
            exercise_element = ET.SubElement(exercises_element, "exercise")
            exercise_id_element = ET.SubElement(exercise_element, "id")
            exercise_id_element.text = str(exercise.id)
            name_element = ET.SubElement(exercise_element, "name")
            name_element.text = exercise.name
            description_element = ET.SubElement(exercise_element, "description")
            description_element.text = exercise.description
            repetitions_element = ET.SubElement(exercise_element, "repetitions")
            repetitions_element.text = str(exercise.repetitions)

    def get_by_id(self, program_id):
        for program_element in self.root.findall(".//program"):
            id_element = program_element.find("id")
            if id_element is not None and int(id_element.text) == program_id:
                return self._xml_to_training_program(program_element)
        return None
