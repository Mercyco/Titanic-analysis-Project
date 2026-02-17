# src/analysis_class.py
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def class_analysis(df):
    survival_by_class = df.groupby("pclass")["survived"].mean()

    print("\nSurvival rate by passenger class:")
    print(survival_by_class)

    survival_by_class.plot(kind="bar", title="Survival Rate by Class")
    plt.ylabel("Survival Rate")
    plt.show()

    
    # Save results as CSV
    survival_by_class.to_csv("outputs/survival_by_class.csv")
    
    return survival_by_class
