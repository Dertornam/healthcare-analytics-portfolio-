
import pandas as pd
df = pd.read_csv("03-claims-cleaning/data/raw_claims.csv")
prov = df["provider_raw"].str.strip().str.lower().str.replace(r"\s+"," ", regex=True).replace({
    "acme health":"acme health","river valley med":"river valley medical","river v. medical":"river valley medical",
    "northcare":"north care","north care":"north care"})
df["provider_clean"]=prov
cpt_map={"99213":"E/M","99214":"E/M","99215":"E/M","93000":"EKG","80053":"CMP","36415":"Lab"}
df["cpt_category"]=df["cpt_code"].map(cpt_map).fillna("Other")
summary=df.groupby(["provider_clean","cpt_category"]).agg(claims=("claim_id","count"),mean_charge=("charge","mean")).reset_index()
df.to_csv("03-claims-cleaning/outputs/claims_clean.csv", index=False)
summary.to_csv("03-claims-cleaning/outputs/summary_by_provider_category.csv", index=False)
print("Wrote outputs to 03-claims-cleaning/outputs/")
