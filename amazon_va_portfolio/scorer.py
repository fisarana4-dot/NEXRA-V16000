import csv
def score(row):
    points = 0
    if float(row["Rating"]) >= 4.3: points += 30
    if row["Competition"] == "Low": points += 25
    if int(row["Reviews"]) >= 500: points += 20
    return points
