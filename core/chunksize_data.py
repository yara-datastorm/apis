import pandas as pd

def chunksize_data(data_url,sep,chuncksize=1000):
    # chuncksize
    chunks = pd.read_csv(filepath_or_buffer=data_url, sep=sep, chunksize=chuncksize)  # the number of rows per chunk

    df = []
    for dframe in chunks:
        df.append(dframe)

    df = pd.concat(df,sort=False)
    return df
