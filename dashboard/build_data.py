"""Build the static dashboard dataset from the reproducible cleaned CSVs."""
import csv, json
from pathlib import Path
from datetime import date
root=Path(__file__).resolve().parent.parent
result={}
for name in ['Threads','TikTok']:
    with (root/'results'/f'{name.lower()}_clean.csv').open(newline='',encoding='utf-8') as stream:
        rows=list(csv.DictReader(stream))
    first=date.fromisoformat(rows[0]['date'])
    result[name]=[{'date':r['date'],'day':(date.fromisoformat(r['date'])-first).days+1,'dau':float(r['dau']),'session':float(r['avg_session_duration_min']),'churn':float(r['churn_rate']),'organic':float(r['organic_traffic_pct'])} for r in rows]
(root/'dashboard'/'data.json').write_text(json.dumps(result,separators=(',',':')),encoding='utf-8')
print({name:len(rows) for name,rows in result.items()})
