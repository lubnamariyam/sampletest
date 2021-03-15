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

xlsheet = ['./font0.xlsx', './font1.xlsx','./font2.xlsx','./font3.xlsx','./font4.xlsx','./font5.xlsx','./font6.xlsx','./font7.xlsx','./font8.xlsx']

appid_list = []
bottom_list = []

i=1
for i in range(1,9):
    print(i)
    values = work_sheet.col_values(i)



    for val in values:
        #print(val)
    
        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(val))
        store_data = url.json()

        if store_data['status'] == "success":
            appid_list.append(val)
            #print("valid app_id")

            if 'bottom_bar' in store_data:
                bottom_list.append("True")
            else:
                bottom_list.append("False")
        else:
            appid_list.append(val)
            bottom_list.append("invalid")


            
            
    output = {'appid' : appid_list,
              'botoom_bar' : bottom_list
            }
    df = pd.DataFrame.from_dict(output , orient = 'index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    df.to_excel(xlsheet[i], sheet_name='bottombar', index=False)
    del appid_list [:]
    del bottom_list[:]
    
else:
    print("________________________________________")    
    

    
