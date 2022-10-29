from bs4 import BeautifulSoup
import requests
import re

RE_1 = ".*[P|p]ython.*"
RE_2 = ".*[J|j]unior.*"

for num_page in range(160,300):
    url = f"https://www.jobs.cz/prace/praha/?page={num_page}"

    response = requests.get(url)
    
    if response.status_code == 200:
        web = response.text
        soup = BeautifulSoup(web, "html.parser")
        jobs_offer = soup.find_all(class_="search-list__main-info__title__link")

        for one_job in jobs_offer:
            job_text = one_job.getText()
            job_link = one_job.get("href")

            if re.findall(RE_1, job_text):
                if re.findall(RE_2, job_text):
                    print(f"{job_text}\n{job_link}")
    else:
        quit()