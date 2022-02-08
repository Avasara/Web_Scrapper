import time
from bs4 import BeautifulSoup
import requests

#Any skill entered here will be filtered out of the program.

unknown_skill = input('Enter skills you do not possess>')
unknown_skill = unknown_skill.split(',')

print(f'Filtering out {unknown_skill}')
print(' ')

def findJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li' ,  class_ = 'clearfix job-bx wht-shd-bx')

    #The index here is to help iterate through the jobs, basically its a counter for the job post found
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
            #Ok the line below basically takes unknown skills list and stores it in a string which helps avoid typeerror when running it.

            for badskill in unknown_skill:
                if badskill not in skills.lower():

            #So because we wanted to access the <a href> tag within the header statement we just stated it.
            #It was inside the header which had a h2 which had 'a' which had the attribute 'href' which we wanted
            #Next we used the [] brackets to call the href attribute. THis prints only the value of href which is what we want

                    with open(f'listings/{index}.txt', 'w') as f:
                        f.write(f'Company name: {company_name.strip()}\n')
                        f.write(f'KeySkills: {skills.strip()}\n')
                        f.write(f'More Info/Apply here:  {job_apply}\n')
                    print(f"File saved: {index}")
                    


if __name__ == '__main__':
    while True:
        findJobs()
        timeWait = 10
        print(f'Waiting {timeWait} minutes...')
        time.sleep(1200)