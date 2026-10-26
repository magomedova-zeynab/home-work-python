from functools import wraps


class Command:
    def __init__(self, value):
        self.value = value

    def apply(self, current):
        raise NotImplementedError

    def name(self):
        return type(self).__name__.replace("Command", "").lower()


class AddCommand(Command):
    def apply(self, current):
        return current + self.value


class MultiplyCommand(Command):
    def apply(self, current):
        return current * self.value


class SubtractCommand(Command):
    def apply(self, current):
        return current - self.value


class DivideCommand(Command):
    def apply(self, current):
        if self.value == 0:
            raise ZeroDivisionError("деление на ноль")
        return current / self.value


COMMANDS = {
    "add": AddCommand,
    "multiply": MultiplyCommand,
    "subtract": SubtractCommand,
    "divide": DivideCommand,
}


def log_command(func):
    @wraps(func)
    def wrapper(self, command, *args, **kwargs):
        print(f"[LOG] {command.name()} {command.value}")
        return func(self, command, *args, **kwargs)

    return wrapper


class CommandProcessor:
    def __init__(self):
        self.value = 0
        self.history = []

    @log_command
    def execute(self, command):
        self.value = command.apply(self.value)
        self.history.append((command.name(), command.value, self.value))
        return self.value

    def handle(self, line):
        line = line.strip()

        if line == "exit":
            return False
        if line == "history":
            for item in self.history:
                print(item)
            return True

        parts = line.split()
        if len(parts) != 2 or parts[0] not in COMMANDS:
            print("Неизвестная или некорректная команда")
            return True

        try:
            command = COMMANDS[parts[0]](int(parts[1]))
            print("Результат:", self.execute(command))
        except ValueError:
            print("Аргумент должен быть целым числом")
        except ZeroDivisionError as error:
            print("Ошибка:", error)

        return True

    def run(self):
        print("Команды: add/multiply/subtract/divide <число>, history, exit")
        while self.handle(input("> ")):
            pass


if __name__ == "__main__":
    CommandProcessor().run()