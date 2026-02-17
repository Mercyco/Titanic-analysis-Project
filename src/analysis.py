import pandas as pd
from analysis_gender import gender_analysis
from analysis_class import class_analysis
from analysis_age import age_analysis

def main():
    df = pd.read_csv("data/train.csv")

    print("Running Gender Analysis...")
    gender_analysis(df)

    print("Running Class Analysis...")
    class_analysis(df)

    print("Running Age Analysis...")
    age_analysis(df)

if __name__ == "__main__":
    main()
