import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = 'SpotifyFeatures.csv'

# load our dataset from kaggle- https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db
df = pd.read_csv(DATA_PATH)

# mean and median of the dataset in general
to_ms=60000 #1 min= 60,000 ms
print('\nMean Duration of a Track:', '%.2f' %(df['duration_ms'].describe()['mean']/to_ms), 'Minutes')
print('Median Duration of a Track:', '%.2f' %(df['duration_ms'].describe()['50%']/to_ms), 'Minutes')

# correlations
df.loc[df["time_signature"] == '0/4', "time_signature"] = 0
df.loc[df["time_signature"] == '1/4', "time_signature"] = 1
df.loc[df["time_signature"] == '3/4', "time_signature"] = 3
df.loc[df["time_signature"] == '4/4', "time_signature"] = 4
df.loc[df["time_signature"] == '5/4', "time_signature"] = 5

# reducing the dataset to all track under 4 minutes
df_4=df[df.duration_ms< 4*to_ms]
print('under 4 minutes tracks',df_4.shape[0])

mapping_2 = {'0': 0, '1': 1, '3': 3, '4': 4, '5': 5}
df_4['time_signature'] = df_4['time_signature'].replace(mapping_2)

sub_df = df_4[['liveness', 'danceability', 'time_signature', 'popularity', 'loudness']]

# calculate the correlation matrix
print('correlations', df_4.corr())
corr = sub_df.corr()

sns_plot = sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
plt.xticks(rotation=50)
plt.yticks(rotation=0)
plt.tight_layout()
#plt.show()
plt.savefig('figs/correlations.png')
plt.clf()

# features distributions
sns.distplot(df_4['danceability']).set_title('Danceability Distribution')
plt.savefig('figs/danceability_dist')
#plt.show()
sns.distplot(df_4['liveness']).set_title('Liveness Distribution')
plt.savefig('figs/liveness_dist')
#plt.show()
df_4['time_signature'].value_counts().plot.pie(autopct="%.1f%%")
plt.legend()
plt.savefig('figs/time_signature_dist')
#plt.show()

# features distributions based on time-signature
# treatment and control histograms
conditions_liveness=[(df_4['liveness']>=0.495),(df_4['liveness']<0.495)]
conditions_danceability=[(df_4['danceability']>=0.465),(df_4['danceability']<0.465)]
values=[1,0]

df_4['liveness_binary'] = np.select(conditions_liveness, values)
df_4['danceability_binary'] = np.select(conditions_danceability, values)
print(df_4)
df_ts1 = df_4[df_4['time_signature'] == 1]
df_ts3 = df_4[df_4['time_signature'] == 3]
df_ts4 = df_4[df_4['time_signature'] == 4]
df_ts5 = df_4[df_4['time_signature'] == 5]

i=1
for df_ts in [df_ts1, df_ts3, df_ts4, df_ts5]:
    df_ts_va_treated = df_ts[df_ts['liveness_binary'] == 1]
    df_ts_va_control = df_ts[df_ts['liveness_binary'] == 0]
    plt.hist(df_ts_va_treated["popularity"].values, alpha=0.5, label='Treated', color='red')
    plt.hist(df_ts_va_control["popularity"].values, alpha=0.5, label='Control', color='blue')
    plt.xlabel('popularity')
    plt.ylabel('Number of Indices')
    plt.legend(loc='upper right')
    plt.title('liveness %.0f' %i)
    plt.savefig('figs/liveness %.0f _binary_dist' %i)
    #plt.show()

    df_ts_va_treated = df_ts[df_ts['danceability_binary'] == 1]
    df_ts_va_control = df_ts[df_ts['danceability_binary'] == 0]
    plt.hist(df_ts_va_treated["popularity"].values, alpha=0.5, label='Treated', color='red')
    plt.hist(df_ts_va_control["popularity"].values, alpha=0.5, label='Control', color='blue')
    plt.xlabel('popularity')
    plt.ylabel('Number of Indices')
    plt.legend(loc='upper right')
    plt.title('danceability %.0f' %i)
    plt.savefig('figs/danceability %.0f _binary_dist' % i)
    #plt.show()

    i+=1

# pie plots for binary danceability and liveness
fig, axs = plt.subplots(2, 2)
df_ts1['danceability_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[0,0]).set_title('1/4')
df_ts3['danceability_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[0,1]).set_title('3/4')
df_ts4['danceability_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[1,0]).set_title('4/4')
df_ts5['danceability_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[1,1]).set_title('5/4')
plt.savefig('figs/danceability_binary_pie')
#plt.show()


fig, axs = plt.subplots(2, 2)
df_ts1['liveness_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[0,0]).set_title('1/4')
df_ts3['liveness_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[0,1]).set_title('3/4')
df_ts4['liveness_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[1,0]).set_title('4/4')
df_ts5['liveness_binary'].value_counts().plot.pie(autopct="%.1f%%", ax=axs[1,1]).set_title('5/4')
plt.savefig('figs/liveness_binary_pie')
#plt.show()


# save the final dataframe as csv
df_4.to_csv('data_frames/final_df.csv')