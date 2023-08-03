import os
from datetime import datetime, timedelta

def get_all_dates_in_year(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    delta = timedelta(days=1)
    current_date = start_date
    all_dates = []
    while current_date <= end_date:
        all_dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += delta
    return all_dates

year = 2021
all_dates = get_all_dates_in_year(year)

for i, d in enumerate(all_dates):
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system(f'git commit --date="{d}" -m "Commit {i+1}"')

os.system('git push -u origin main')



#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin 
#git rebase origin --reapply-cherry-picks
#python git.py

# "git rebase origin/branch " for remove contribution 