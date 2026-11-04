from datetime import timedelta
def news_protected(now, news_time, impact="HIGH"):
    if impact != "HIGH":
        return False
    return news_time-timedelta(minutes=30)<=now<=news_time+timedelta(minutes=30)
