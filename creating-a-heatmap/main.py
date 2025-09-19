import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

tips = pd.read_csv("tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"] * 100
tips_pivoted = tips.pivot_table(index="time", columns="size", values="tip_pct")
sns.heatmap(tips_pivoted, annot=True, fmt=".1f", cmap="coolwarm")
plt.title("Tip Percentage based on Party Size and Meal")
plt.xlabel("Party Size")
plt.ylabel("Meal")
plt.savefig("tips.png")
