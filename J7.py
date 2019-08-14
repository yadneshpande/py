import seaborn as sns

df = sns.load_dataset('flights')
df2 = df.pivot('year','month','passengers')


sns.heatmap(df2).get_figure().savefig('h1.png')
