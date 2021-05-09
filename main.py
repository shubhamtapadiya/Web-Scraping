from bs4 import BeautifulSoup
import requests
import time

# requesting website
html_text = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

# creating object for BeautifulSoup
soup = BeautifulSoup(html_text, 'lxml')

print ("Put two skill which you are not familiar with")
unfamiliar_skill1 = raw_input('>')
unfamiliar_skill2 = raw_input('>')
print ("Filtering out " + unfamiliar_skill1 + ' and ' + unfamiliar_skill2)

# function for finding jobs which are posted "few days back"
def find_jobs():
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        job_publish = job.find('span', class_='sim-posted').span.text
        if 'few' in job_publish:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            links = job.header.h2.a['href']
            if (unfamiliar_skill1 or unfamiliar_skill2) not in skills:
                print ("Company Name: " + company_name.strip())
                print ("Required Skills: " + skills.strip())
                print ("More Info: " + links)
                print ("")


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print ("Waiting " +str(time_wait)+ " seconds...")
        time.sleep(time_wait)




#Reference:
# https://www.youtube.com/watch?v=XVv6mJpFOb0
# https://www.timesjobs.com/