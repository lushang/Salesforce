# Use this file to create custom meta data, and then import into Salesforce using Ant migration tool

import csv

cm_template = """<?xml version="1.0" encoding="UTF-8"?>
<CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <label>{0}</label>
    <protected>false</protected>
    <values>
        <field>Fcode__c</field>
        <value xsi:type="xsd:string">{1}</value>
    </values>
    <values>
        <field>Location__c</field>
        <value xsi:type="xsd:string">{2}</value>
    </values>
</CustomMetadata>
"""

with open('custom.metadata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cm = cm_template.format(row[0].strip(), row[2].strip(), row[1].strip())
        cm_file = open('Branch_Location.'+ row[0] + '.md', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
