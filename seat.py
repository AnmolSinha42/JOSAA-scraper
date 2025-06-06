import requests
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()
res = session.get("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx")

soup = BeautifulSoup(res.text,'html.parser')
hidden = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}


fields=[
"ctl00$ContentPlaceHolder1$ddlInstType",
"ctl00$ContentPlaceHolder1$ddlInstitute",
"ctl00$ContentPlaceHolder1$ddlBranch",
"ctl00$ContentPlaceHolder1$btnSubmit"]

#get list of options
inst_type = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlInstType"}).find_all("option")][1:]
institutes = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlInstitute"}).find_all("option")][1:]
branches = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlBranch"}).find_all("option")][1:]
print(inst_type)
print(institutes)
print(branches)
"""
data = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}
data[fields[0]] = "IIT"
data["__EVENTTARGET"] = fields[0]
res = session.post("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx",data = data)
soup = BeautifulSoup(res.text,'html.parser')

data = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}
data[fields[1]] = "121"
data["__EVENTTARGET"] = fields[1]
res = session.post("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx",data = data)
soup = BeautifulSoup(res.text,'html.parser')

data = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}
data[fields[2]] = "4109"
data["__EVENTTARGET"] = fields[2]
res = session.post("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx",data = data)
soup = BeautifulSoup(res.text,'html.parser')

print(res.text)
"""
counter = 0
for type in inst_type:
    for institute in institutes:
        for branch in branches:
            parameters = [type,institute,branch,"Submit"]
            for i in range(4):
                data = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}
                data[fields[i]] = parameters[i]
                data["__EVENTTARGET"] = fields[i]
                res = session.post("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx",data = data)
                soup = BeautifulSoup(res.text,'html.parser')
            
            
            if counter<3:
                counter = counter+1
                with open(f"{counter}.html","w") as f:
                    f.write(res.text)
            else:
                break
            



