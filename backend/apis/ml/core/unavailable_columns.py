def unavailable_columns(dataframe, seuil=0.25) -> list:
    """
    missing value > 25%
    """
    try:
        df_int = dataframe.isnull().sum()
        df_int = df_int.to_frame("missing").reset_index()
        print(df_int)

        columns_delete = df_int['index'][df_int["missing"] > dataframe.shape[0]*seuil].values
        return list(columns_delete)
    except Exception as ex:
        raise('something wrong')