# Custom DataFrameToSql errors Exceptions.
class DataFrameSQLError (Exception):
    def __init__(self, message : str):
        self.message = "DataFrameToSql " + message
        super().__init__(self.message)

# Function to return a general error message.
def error_message(
    code:str,
    type:str,
    description:str) -> str:
    _general_error = f"ERROR: {description}, type: {type}, code: {code}"
    return _general_error

# Function to return a general warning message.
def warning_message(
    description:str) -> None:
    _general_warning = f"WARNING: {description}"
    print(_general_warning)

# Function to return a general info message.
def info_message(
    description:str) -> None:
    _general_warning = f"INFO: {description}"
    print(_general_warning)
    
