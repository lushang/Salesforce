# Use this file to create custom meta data, and then import into Salesforce using Ant migration tool

import csv

cm_template = """<?xml version="1.0" encoding="UTF-8"?>
<CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <label>{0}</label>
    <protected>false</protected>
    <values>
        <field>BOSS_Execution_Affiliate__c</field>
        <value xsi:type="xsd:string">{1}</value>
    </values>
    <values>
        <field>BOSS_Execution_Contact_ID__c</field>
        <value xsi:type="xsd:string">{2}</value>
    </values>
    <values>
        <field>Cost_Code__c</field>
        <value xsi:type="xsd:string">{3}</value>
    </values>
    <values>
        <field>Entity__c</field>
        <value xsi:type="xsd:string">{4}</value>
    </values>
    <values>
        <field>FCode__c</field>
        <value xsi:type="xsd:string">{5}</value>
    </values>
    <values>
        <field>Lob__c</field>
        <value xsi:type="xsd:string">{6}</value>
    </values>
    <values>
        <field>Location__c</field>
        <value xsi:type="xsd:string">{7}</value>
    </values>
    <values>
        <field>Project_Template__c</field>
        <value xsi:type="xsd:string">{8}</value>
    </values>
    <values>
        <field>Sales_Description__c</field>
        <value xsi:type="xsd:string">{9}</value>
    </values>
    <values>
        <field>Sales_Id__c</field>
        <value xsi:type="xsd:string">{10}</value>
    </values>
    <values>
        <field>SBU__c</field>
        <value xsi:type="xsd:string">{11}</value>
    </values>
    <values>
        <field>Site_Lab_Profit_Code__c</field>
        <value xsi:type="xsd:string">{12}</value>
    </values>
    <values>
        <field>BOSS_Execution_Contact_ID__c</field>
        <value xsi:type="xsd:string">{13}</value>
    </values>
</CustomMetadata>
"""

with open('cmd.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # print(len(row))
        cm = cm_template.format(row[0].strip(), row[1].strip(), row[2].strip()
                , row[3].strip(), row[4].strip(), row[5].strip()
                , row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip()
                , row[10].strip(), row[11].strip(), row[12].strip(), row[13].strip())
        name = row[0].strip()
        # name = name.replace(' ', '_')
        cm_file = open('FCode_X_SBU.'+ name + '.md', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
