from .message_format import (DataFrameSQLError,error_message, warning_message, info_message)
from .validations import * 
import pandas as pd

# Functions to create sql files with transformed dataframes data.
def _create_sql_file(query: str, sql_file_name: str) -> None:
    """
    This function creates a sql file with the provided query.
    
    Args:
        query (str): query to insert.
        sql_file_name (str): file name.
    
    Returns:
        none (create a new file with the query)
    """
    info_message(f"creating {sql_file_name}.sql file")
    with open(f"{sql_file_name}.sql", "w") as file:
        file.write(query)
    info_message(f"{sql_file_name}.sql created")
    pass

# Function that process a dataframe and creates a sql query with the data
def data_frame_to_sql_insert(data_frame: pd.DataFrame, table: str, sql_file_name: str = "") -> None:
    """
    This function process a dataframe and creates a sql query
    
    Args:
        data_frame (pandas.Dataframe): query to insert.
        table (str): file name.
        sql_file_name (str): file name.
    
    Returns:
        none
    """
    try:
        validate_dataframe(data_frame)
        validate_table(table)
        validate_sql_file_name(sql_file_name)
        info_message("processing dataframe")
        _dataframe_colums = data_frame.columns.to_list()        
        _insert = F"INSERT INTO '{table}' ({', '.join(_dataframe_colums)}) VALUES "
        _insert_data = ""  
        for _, row in data_frame.iterrows():
            _insert_data += "("
            for column in data_frame.columns:
                _insert_data += f"'{row[column]}',"
            _insert_data = _insert_data[:-1] + "),"
        _insert_data = _insert_data[:-1]
        _query = _insert + _insert_data
        
        if sql_file_name == "": 
            warning_message("sql_name_not_provided, chosing dataframe_sql_insert as default")
            sql_file_name = "dataframe_sql_insert" 
        
        _create_sql_file(_query, sql_file_name)
        
    except DataFrameSQLError as error:
        print(error)
    
    except Exception as error:
        print(error_message("000","UNDEFINED", error))    

