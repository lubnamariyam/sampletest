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

appid = []
android_enabled_list = []
ios_enabled_list = []





#xlsheet = ['./batch1.xlsx', './batch2.xlsx','./batch3.xlsx','./batch4.xlsx','./batch5.xlsx','./batch6.xlsx','./batch7.xlsx','./batch8.xlsx']

i=1
for i in range(1,2):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:

        #for val in values:
    
    
            
            
    
        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))
        store_data = url.json()
        #appid_list.append(val)

        if store_data['status'] == "success":
            appid.append(j)
        
    




            if 'bottom_bar' in store_data:
                v=store_data['bottom_bar']
                if 'android_enabled' in v:
                    if v['android_enabled']:
                        android_enabled_list.append(v['android_enabled'])
                    else:
                        android_enabled_list.append(v['android_enabled'])
                else:
                    android_enabled_list.append("android_enabled key missing")


                if 'ios_enabled' in v:
                    if v['ios_enabled']:
                        ios_enabled_list.append(v['ios_enabled'])
                    else:
                        ios_enabled_list.append(v['ios_enabled'])
                else:
                    ios_enabled_list.append("ios_enabled key missing")


            else:
                android_enabled_list.append("bottom_bar missing")
                ios_enabled_list.append("bottom_bar missing")



        else:
            android_enabled_list.append("invalid")
            ios_enabled_list.append("invalid")
            appid.append(j)    





            
            
    output = {'#01appid' : appid,
              '#02android_enabled' : android_enabled_list,
              '#03ios_enabled': ios_enabled_list
            }
    df = pd.DataFrame.from_dict(output , orient = 'index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    df.to_excel('./bottombar0.xlsx', sheet_name='bottombar', index=False)
    del appid_list [:]
    del ios_enabled_list[:]
    del android_enabled [:]
    
else:
    print("________________________________________")    
    








