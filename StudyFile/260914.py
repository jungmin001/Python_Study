# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf

# # Language Settings
# kf.set_korean_font()

# # DataFile Locations 
# Data_File = os.path.join("Data", "25_cmapss_sample_94_260914_1.csv")
# Data_File2 = os.path.join("Data", "25_mimii_features_94_260914_2.csv")

# # DataFile Load
# df = pd.read_csv(Data_File2)

# y = df["label"]
# x = df[["rms", "spectral_centroid", "zero_crossing_rate"]]

# print(x.shape)
# print(y.shape)


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import koreanfont as kf

# Language Settings
kf.set_korean_font()

# DataFile Locations
Data_File = "Data/25_mimii_features_94_260914_2.csv"

# DataFile Load
df = pd.read_csv(Data_File)

plt.figure(figsize=(10, 5))

normal = df[df['label'] == 0]
anomaly = df[df['label'] == 1]

plt.scatter(normal.index, normal['rms'], color='blue', alpha=0.7, label='정상 (0)')
plt.scatter(anomaly.index, anomaly['rms'], color='red', alpha=0.7, label='이상 (1)')
plt.xlabel('Index')
plt.ylabel('RMS')
plt.legend()
plt.show()
