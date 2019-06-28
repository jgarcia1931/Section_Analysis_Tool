import requests
from flask import jsonify

payload = {
    'section1':'[(0.50,    0), 1.00, 0.30]',
    'section2':'[(0.85, 0.3), 0.30, 2.40]',
    'section3':'[(0, 2.7), 2.00, 0.30]',
    'section4':'[(0, 0), 0, 0]',
    'section5':'[(0, 0), 0, 0]',
    'section6':'[(0, 0), 0, 0]',
    'section7':'[(0, 0), 0, 0]',
    'section8':'[(0, 0), 0, 0]'}
headers = {'User-Agent': 'Mozilla/5.0'}

session = requests.Session()
print(session.post(url='https://sectionanalysistest.herokuapp.com/', headers = headers,data=jsonify(payload)))

print("test")