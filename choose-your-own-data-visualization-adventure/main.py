import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")
# print(df.columns)

def remove_outliers_iqr(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return dataframe[(dataframe[column] >= lower) & (dataframe[column] <= upper)]

df_clean = remove_outliers_iqr(df, "# num_pages")
df_clean = remove_outliers_iqr(df_clean, "ratings_count")

sns.scatterplot(x="average_rating", y="# num_pages", hue="ratings_count", data=df_clean)
plt.xlabel("Average Rating")
plt.ylabel("Number of Pages")
plt.title("Book Length and Average Rating")
plt.legend(title="Number of Ratings")
plt.savefig("book-length-rating.png")

