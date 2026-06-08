import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Student_Social_Media_And_Mental_Health_Impact.csv") 
df = df.drop(["Gender", "Country", "Purpose_Of_Use", "Academic_Level", "Physical_Activity_Hours", "Daily_Unlocks"], axis=1)

daily_usage = df["Avg_Daily_Usage_Hours"].to_numpy()
sleep_hours = df["Sleep_Hours_Per_Night"].to_numpy()

mean_usage = np.mean(daily_usage)
std_sleep = np.std(sleep_hours)

print("--- Data Summary ---")
print(f"Average Daily Social Media Usage: {mean_usage:.2f} hours")
print(f"Standard Deviation of Sleep Hours: {std_sleep:.2f} hours\n")


figure, axes = plt.subplots(2, 2, figsize=(13, 11))

# --- figure 1 ---
axes[0,0].scatter(df["Avg_Daily_Usage_Hours"], df["Mental_Health_Score"], alpha=0.6, color='purple', edgecolor='black')
axes[0,0].set_title("Social Media Usage vs Mental Health Score", fontsize=12, fontweight='bold', color="#fc0303")
axes[0,0].set_xlabel("Average Daily Usage (Hours)")
axes[0,0].set_ylabel("Mental Health Score")
axes[0,0].grid(True, linestyle='--', alpha=0.6)

# --- figure 2 ---
most_used_platform = df["Most_Used_Platform"].value_counts()
wedges, texts, autotexts = axes[0,1].pie(
    most_used_platform.values, 
    labels=None, 
    autopct='%1.1f%%', 
    startangle=140, 
    pctdistance=0.85
)
axes[0,1].legend(
    wedges, 
    most_used_platform.index, 
    title="Platforms", 
    loc="center left", 
    bbox_to_anchor=(1.05, 0.5),
    prop={'size': 9}
)
axes[0,1].set_title("Most Used Platforms Distribution", fontsize=12, fontweight='bold', color="#fc0303")

# --- figure 3 ---
most_used = df["Most_Used_Platform"].value_counts(ascending=True)
axes[1,0].barh(most_used.index, most_used.values, color="#03fcf4", edgecolor="black")
axes[1,0].set_title("Most Used Platforms (Total Users)", color="#fc0303", fontsize=12, fontweight='bold')
axes[1,0].set_xlabel("# of Users")
axes[1,0].set_ylabel("Platform")

# --- figure 4 ---
strees_level = df["Stress_Level"].value_counts()
axes[1,1].bar(strees_level.index, strees_level.values, color="#9dfc03dc", edgecolor="black")
axes[1,1].set_title("Stress Level", fontsize=12, fontweight='bold', color="#fc0303")
axes[1,1].tick_params(axis='x', rotation=45) 
axes[1,1].set_xlabel("Stress Level")
axes[1,1].set_ylabel("# of Users")


plt.subplots_adjust(right=0.85, hspace=0.4, wspace=0.4)

plt.show()