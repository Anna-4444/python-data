import matplotlib.pyplot as plt;

snack_scores = [80, 60, 40]
slice_labels = ["Reese's", "Fritos", "pistachios"]
colors = ["orange", "yellow", "green"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)
plt.title("My favorite snacks")
plt.savefig("fav-snacks.png")

