
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("02-readmissions-risk/data/readmissions.csv")
df["decile"] = pd.qcut(df["risk_score"], 10, labels=False)
df.groupby("decile")["readmitted_30d"].mean().plot(kind="bar", figsize=(10,4.5))
plt.title("30-day Readmission Rate by Risk Decile"); plt.ylabel("Readmission rate"); plt.xlabel("Risk decile (0=lowest)"); plt.tight_layout()
plt.savefig("02-readmissions-risk/outputs/fig_readmit_rate_by_decile.png", dpi=150); plt.close()
plt.scatter(df["los_days"], df["risk_score"], s=10); plt.title("Risk Score vs Length of Stay")
plt.xlabel("LOS (days)"); plt.ylabel("Risk score (0–1)"); plt.tight_layout()
plt.savefig("02-readmissions-risk/outputs/fig_risk_vs_los.png", dpi=150); plt.close()
