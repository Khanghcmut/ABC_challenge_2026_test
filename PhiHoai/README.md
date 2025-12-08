# README – Project: Hidden Error Detection in Wearable Accelerometer Dataset
### (Data Cleaning & Sensor Mislabeling Recovery)
#### Conclusion
After analysing the dataset, the following hidden error was discovered and corrected:

**All files of Subject 1 (1_sbj_*.csv) had leg and arm acceleration columns completely swapped.**

This caused physically impossible patterns:
During jogging, burpees, butt-kicks, skipping, sidesteps, lunges, etc., the recorded “leg” acceleration was significantly lower than “arm” acceleration (mean difference leg − arm < 0).

The error was detected automatically by computing resultant acceleration magnitude and comparing leg vs. arm means per activity, revealing consistent negative differences in high-intensity lower-body movements for Subject 1 only.

**Correction applied:**

Swapped the six acceleration columns back in all Subject 1 files.**
Result: After correction, leg magnitude > arm magnitude in all running/jumping activities (diff +0.15 to +0.85), fully consistent with biomechanics.

**Subject 2 files were already correct.**

Final dataset (FINAL_CLEANED_DATASET.csv, 568,876 samples) now has correct sensor mapping and unified column order:
leg_acc_x, leg_acc_y, leg_acc_z, arm_acc_x, arm_acc_y, arm_acc_z, label