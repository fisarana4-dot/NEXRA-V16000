import requests, feedparser, json, hashlib
from datetime import datetime, timezone
SOURCES = {
 "remotive": "https://remotive.com/api/remote-jobs?limit=100",
 "remoteok": "https://remoteok.com/api",
 "reddit": "https://www.reddit.com/r/RemoteJobs/.rss",
 "reddit_python": "https://www.reddit.com/r/forhire/.rss",
}
def collect_jobs():
 jobs = []
 for source, url in SOURCES.items():
  try:
      headers = {"User-Agent": "NEXRA-V16000/1.0"}
      response = requests.get(url, headers=headers, timeout=20)
    except Exception as e: jobs.append({"source":source,"error":str(e)})
