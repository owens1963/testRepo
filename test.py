class Employee:
    __slots__ = ["name", "age", "position"]

    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position


class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework


def main():
    newEmployee = Developer("Alice", 30, 80000, "Django")
    print(
        f"Name: {newEmployee.name}, Age: {newEmployee.age}, Position: {newEmployee.position}, Framework: {newEmployee.framework}"
    )


if __name__ == "__main__":
    main()
