class BuilderException(Exception):
    message = "Unknown Error"

    def __init__(self, message=None):
        message = message if message else self.message
        super().__init__(message)

    def get_message(self):
        return self.message


class DoesNotExist(BuilderException):
    message = "Object does not exist"

    def __init__(self, object_name="", object_class_name="Object"):
        self.message = f"{object_class_name} named '{object_name}' does not exist"
        super().__init__()


class TooManyValuesError(BuilderException):
    message = "Too many values to unpack"

    def __init__(self, object_name="", object_class_name="Object"):
        self.message = f"{object_class_name} named '{object_name}' found more than one"
        super().__init__()


#
class BuildDoesNotExist(DoesNotExist):
    def __init__(self, object_name=""):
        super().__init__(object_name, "Build")


class BuildTooManyValuesError(TooManyValuesError):
    def __init__(self, object_name=""):
        super().__init__(object_name, "Build")


class TaskDoesNotExist(DoesNotExist):
    def __init__(self, object_name=""):
        super().__init__(object_name, "Task")


class TaskTooManyValuesError(TooManyValuesError):
    def __init__(self, object_name=""):
        super().__init__(object_name, "Task")
