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
        <field>BOSS_Invoice_Contact_Description__c</field>
        <value xsi:type="xsd:string">{13}</value>
    </values>
    <values>
        <field>BOSS_Order_Creator__c</field>
        <value xsi:type="xsd:string">{14}</value>
    </values>
    <values>
        <field>BOSS_Org_Name__c</field>
        <value xsi:type="xsd:string">{15}</value>
    </values>
     <values>
        <field>BOSS_IDN_Order_Creator__c</field>
        <value xsi:type="xsd:string">{16}</value>
    </values>
</CustomMetadata>
"""

with open('data/cmd.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        # print(len(row))
        cm = cm_template.format(row['Label'].strip(), row["BOSS Execution Affiliate"].strip()
                , row["BOSS Execution Contact ID"].strip()
                , row["Cost Code"].strip(), row["Entity"].strip(), row["FCode"].strip()
                , row["LOB"].strip(), row["Location"].strip(), row["Project Template"].strip()
                , row["Sales Person Description"].strip()
                , row["Sales Person ID"].strip(), row["SBU"].strip(), row["Site Lab Profit Code"].strip()
                , row["BOSS Invoice Contact Desc"].strip()
                , row["BOSS Order Creator"].strip(), row["BOSS Org Name"].strip()
                , row["BOSS IDN Order Creator"].strip())
        name = row["Label"].strip()
        # name = name.replace(' ', '_')
        cm_file = open('data/FCode_X_SBU.'+ name + '.md', 'w', encoding='utf-8')
        cm_file.write(cm)
        cm_file.close()
