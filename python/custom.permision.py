# Use this file to create custom permission, then import into Salesforce using Ant migration tool

import csv

cm_template = """<?xml version="1.0" encoding="UTF-8"?>
<CustomPermission xmlns="http://soap.sforce.com/2006/04/metadata">
    <description>{0}</description>
    <label>{1}</label>
</CustomPermission>
"""

with open('cp.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        cm = cm_template.format(row["Description"].strip(), row["MasterLabel"].strip())
        name = row["DeveloperName"].strip()
        # name = name.replace(' ', '_')
        cm_file = open(name + '.customPermission', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
