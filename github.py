"""

github.py

Contains github for github side of the program

"""

from flask import render_template
import requests
from datetime import datetime
from config import GITHUB_REPO


# def get_pr_date() -> list:
#     url = f'https://api.github.com/repos/{GITHUB_REPO}/pulls'

#     response = requests.get(url)
#     print(response.text)

#     if response.status_code == 200:
#         pulls_data = response.json()
#         return pulls_data

#     else:
#         print(f"Request failed with status code {response.status_code}")


#def load_github_sites(app): #for main.py
#    @app.route('/pr')
#    def pr():
#        date_format = "%Y-%m-%dT%H:%M:%SZ"
#        pulls_data = get_pr_date()
#        links = [{"title":pull["title"], "url": pull['html_url'], "date": datetime.strptime(pull['created_at'], date_format).strftime("%Y-%m-%d"), "user":pull["user"]["login"]} for pull in pulls_data]
#        return render_template('github.html', links = links, n = len(links))*/