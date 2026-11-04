import requests,csv,xml.etree.ElementTree as ET
URL='https://weworkremotely.com/remote-jobs.rss'
OUT='~/NEXRA-V16000/job_finder/jobs.csv'
OUT=__file__.replace('run.py','jobs.csv')
r=requests.get(URL,timeout=20)
