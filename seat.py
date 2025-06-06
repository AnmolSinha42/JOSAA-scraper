import requests
from bs4 import BeautifulSoup
import pandas as pd

session = requests.Session()
res = session.get("https://josaa.admissions.nic.in/applicant/seatmatrix/seatmatrixinfo.aspx")

soup = BeautifulSoup(res.text,'html.parser')
hidden = {item["name"]:item.get("value","") for item in soup.find_all("input",{"type":"hidden"})}
post_data = hidden.copy()

"""
"ctl00$ContentPlaceHolder1$ddlInstType"
"ctl00$ContentPlaceHolder1$ddlInstitute"
"ctl00$ContentPlaceHolder1$ddlBranch"

"""
inst_type = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlInstType"}).find_all("option")]
institutes = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlInstitute"}).find_all("option")]
branches = [item["value"] for item in soup.find("select",{"name":"ctl00$ContentPlaceHolder1$ddlBranch"}).find_all("option")]

