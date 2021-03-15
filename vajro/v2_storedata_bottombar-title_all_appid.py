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
title=[]






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
                #print(j)

                if 'bottom_bar' in store_data:
                    v=store_data['bottom_bar']
                    if 'tabs' in v:
                        print(j)
                        appid.append(j)
                        tit=[]
                
                        for val in v['tabs']:
                            if 'title' in val:
                                #print([val['title']])
                                tit.append(val['title'])
                        #del title [:]    
                        title.append(tit)
                                

                        
                                


                           
                    
                else:
                    print("no bottombar")


    

    output = {'#001appid' :appid,
                  '#002title' : title,        
          }
    
    df = pd.DataFrame.from_dict(output, orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    
    print(df)
    
    df.to_excel('./bottom-title.xlsx', sheet_name='storedata', index=False)
    
    

del appid [:]
del title[:]

    

