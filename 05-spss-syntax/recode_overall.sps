
* Recode 0–10 overall rating into bands: 0–6 (Low), 7–8 (Medium), 9–10 (High).
RECODE overall_0to10
 (LO THRU 6 = 1)
 (7 THRU 8 = 2)
 (9 THRU HI = 3) INTO overall_band.
VARIABLE LABELS overall_band 'Overall rating band (1=Low,2=Medium,3=High)'.
VALUE LABELS overall_band 1 'Low' 2 'Medium' 3 'High'.
EXECUTE.
