import pandas as pd
import matplotlib.pyplot as plt

# Load sample EAR data
df_ear = pd.read_csv('../data/sample_ear.csv')
plt.plot(df_ear['Time'], df_ear['EAR'])
plt.title("EAR Drop Over Time")
plt.xlabel("Time (s)")
plt.ylabel("EAR Value")
plt.grid(True)
plt.show()
