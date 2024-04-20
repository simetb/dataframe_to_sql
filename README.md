# Data frame to sql

## Overview
This Python program converts data from a DataFrame into a SQL file containing INSERT queries for a specified table. It's useful for quickly generating SQL scripts from DataFrame data.

## Requirements
Ensure you have the following packages installed in your Python environment. You can install them via `pip install -r requirements.txt`.

## Usage
1. Import the necessary libraries:
    ```python
    import pandas as pd
    import data_frame_to_sql_insert as dts
    ```

2. Read your data into a DataFrame:
    ```python
    example = pd.read_csv('example.csv')
    ```

3. Call the `data_frame_to_sql_insert` function with the appropriate parameters:
    ```python
    dts.data_frame_to_sql_insert(data_frame=example, table='table_to_insert', sql_file_name='file_name')
    ```

    - `data_frame`: The DataFrame containing the data to be converted.
    - `table`: The name of the table in the SQL database.
    - `sql_file_name`: The name of the SQL file to be created.

4. The program will generate an SQL file (`file_name.sql`) with INSERT queries based on the DataFrame data.
