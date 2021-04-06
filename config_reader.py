from errors.ConfigErrors import *


class Config:
    def __init__(self, file_path="./edith.config"):
        self.file_path = file_path
        self.source = self.get_source()
        self.config = self.parse()

    def get_source(self):
        with open(self.file_path, 'r') as f:
            source = f.read()
        return source

    @staticmethod
    def is_valid_var(var: str):
        if not var[0].isnumeric():
            return var.replace("_", "").isalnum()
        return False

    @staticmethod
    def remove_spaces(string):
        string = string.replace(" =", "=")
        string = string.replace("= ", "=")
        return string

    def parse(self):
        config = {}
        for i, statement in enumerate(self.source.split("\n")):
            if "=" not in statement[::len(statement)-1]:
                lexemes = self.remove_spaces(statement).split("=")
                if len(lexemes) == 2:
                    var_name, var_value = lexemes[0], lexemes[1]
                    if self.is_valid_var(var_name):
                        config[var_name] = var_value
                    else:
                        raise InvalidVarNameError(i, extra_args=var_name)
                else:
                    raise MultipleAssignmentError(i)
            else:
                raise InvalidVarNameError(i, extra_args=statement.split("=")[0])
        return config
