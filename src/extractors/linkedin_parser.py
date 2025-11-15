thonpy
import logging
from typing import List, Dict
from .utils_filters import filter_by_domain

# Mock dataset simulating LinkedIn scraping results
MOCK_LINKEDIN_DATA = [
    {
        "title": "Software Engineer",
        "profile": "https://linkedin.com/in/johndoe",
        "username": "johndoe",
        "email": "johndoe@gmail.com"
    },
    {
        "title": "Security Engineer",
        "profile": "https://linkedin.com/in/anubhavgain",
        "username": "anubhavgain",
        "email": "iamanubhavgain@gmail.com"
    },
    {
        "title": "Marketing Lead",
        "profile": "https://linkedin.com/in/janedoe",
        "username": "janedoe",
        "email": "jane.doe@outlook.com"
    }
]

class LinkedInParser:
    def __init__(self):
        logging.info("LinkedInParser initialized.")

    def search_and_extract(self, keyword: str, domains: List[str]) -> List[Dict]:
        logging.info(f"Searching for keyword '{keyword}' with domain filters {domains}")

        matches = []
        for entry in MOCK_LINKEDIN_DATA:
            if keyword.lower() in entry["title"].lower():
                matches.append(entry)

        logging.info(f"Found {len(matches)} profiles matching keyword '{keyword}'")

        filtered = filter_by_domain(matches, domains)
        logging.info(f"{len(filtered)} profiles remain after domain filtering.")

        final_output = []
        for item in filtered:
            final_output.append({
                "Email": item["email"],
                "Domain": item["email"].split("@")[-1],
                "Title": item["title"],
                "Detail_Link": item["profile"],
                "Username": item["username"],
                "Keyword": keyword,
                "DomainEmailUsed": domains
            })

        return final_output