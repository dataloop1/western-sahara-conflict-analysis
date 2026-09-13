import re
import pandas as pd
from urllib.parse import urlparse
progress = pd.read_csv('test_start.csv')
data_conf = pd.read_csv('conflicts.csv')
data_conf['domain'] = data_conf['SOURCEURL'].apply(lambda x: urlparse(x).netloc)
result = progress.merge(data_conf, on='GLOBALEVENTID')
words_casualty = ['killed', 'died', 'dead', 'injured', 'wounded', 'casualties', 'fatalities', 'tué', 'tuée', 'tués',
                  'tuées', 'mort', 'morte', 'morts', 'mortes', 'décédé', 'décédée', 'décédés', 'décédées', 'blessé',
                  'blessée', 'blessés', 'blessées', 'victime', 'victimes', 'muerto', 'muertos', 'herido', 'heridos',
                  'víctima', 'víctimas', 'fallecido', 'fallecidos', 'إصابة', 'مصابين', 'وفاة', 'مقتل',
                  'ضحايا', 'جرحى', 'قتلى']
words_repression = ['torture', 'tortured', 'rape', 'raped', 'arbitrary detention', 'repression', 'abuse', 'torturé',
                    'torturée', 'torturés', 'torturées', 'viol', 'violé', 'violée', 'violés', 'violées',
                    'détention arbitraire', 'répression', 'tortura', 'torturado', 'torturados', 'violación',
                    'detención arbitraria', 'represión', 'تعذيب', 'اغتصاب', 'احتجاز تعسفي', 'قمع']
pattern_casualty = r"\b("+"|".join(words_casualty)+r")\b"
def check_casualty(data_frame):
    if pd.isna(data_frame):
        return False
    else:
        return re.search(pattern_casualty, data_frame, flags =re.IGNORECASE) is not None
result['has_casualty_mention'] = result['extract'].apply(check_casualty)
pattern_repression = r"\b("+"|".join(words_repression)+r")\b"
def check_repression(data_frame):
    if pd.isna(data_frame):
        return False
    else:
        return re.search(pattern_repression, data_frame, flags =re.IGNORECASE) is not None
result['has_repression_mention'] = result['extract'].apply(check_repression)
result['date'] = pd.to_datetime(result['SQLDATE'], format='%Y%m%d')
result.to_csv('conflicts_enriched.csv', index=False)
testing = pd.read_csv('GEDEvent_v26_1.csv')
testing_maroco = testing[testing['country']=='Morocco']
testing_maroco['date_start'] = pd.to_datetime(testing_maroco['date_start'])
result_sort = result.sort_values('date')
testing_maroco_sort = testing_maroco.sort_values('date_start')
conflicts_info = pd.merge_asof(result_sort, testing_maroco_sort, left_on='date', right_on='date_start', direction='nearest', tolerance=pd.Timedelta(days=2))
ucdp_conflicts = conflicts_info[conflicts_info['best'].notna()]
ucdp_conflicts_unique_matches = ucdp_conflicts.drop_duplicates(subset='id')
ucdp_conflicts.to_csv('ucdp_articles_all.csv', index=False)
ucdp_conflicts_unique_matches.to_csv('ucdp_unique.csv', index=False)