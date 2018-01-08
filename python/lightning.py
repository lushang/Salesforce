import requests
import json
from bs4 import BeautifulSoup
import re

# lightning_meta = 'https://developer.salesforce.com/docs/get_document/atlas.en-us.lightning.meta'
# url = 'https://developer.salesforce.com/docs/get_document_content/lightning/ref_intro.htm/en-us/210.0'
# soup = BeautifulSoup(html_doc)
#
# print(soup.prettify())


def find_attributes(json):
    pass


def get_attribute(_url_key):
    """
    This method take Salesforce Developer Guide component url key like `ref_intro` and return a dict with attribute


    :param _url_key: Salesforce Developer Guide component url key like ref_intro
    :return: a dict with all the component attribute
    """
    # attributes = []
    attribute = {"simple": False, "type": "aura", "attribs": {}}
    url = 'https://developer.salesforce.com/docs/get_document_content/lightning/' + _url_key + '.htm/en-us/210.0'
    print(url)
    r = requests.get(url, timeout=10)
    cmp = json.loads(r.text, encoding=r.encoding)
    attr_page = BeautifulSoup(cmp['content'], 'lxml')
    tables = attr_page.find_all('table')
    for table in tables:
        trs = table.find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')
            # attribute = {'Attribute': tds[0].text, 'Type': tds[1].text, 'Description': tds[2].text}
            # attributes.append(attribute)
            if len(tds) >= 3:
                description = tds[2].text
                description = re.sub(r'\n(\s)+', ' ', description)
                des_list = description.split('.')
                if len(des_list) > 2 and len(description) > 200:
                    description = des_list[0]
                attribute['attribs'][tds[0].text.replace("\n", "")] = {"type": tds[1].text, "description": description}
            else:
                print(_url_key)
    return attribute


ref_prefix = 'aura_compref_'
aura ='auraStorage:init,force:recordData,force:recordPreview,forceChatter:fullFeed,forceChatter:publisher,forceCommunity:appLauncher,forceCommunity:navigationMenuBase,forceCommunity:notifications,forceCommunity:routeLink,forceCommunity:waveDashboard'
aura = aura.split(',')
d = {}
for item in aura:
    if item == 'force:recordPreview':
        url_key = 'data_service_force_record'
    else:
        url_key = ref_prefix + item.replace(':', '_')
    d[item] = get_attribute(url_key)
with open('force_attrs.json', 'w', encoding='utf-8') as aura_file:
    json.dump(d, aura_file, indent=4)
