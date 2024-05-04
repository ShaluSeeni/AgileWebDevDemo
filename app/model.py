
class Student:

    def __init__(self, uwaId:str, name:str) -> None:
        self.uwaId = uwaId 
        self.name:str = name

class Group:

    def __init__(self, students: list[Student]) -> None:
        self.students: list[Student] = students

