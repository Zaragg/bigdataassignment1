import sys
import pandas as pd
import dpre
path = sys.argv[0]
df = pd.read_csv(path)

print(df.head())

dpre.preprocess(df)
