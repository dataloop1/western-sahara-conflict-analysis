import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy import text
load_dotenv()

df_diplomatic = pd.read_csv('../data/diplomatic.csv')
df_diplomatic['NEW_DATE'] = pd.to_datetime(df_diplomatic['SQLDATE'], format='%Y%m%d').dt.date
df_diplomatic = df_diplomatic.drop(columns=['SQLDATE'])
df_diplomatic.columns = df_diplomatic.columns.str.lower()

df_ucdp_all = pd.read_csv('../data/ucdp_articles_all.csv')
df_ucdp_all['date'] = pd.to_datetime(df_ucdp_all['date'], format='%Y-%m-%d')
df_ucdp_all['date_start'] = pd.to_datetime(df_ucdp_all['date_start'], format='%Y-%m-%d')
df_ucdp_all['days_diff'] = df_ucdp_all['date'] - df_ucdp_all['date_start']
df_ucdp_all['days_diff'] = df_ucdp_all['days_diff'].dt.days
df_ucdp_all = df_ucdp_all[['GLOBALEVENTID', 'id', 'days_diff']]
df_ucdp_all['id'] = df_ucdp_all['id'].astype(int)
df_ucdp_all.columns = df_ucdp_all.columns.str.lower()

df_cameo = pd.read_csv('../data/CAMEO.eventcodes.txt', sep='\t', dtype={'CAMEOEVENTCODE': str})
df_cameo.columns = df_cameo.columns.str.lower()
df_ucdp_events = pd.read_csv('../data/ucdp_unique.csv')
target_columns = [
    'id', 'side_a', 'side_b', 'dyad_name', 'conflict_name',
    'date_prec', 'event_clarity', 'date_start', 'date_end',
    'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown',
    'best', 'high', 'low', 'latitude', 'longitude'
]
df_ucdp_events = df_ucdp_events[target_columns]
ucdp_int = ['id', 'date_prec', 'event_clarity', 'deaths_a', 'deaths_b', 'deaths_civilians', 'deaths_unknown', 'best', 'high', 'low']
df_ucdp_events[ucdp_int] = df_ucdp_events[ucdp_int].astype(int)
df_ucdp_events['date_start'] = pd.to_datetime(df_ucdp_events['date_start'])
df_ucdp_events['date_end'] = pd.to_datetime(df_ucdp_events['date_end'])
df_ucdp_events.columns = df_ucdp_events.columns.str.lower()

df_conflicts = pd.read_csv('../data/conflicts_enriched.csv')
df_conflicts['NEW_DATE'] = pd.to_datetime(df_conflicts['SQLDATE'], format='%Y%m%d').dt.date
df_conflicts = df_conflicts.drop(columns=['SQLDATE', 'date'])
df_conflicts.columns = df_conflicts.columns.str.lower()

engine = create_engine(f'postgresql+psycopg2://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}')
data = {
    'conflicts': df_conflicts,
    'diplomatic': df_diplomatic,
    'ucdp_events': df_ucdp_events,
    'ucdp_matches': df_ucdp_all,
    'cameo_codes': df_cameo
}

for table_name, df in data.items():
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='replace',
        index=False)
df_ucdp_events.to_csv('../data/ucdp_clean.csv', index=False)
df_conflicts.to_csv('../data/conflicts_clean.csv', index=False)
df_diplomatic.to_csv('../data/diplomatic_clean.csv', index=False)