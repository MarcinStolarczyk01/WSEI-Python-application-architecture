import re
import logging


class EmailValidator:
    def __set__(self, instance, value):
        if not re.match(r"^[a-zA-Z0-9._%+-]+@wsei.edu.pl", value):
            raise ValueError("Bad mail")


class Student:
    email = EmailValidator()

    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email


# todo: task 3
class ActionLogger:
    logging.basicConfig(level="INFO")
    __logger = logging.getLogger(__file__)

    def __set_name__(self, owner, name):
        self._attr_name = name

    def __set__(self, instance, value):
        self.__logger.info(f"Setting {self._attr_name} to value: {value}")
        instance.__dict__[self._attr_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.__logger.info(
            f"Getting {self._attr_name} value equal: {instance.__dict__.get(self._attr_name)}"
        )
        return instance.__dict__.get(self._attr_name)


class User:
    name = ActionLogger()
    age = ActionLogger()

    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    # s = Student('Marcin', 'Stolarczyk', 'marcin.stolarczyk@wsei.edu.pl')
    user = User("Marcin", 23)
    age = user.age
    name = user.name


if __name__ == "__main__":
    main()
