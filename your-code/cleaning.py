import pandas as pd

def drop_missing_values(df, columns):

    return df.dropna(subset=columns)

def remove_percentage(df,column):
    df[column] = df[column].str.replace('%', '').astype(float)

def drop_columns(df, columns):

    columns_to_drop = [col for col in columns if col in df.columns]

    return df.drop(columns_to_drop, axis=1)

def fill_missing_values(df, column, method='mean'):

    if method == 'mean':
        fill_value = df[column].mean()
    elif method == 'median':
        fill_value = df[column].median()
    elif method == 'mode':
        fill_value = df[column].mode()[0]
    else:
        raise ValueError("Method must be 'mean', 'median', or 'mode'.")

    df[column] = df[column].fillna(fill_value)
    return df

def standardize_column_names(df):

    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def remove_duplicates(df):

    return df.drop_duplicates()

def unique_values_for_categorical(df, max_unique_limit=None):
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    unique_values = {}

    for column in categorical_columns:
        unique_vals = df[column].unique()
        if max_unique_limit is not None and len(unique_vals) > max_unique_limit:
            print(f'{column} uniques: more than {max_unique_limit} values')
        else:
            print(f'{column} uniques: {unique_vals}')

import pandas as pd

def drop_columns_with_missing_data(df, threshold=0.10):
    """
    Drops columns from a DataFrame where the percentage of missing data is greater than a specified threshold.

    Parameters:
    - df: pandas DataFrame from which to remove columns.
    - threshold: float, the threshold for dropping columns. Default is 0.10 for 10%.
    
    Returns:
    - DataFrame with columns dropped based on the missing data threshold.
    """
    # Calculate the percentage of missing data for each column
    missing_percentage = df.isnull().sum() / len(df)
    
    # Find columns where the missing percentage is greater than the threshold
    columns_to_drop = missing_percentage[missing_percentage > threshold].index
    # Drop these columns from the DataFrame
    df_dropped = df.drop(columns=columns_to_drop)
    print(f'Dropped columns: {columns_to_drop}')
    return df_dropped

import pandas as pd

def standardize_values(df, columns, to_lower=True):
    """
    Standardize string values in specified columns of a DataFrame to either
    lowercase or uppercase.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data to be standardized.
    - columns (list of str or str): The column(s) in the DataFrame to standardize.
    - to_lower (bool, optional): If True, standardize to lowercase. If False, standardize to uppercase.
      Defaults to True.

    Returns:
    - pd.DataFrame: The DataFrame with standardized values in the specified columns.
    """
    
    # Ensure 'columns' is a list even if a single column name is provided
    if isinstance(columns, str):
        columns = [columns]
    
    # Iterate over the specified columns and standardize values
    for column in columns:
        if to_lower:
            df[column] = df[column].str.lower()
        else:
            df[column] = df[column].str.upper()
    
    return df

# Example usage:
# df = standardize_values(df, ['column1', 'column2'], to_lower=False)



if __name__ == "__main__":

    data = {'Name': ['Alice', 'Bob', None, 'David', 'Alice'],
            'Age': [25, 30, 35, 40, '25']}
    df = pd.DataFrame(data)

    df = drop_missing_values(df, ['Name'])
    df = fill_missing_values(df, 'Age', method='median')
    df = standardize_column_names(df)
    df = remove_duplicates(df)

    print(df)
