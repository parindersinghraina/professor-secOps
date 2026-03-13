import boto3
import requests

# BAD: Hardcoded credentials (a real federal nightmare)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "SuperSecret123!"

def get_user_data(user_id):
    # BAD: SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def fetch_data(url):
    # BAD: No SSL verification (ITSG-33 violation)
    return requests.get(url, verify=False)
