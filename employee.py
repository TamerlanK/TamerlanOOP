class Employee:
    def __init__(self, name: str, job: str, salary: float, age: int, work_duration: int):
        self._name = name
        self._job = job
        self._salary = salary
        self._age = age
        self._work_duration = work_duration

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value:str):
        self._job = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    @property
    def work_duration(self):
        return self._work_duration

    @work_duration.setter
    def work_duration(self, value: int):
        self._work_duration = value

    def index(self):
        effectivity = self._salary / self._work_duration
        return f"{self._name}'s effectivity = {effectivity:.2f}"





