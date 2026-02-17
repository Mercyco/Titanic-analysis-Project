import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.pyplot as plt

def age_analysis(df):
    df["age"].hist(bins=20)
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()


