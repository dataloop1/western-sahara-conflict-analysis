import trafilatura
import csv
import pandas as pd
import time
from urllib.parse import urlparse

data_conf = pd.read_csv(r'E:\desktop\maroco\conflicts.csv')
data_dip = pd.read_csv(r'E:\desktop\maroco\diplomatic.csv')
data_conf['domain'] = data_conf['SOURCEURL'].apply(lambda x: urlparse(x).netloc)
domain_dict = data_conf['domain'].value_counts().to_dict()
time_start = time.time()
with open('test_start.csv', mode='w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['GLOBALEVENTID', 'extract', 'status'])
    writer.writeheader()
    for index, row in data_conf.iterrows():
        try:
            domain = row['domain']
            dom_times = domain_dict.get(domain, 0)
            site_fetch_url = trafilatura.fetch_url(row['SOURCEURL'])
            if site_fetch_url is not None:
                site_extract = trafilatura.extract(site_fetch_url)
                if site_extract is not None:
                    writer.writerow({"GLOBALEVENTID": row['GLOBALEVENTID'], "extract": site_extract, "status": "success"})
                elif site_extract is None:
                    writer.writerow({"GLOBALEVENTID": row['GLOBALEVENTID'], "extract": None, "status": "no_extract" })
            else:
                writer.writerow({"GLOBALEVENTID": row['GLOBALEVENTID'], "extract": None, "status": "no_fetch"})
        except Exception as e:
            writer.writerow({"GLOBALEVENTID": row['GLOBALEVENTID'], "extract": None, "status": "error"})
        if dom_times>10:
            time.sleep(3)
        else:
            time.sleep(1.5)
time_end= time.time()
print(f'start - {time_start}')
print(f'end - {time_end}')
print(f'end-start {time_end-time_start}')
test_check = pd.read_csv('test_start.csv')

