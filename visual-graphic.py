import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
conflicts_df = pd.read_csv('conflicts_clean.csv')
diplomatic_df = pd.read_csv('diplomatic.csv')
conflicts_df['new_date'] = pd.to_datetime(conflicts_df['new_date'])
conf_groupby = conflicts_df.groupby(conflicts_df['new_date'].dt.to_period('M')).size().reset_index(name='counts')



diplomatic_df['new_date'] = pd.to_datetime(diplomatic_df['new_date'])
dipl_groupby = diplomatic_df.groupby(diplomatic_df['new_date'].dt.to_period('M')).size().reset_index(name='counts')

conf_groupby['new_date']=conf_groupby['new_date'].dt.to_timestamp()
dipl_groupby['new_date']=dipl_groupby['new_date'].dt.to_timestamp()


events = [
    {"date": "2020-11-13", "label": "1",  "y_mult": 0.97, "color": "red"},
    {"date": "2020-12-10", "label": "2",  "y_mult": 0.80, "color": "red"},
    {"date": "2021-08-24", "label": "3",  "y_mult": 0.97, "color": "red"},
    {"date": "2021-11-01", "label": "4",  "y_mult": 0.97, "color": "red"},
    {"date": "2022-03-14", "label": "5",  "y_mult": 0.97, "color": "red"},
    {"date": "2022-04-10", "label": "6",  "y_mult": 0.80, "color": "red"},
    {"date": "2023-10-30", "label": "7",  "y_mult": 0.97, "color": "red"},
    {"date": "2024-07-30", "label": "8",  "y_mult": 0.97, "color": "red"},
    {"date": "2024-10-04", "label": "9",  "y_mult": 0.97, "color": "red"},
    {"date": "2025-01-18", "label": "10", "y_mult": 0.97, "color": "red"},
    {"date": "2026-02-09", "label": "11", "y_mult": 0.80, "color": "red"},
    {"date": "2026-05-05", "label": "12", "y_mult": 0.80, "color": "red"},
    {"date": "2026-06-07", "label": "13", "y_mult": 0.97, "color": "red"},
    {"date": "2026-07-28", "label": "14", "y_mult": 0.90, "color": "orange"}
]

fig, axes = plt.subplots(nrows=2, figsize=(20, 14))
sns.lineplot(data=conf_groupby, x='new_date', y='counts', ax=axes[0])
top = axes[0].get_ylim()[1]
for m in events:
    axes[0].axvline(pd.Timestamp(m["date"]), color=m["color"])
    axes[0].text(pd.Timestamp(m["date"]), top * m["y_mult"], m["label"], fontsize=17)
axes[0].tick_params(axis='x', labelrotation=90)
axes[0].set_xlabel('Month-Year')
axes[0].set_ylabel('Count')
axes[0].set_title('Count of conflicts news by month')
sns.lineplot(data=dipl_groupby, x='new_date', y='counts', ax=axes[1])
top = axes[1].get_ylim()[1]
for m in events:
    axes[1].axvline(pd.Timestamp(m["date"]), color=m["color"])
    axes[1].text(pd.Timestamp(m["date"]), top * m["y_mult"], m["label"], fontsize=17)
axes[1].tick_params(axis='x', labelrotation=90)
axes[1].set_xlabel('Month-Year')
axes[1].set_ylabel('Count')
axes[1].set_title('Count of diplomatic news by month')
plt.savefig('conflicts_vs_diplomatic.png', dpi=150)