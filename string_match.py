import psycopg2
from typing import Dict, Tuple
import Levenshtein

def jaccard_similarity(str1: str, str2: str) -> float:
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def combined_similarity(str1: str, str2: str) -> float:
    levenshtein_sim = 1 - (Levenshtein.distance(str1, str2) / max(len(str1), len(str2)))
    jaccard_sim = jaccard_similarity(str1, str2)
    return (levenshtein_sim + jaccard_sim) / 2

def best_matches_combined(names_dict: Dict[str, str]) -> Dict[str, Tuple[str, float]]:
    matches = {}
    
    for full_name, modified_name in names_dict.items():
        similarity = combined_similarity(full_name, modified_name)
        matches[full_name] = (modified_name, similarity)
    
    return matches

def fetch_names_from_website_statistics_data(db_config: Dict[str, str]) -> Dict[str, str]:
    query = 'SELECT Name FROM WebsiteStatisticsData'
    
    names = []
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(query)
        names = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error fetching data: {e}")
    return names

def fetch_names_from_user_logistics(db_config: Dict[str, str]) -> Dict[str, str]:
    query = "SELECT \"User Name\" FROM UserLogistics"
    names = []
    try:
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(query)
        names = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error fetching data: {e}")
    return names

if __name__ == "__main__":
    website_db_config = {
        'dbname': 'your_website_db_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }
    
    crm_db_config = {
        'dbname': 'your_crm_db_name',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'port': 'your_port'
    }

    website_names = fetch_names_from_website_statistics_data(website_db_config)
    crm_names = fetch_names_from_user_logistics(crm_db_config)

    # Convert the lists into a dictionary for matching
    names_dict = {website_name: crm_name for website_name, crm_name in zip(website_names, crm_names)}

    matches = best_matches_combined(names_dict)
    for full_name, (modified_name, similarity) in matches.items():
        print(f"'{full_name}' best matches with '{modified_name}' with similarity {similarity:.2f}")
