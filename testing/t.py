import pandas as pd
df = pd.DataFrame({"A": [1, 2, 3], "B": [1, 2, 3]}, index=['a', 'a', 'b'])
print(df.to_markdown())
df.to_markdown('a.md')