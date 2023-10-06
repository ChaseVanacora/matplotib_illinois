import matplotlib.pyplot as plt
import numpy as np

plt.style.use("Solarize_Light2")
plt.title("Age to Population Ratio in Illinois", loc="left")

# x function
xpoints = np.array(
    [
        "Under 5 years",
        "5 to 9 years",
        "10 to 14 years",
        "15 to 19 years",
        "20 to 24 years",
        "25 to 34 years",
        "35 to 44 years",
        "45 to 54 years",
        "55 to 59 years",
        "60 to 64 years",
        "65 to 74 years",
        "75 to 84 years",
        "85 years and over",
    ]
)
plt.xlabel("Age group")

# y function
ypoints = np.array(
    [
        876549,
        929858,
        905097,
        894002,
        850843,
        1811674,
        1983870,
        1626742,
        577747,
        462886,
        772247,
        535747,
        192031,
    ]
)  # Added closing parenthesis
plt.ylabel = plt.ylabel("Population Compared to Age Group")

# plot settings
plt.plot(ypoints, marker="o")
plt.plot(xpoints, ypoints)
plt.show()
