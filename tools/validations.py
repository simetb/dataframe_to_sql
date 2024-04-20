from .message_format import (error_message, DataFrameSQLError)
import pandas as pd

# Function that validates if a given data frame is a pandas.DataFrame.
def validate_dataframe(data_frame) -> bool:
    if(isinstance(data_frame,pd.DataFrame)):
        return True
    raise DataFrameSQLError(error_message("001", "DATA_FRAME", "DATA_FRAME must be a valid pandas.DataFrame"))

# Function that validates if a given table is a string.
def validate_table(table) -> bool:
    if(isinstance(table, str)):
        return True
    raise DataFrameSQLError(error_message("002", "TABLE", "TABLE must be a string"))

# Function that validates if a given SQL file name is a string.
def validate_sql_file_name(sql_name) -> bool:
    if(isinstance(sql_name, str)):
        return True
    raise DataFrameSQLError(error_message("003", "SQL_FILE_NAME", "SQL_FILE_NAME must be a string"))