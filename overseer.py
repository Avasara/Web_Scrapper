import time
from bs4 import BeautifulSoup
import requests




unfamiliar_skill = input('Enter skills you do not possess>')
print(f'Filtering out {unfamiliar_skill}')
print(' ')

def findJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li' ,  class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):

        #Job status is outside because we want the entire code to revolve around when the employment ad was posted. 
        #It is the only variable where we want a very specific thing which is being posted a 'few' days ago
        #Theres no need to call a print statement for it as everything the program finds will be within the last few days

        job_status = job.find('span' , class_ = 'sim-posted').span.text

        #I love just how versatile the in statement is. Goddamn. Such a useful cookie :)

        if 'few' in job_status:
            company_name = job.find('h3' , class_ = 'joblist-comp-name').text.replace(' ', '')
            skills =  job.find('span' , class_ = 'srp-skills').text.replace(' ', '')
            job_apply = job.header.h2.a['href']

            #OH MY GOD NOT IS HERE AS WELL. GODAYAMMMMMMM. These 2 guys combined make it even better!! 

            if unfamiliar_skill not in skills.lower():

            #So because we wanted to access the <a href> tag within the header statement we just stated it.
            #It was inside the header which had a h2 which had 'a' which had the attribute 'href' which we wanted
            #Next we used the [] brackets to call the href attribute. THis prints only the value of href which is what we want

                with open(f'listings/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()}')
                    f.write(f'KeySkills: {skills.strip()}')
                    f.write(f'Apply here:  {job_apply}')
                print(f"File saved: {index}")

if __name__ == '__main__':
    while True:
        findJobs()
        timeWait = 10
        print(f'Waiting {timeWait} minutes...')
        time.sleep(1200)