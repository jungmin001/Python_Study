# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/25_mimii_features_94_260914_2.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# mu = df["rms"].mean()
# sd = df["rms"].std()
#
# z = (df["rms"] - mu) / sd
# print(z.head())

#
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_new_96_260915_2.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# mu = df["rms"].mean()
# sd = df["rms"].std()
#
# z = (df["rms"] - mu) / sd
# is_abnormal = z.abs() > 3
#
# abnormal_count = is_abnormal.sum()
# normal_count = (~is_abnormal).sum()
#
# print(f"행, 열 : {df.shape}")
# print(f"정상 개수: {normal_count}")
# print(f"이상 개수: {abnormal_count}")


#
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# # Feature to plot
# feature = "rms"
#
# normal = df.loc[df["label"] == 0, feature]
# abnormal = df.loc[df["label"] == 1, feature]
#
# plt.figure(figsize=(8, 5))
# plt.hist(normal, bins=30, alpha=0.5, label="정상", color="tab:blue")
# plt.hist(abnormal, bins=30, alpha=0.5, label="이상", color="tab:red")
#
# plt.title("rms 분포")
# plt.xlabel(feature)
# plt.ylabel("빈도")
# plt.legend()
# plt.tight_layout()
# plt.show()


# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# normal = df.loc[df["label"] == 0]
#
# normal_count = len(normal)
#
# features = ["rms", "spectral_centroid", "zero_crossing_rate"]
# mu = normal[features].mean()
# sd = normal[features].std()
#
# print(f"정상 개수: {normal_count} | 평균: {mu["rms"].round(3)} | 표준편차: {sd["rms"].round(3)}")
#


#
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# normal = df.loc[df['label'] == 0]
# mu = normal['rms'].mean()
# sd = normal['rms'].std()
#
# df['z_rms'] = (df['rms'] - mu) / sd
# df['z_abs'] = df['z_rms'].abs()
# df['is_anomaly'] = df['z_abs'] > 3
# print('임계값 3:', int(df['is_anomaly'].sum()))
# print('임계값 2:', int((df['z_abs'] > 2).sum()))



#
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# normal = df.loc[df['label'] == 0]
#
# is_any = pd.Series(False, index=df.index)
# for f in ['rms', 'spectral_centroid', 'zero_crossing_rate']:
#     z = (df[f] - normal[f].mean()) / normal[f].std()
#     is_any = is_any | (np.abs(z) > 3)
# print('종합 이상:', int(is_any.sum()))



# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# normal = df.loc[df['label'] == 0]
# mu = normal['rms'].mean()
# sd = normal['rms'].std()
#
# df['z_rms'] = (df['rms'] - mu) / sd
# df['z_abs'] = df['z_rms'].abs()
# df['is_anomaly'] = df['z_abs'] > 3
#
# hits = df[df['is_anomaly']].sort_values('z_abs', ascending=False).head(3)
# for i, row in hits.iterrows():
#     direction = '위' if row['z_rms'] > 0 else '아래'
#
# print(f"{i}번: 소리 세기가 표준편차 {row['z_abs']:.1f}배 {direction}로 벗어남, 점검 권장")


#
# import os
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import koreanfont as kf
# from sklearn.ensemble import IsolationForest
#
# # Language Settings
# kf.set_korean_font()
#
# # DataFile Locations
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# # DataFile Load
# df = pd.read_csv(Data_File)
#
# normal = df.loc[df['label'] == 0]
# mu = normal['rms'].mean()
# sd = normal['rms'].std()
#
# df['z_rms'] = (df['rms'] - mu) / sd
# df['z_abs'] = df['z_rms'].abs()
#
# missed = df[(df['z_abs'] <= 3) & (df['label'] == 1)]
# print('놓친 이상:', len(missed)) # 17
# sns.scatterplot(data=df, x='rms', y='zero_crossing_rate', hue='label')
# plt.title('rms vs zcr (missed anomalies)'); plt.show()

#
# import pandas as pd
# from sklearn.ensemble import IsolationForest
#
# Data_File = "Data/26_mimii_features_96_260915_3.csv"
#
# df = pd.read_csv(Data_File)
#
# x = df[["rms", "spectral_centroid", "zero_crossing_rate"]]
#
# iso = IsolationForest(contamination=0.18, random_state=42)
# iso.fit(x)
#
# pred = iso.predict(x)
# print(pred)


import pandas as pd
from sklearn.ensemble import IsolationForest

Data_File = "Data/26_mimii_features_96_260915_3.csv"

df = pd.read_csv(Data_File)

x = df[["rms", "spectral_centroid", "zero_crossing_rate"]]

model = IsolationForest(contamination=0.05, random_state=42)

model.fit(x)

df["이상판정"] = model.predict(x)
df["pred_anom"] = (df["이상판정"] == -1)

#print(pd.crosstab(df["label"], df["pred_anom"]))

df["score"] = model.score_samples(x)
df["decision"] = model.decision_function(x)