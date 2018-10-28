import pandas as pd

# url = "http://sentdex.com/api/finance/sentiment-signals/sample/"
# df2 = pd.read_csv(url)
# df2.to_csv("test.csv")
df = pd.read_csv("finalcsv.csv")
maxx = -4

# print(df.sort_values(by='sentiment', ascending=False))
df3 = df.sort_values(by='sentiment', ascending=False)
# print(df3)
df_top = df3.head(10)
df_bot = df3.tail(10)
df_top.to_csv("topsent.csv")
df_bot.to_csv("botsent.csv")
print(df_top)
print(df_bot)
