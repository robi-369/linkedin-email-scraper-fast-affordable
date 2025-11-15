thonpy
from typing import List, Dict

def filter_by_domain(data: List[Dict], domains: List[str]) -> List[Dict]:
    if not domains:
        return data

    filtered = []
    for item in data:
        email = item.get("email", "").lower()
        if any(email.endswith(d.replace("@", "").lower()) for d in domains):
            filtered.append(item)
    return filtered