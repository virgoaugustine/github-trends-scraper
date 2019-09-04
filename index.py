import requests
from bs4 import BeautifulSoup as bs
import csv

page = requests.get("https://github.com/trending")
soup = bs(page.text, 'html.parser')

repo_list = soup.find_all('article', attrs={'class':'Box-row'})

#Save the data to a csv file
filename = "github_trending_today.csv"
f = csv.writer(open(filename, 'w', newline=''))

#Header Row
f.writerow(['Developer', 'Repository Name', 'Description', 'Stars', 'Link'])

for repo in repo_list:
    full_repo_name = repo.find('h1').find('a').text.strip().split('/')
    developer_name = full_repo_name[0].strip()
    repo_name = full_repo_name[1].strip()
    repo_description = repo.find('p').text.strip()
    #I could not find a way to extract the URL from the HREF text So I came up with this hack. 
    #Will probably find a better solution later.
    repo_link = "https://github.com" + repo.find('h1').find('a').get('href')
    repo_stars = repo.find('div', class_='f6').find('a').text.strip()
    # print("{} | {} | {} | {} | {} stars".format(developer_name, repo_name, repo_description, repo_link, repo_stars))
    print("Writing rows")
    f.writerow([developer_name, repo_name, repo_description, repo_stars, repo_link])





