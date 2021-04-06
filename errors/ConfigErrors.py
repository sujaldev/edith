class ConfigError(Exception):
    def __init__(self, line_no, extra_args="", file_path="./edith.config"):
        self.extra_args = extra_args
        self.error_msg = self.get_error_msg()
        self.display = f' {self.error_msg} Error in "{file_path}" on line "{line_no}" '
        super().__init__(self.display)

    @staticmethod
    def get_error_msg():
        return "Syntax Error: ==> Invalid syntax ==> "


class MultipleAssignmentError(ConfigError):
    @staticmethod
    def get_error_msg():
        return "Syntax Error: ==> Found Multiple assignment operators in one statement ==> "


class InvalidVarNameError(ConfigError):
    def get_error_msg(self):
        return "Syntax Error ==> {} is not a valid variable name ==> ".format(f'"{self.extra_args}"')
