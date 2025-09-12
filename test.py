class Employee:
    __slots__ = ["name", "age", "position"]

    def __init__(self, name, age, position):
        """
        Initialize an Employee instance.

        Args:
            name (str): The employee's name
            age (int): The employee's age
            position (str): The employee's job position
        """
        self.name = name
        self.age = age
        self.position = position


class Developer(Employee):
    def __init__(self, name, age, salary, framework):
        """
        Initialize a Developer instance.

        Args:
            name (str): The developer's name
            age (int): The developer's age
            salary (int): The developer's salary
            framework (str): The development framework the developer specializes in
        """
        super().__init__(name, age, salary)
        self.framework = framework


def main():
    """
    Main function to demonstrate the Employee and Developer classes.

    Creates a Developer instance and prints their information.
    """
    newEmployee = Developer("Alice", 30, 80000, "Django")
    print(
        f"Name: {newEmployee.name}, Age: {newEmployee.age}, Position: {newEmployee.position}, Framework: {newEmployee.framework}"
    )


if __name__ == "__main__":
    main()
