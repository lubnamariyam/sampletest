import requests
import json
import os.path
import sys
import pandas as pd

import gspread

from oauth2client.service_account import ServiceAccountCredentials



scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/lubna/Downloads/lubnatest-16b0d291d690.json', scope)
client = gspread.authorize(credentials)
#sheet_instance = work_sheet.get_worksheet(0)
#sheet_instance = 1438190586
work_sheet = client.open('lubna62').sheet1



xlsheet = ['./pay0.xlsx', './pay1.xlsx','./pay2.xlsx','./pay3.xlsx','./pay4.xlsx','./pay5.xlsx','./pay6.xlsx','./pay7.xlsx','./pay8.xlsx','./pay9.xlsx']
appid_list = []
appname_list = []




i=1
for i in range(4,10):
    print(i)
    values = work_sheet.col_values(i)
    for val in values:
        #print(val)
        try:
            url =requests.get("https://dev-api.vajro.com/fetch_setup_config?appid=" +str(val))
            fetch_setup = url.json()
        
            if fetch_setup['status'] == "success":
                appid_list.append(val)

                if 'app_name' in fetch_setup:
                    if fetch_setup['app_name']:
                        appname_list.append(fetch_setup['app_name'])

                    else:
                        appname_list.append("-----")

                else:
                    appname_list.append("KEY MISSING")
            else:
                appid_list.append(val)
                appname_list.append("invalid")

        except ValueError as err:
            appid_list.append(val)
            appname_list.append(err.args)
            
            #to print name of exception occured
            #print(val, type(err))
            #to print message of exception
            print(val, (err.args))
            
            






    output = {'#01Appid' : appid_list,
              '#02Appname' : appname_list,
              
            }
    df = pd.DataFrame.from_dict(output , orient = 'index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    df.to_excel(xlsheet[i], sheet_name='paidapp', index=False)
    del appid_list [:]
    del appname_list [:]
    
else:
    print("________________________________________")
        
            
