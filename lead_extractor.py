import re
print('NEXRA V16000 Lead Extractor Ready')
open('potential_buyers.txt','w').write('\n'.join(set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', open('leads_raw.csv').read()))))
import hashlib

open('verified_leads.txt','w').writelines([f'{e.strip()} {hashlib.sha256(e.strip().encode()).hexdigest()}\n' for e in open('potential_buyers.txt')])
