# Use this file to create custom meta data, and then import into Salesforce using Ant migration tool

import csv

cm_template = """<?xml version="1.0" encoding="UTF-8"?>
<CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <label>{0}</label>
    <protected>false</protected>
    <values>
        <field>Inspection_Cost_Center_Code__c</field>
        <value xsi:type="xsd:string">{1}</value>
    </values>
    <values>
        <field>Onsite_Lab_Cost_Center_Code__c</field>
        <value xsi:type="xsd:string">{2}</value>
    </values>
    <values>
        <field>Central_Lab_Cost_Center_Code__c</field>
        <value xsi:type="xsd:string">{3}</value>
    </values>
    <values>
        <field>Sub_SBU__c</field>
        <value xsi:type="xsd:string">{4}</value>
    </values>
    <values>
        <field>Parent_SBU__c</field>
        <value xsi:type="xsd:string">{5}</value>
    </values>
</CustomMetadata>
"""

with open('data/sbubranch.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        # print(len(row))
        cm = cm_template.format(
                row['MasterLabel'].strip()
                , row["Inspection_Cost_Center_Code__c"].strip()
                , row["Onsite_Lab_Cost_Center_Code__c"].strip()
                , row["Central_Lab_Cost_Center_Code__c"].strip()
                , row["Sub_SBU__c"].strip()
                , row["Parent_SBU__c"].strip())
        name = row["DeveloperName"].strip()
        # name = name.replace(' ', '_')
        cm_file = open('data/SBU_Branch.'+ name + '.md', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
