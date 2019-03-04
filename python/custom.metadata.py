# Use this file to create custom meta data, and then import into Salesforce using Ant migration tool

import csv

cm_template = """<?xml version="1.0" encoding="UTF-8"?>
<CustomMetadata xmlns="http://soap.sforce.com/2006/04/metadata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <label>{1}</label>
    <protected>false</protected>
    <values>
        <field>Chinese_Address__c</field>
        <value xsi:type="xsd:string">{5}</value>
    </values>
    <values>
        <field>Chinese_Name__c</field>
        <value xsi:type="xsd:string">{3}</value>
    </values>
    <values>
        <field>Control_No__c</field>
        <value xsi:type="xsd:string">{0}</value>
    </values>
    <values>
        <field>Email__c</field>
        <value xsi:type="xsd:string">{7}</value>
    </values>
    <values>
        <field>English_Address__c</field>
        <value xsi:type="xsd:string">{6}</value>
    </values>
    <values>
        <field>Mobile__c</field>
        <value xsi:type="xsd:string">{10}</value>
    </values>
    <values>
        <field>SLIM_CODE__c</field>
        <value xsi:type="xsd:string">{2}</value>
    </values>
    <values>
        <field>Status__c</field>
        <value xsi:type="xsd:string">{4}</value>
    </values>
    <values>
        <field>Supervisor_Email__c</field>
        <value xsi:type="xsd:string">{11}</value>
    </values>
    <values>
        <field>Supervisor__c</field>
        <value xsi:type="xsd:string">{9}</value>
    </values>
    <values>
        <field>ZipCode__c</field>
        <value xsi:type="xsd:double">{8}</value>
    </values>
</CustomMetadata>
"""

with open('custom.metadata.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # print(len(row))
        cm = cm_template.format(row[0].strip(), row[1].strip(), row[2].strip()
                , row[3].strip(), row[4].strip(), row[5].strip()
                , row[6].strip(), row[7].strip(), row[8].strip()
                , row[9].strip(), row[10].strip(), row[11].strip())
        name = row[1].strip()
        name = name.replace(' ', '_')
        cm_file = open('Lab.'+ name + '.md', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
