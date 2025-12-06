import pandas as pd
import glob
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Load all files
files = glob.glob("*.csv")
print(f"Tìm thấy {len(files)} files:")

for f in files:
    df_temp = pd.read_csv(f, nrows=1)
    shape = pd.read_csv(f).shape          # đọc toàn bộ để lấy shape thật
    print(f"{f:30} → columns: {len(df_temp.columns)} cột → shape: {shape}")