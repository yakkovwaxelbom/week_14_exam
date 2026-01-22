import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['x', 'y', 'z']
})


print(*df.columns)