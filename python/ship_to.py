import requests
import csv
import json

def handle():
    with open('shipdata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            fetch(row['Client BO'], row['Bill to SiteUser Id'], row['Ship to SiteUse Id'])

def fetch(number, bill_id, ship_id, fcode = 'F615930'):
    url = 'https://nrisinterface.sgsonline.com.cn/CustomerApi/preOrderCustomer/contactAddress/query'
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'organizationName': fcode,'number': number, 'rows': 1000}
    res = requests.post(url, headers=headers, data=payload)
    result = json.loads(res.text)
    for row in result['rows']:
        # if p(row) and len(ship_id) > 0 and row['bossSiteUseID'] == int(ship_id):
        #     print(row)
        if b(row) and len(bill_id) > 0 and row['bossSiteUseID'] == int(bill_id):
            print(row)
    print(number, result['records'])

p = lambda row : row['code'] == 'SHIP_TO' and row['contactRole'] == 'SHIP_TO' and row['bossLocationCode'].startswith('P_')
b = lambda row : row['code'] == 'BILL_TO' and row['contactRole'] == 'BILL_TO' and row['bossLocationCode'].startswith('P_')

if __name__ == '__main__':
    handle()
    # fetch('3515120', 18649698, 18649698)

