import pandas as pd

DATA_PATH = 'data_frames/final_df.csv'

# load data
df = pd.read_csv(DATA_PATH)

# change mode, genre and key features to binary columns
tmp_mode=pd.get_dummies(df['mode'])
tmp_key=pd.get_dummies(df['key'])

df=pd.concat((df,tmp_mode,tmp_key),axis=1)

# drop unused columns
df=df.drop(['key','mode','track_name', 'Unnamed: 0'], axis=1)

# change track_id and genre to numerical values
df[['track_id', 'genre']] = \
    df[['track_id', 'genre']].apply(lambda col: pd.factorize(col, sort=True)[0])

# drop all rows that contain & in their artist_name
tmp=df['artist_name'].str.contains('&')
indexNames = df[ df['artist_name'].str.contains('&') ].index
df.drop(indexNames , inplace=True)

df[['artist_name']] = \
    df[['artist_name']].apply(lambda col: pd.factorize(col, sort=True)[0])


# save final data-frame to csv
df.to_csv('data_frames/df_prep.csv')

df_ts1 = df[df['time_signature'] == 1]
df_ts3 = df[df['time_signature'] == 3]
df_ts4 = df[df['time_signature'] == 4]
df_ts5 = df[df['time_signature'] == 5]

df_ts1.to_csv('data_frames/df_ts1_prep.csv')
df_ts3.to_csv('data_frames/df_ts3_prep.csv')
df_ts4.to_csv('data_frames/df_ts4_prep.csv')
df_ts5.to_csv('data_frames/df_ts5_prep.csv')