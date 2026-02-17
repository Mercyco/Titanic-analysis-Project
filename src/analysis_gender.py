# src/analysis_gender.py
import matplotlib.pyplot as plt

def gender_analysis(df):
    survival_by_gender = df.groupby("sex")["survived"].mean()
    
    print("\nSurvival rate by gender:")
    print(survival_by_gender)

    survival_by_gender.plot(kind="bar", title="Survival Rate by Gender")
    plt.ylabel("Survival Rate")
    plt.show()

