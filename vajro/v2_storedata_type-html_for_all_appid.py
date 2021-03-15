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
typehtml= []






xlsheet = ['./v2_storedata_sheet0_type-html.xlsx', './v2_storedata_sheet1_type-html.xlsx','./v2_storedata_sheet2_type-html.xlsx','./v2_storedata_sheet3_type-html.xlsx','./v2_storedata_sheet4_type-html.xlsx','./v2_storedata_sheet5_type-html.xlsx','./v2_storedata_sheet6_type-html.xlsx','./v2_storedata_sheet7_type-html.xlsx','./v2_storedata_sheet8_type-html.xlsx','./v2_storedata_sheet9_type-html.xlsx','./v2_storedata_sheet10_type-html.xlsx']

i=1
for i in range(10,11):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:

        #for val in values:
    
    
            
            
        try:
            
            url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))
            store_data = url.json()
            #appid_list.append(val)

            if store_data['status'] == "success":
                #print(j)

                if 'pages' in store_data:
                    v=store_data['pages']
                    if 'home' in store_data['pages']:
                        if 'addons' in v['home']:
                            b=v['home']['addons']
                            for val in v['home']['addons']:
                                if 'type' in val and val['type']=='html':
                                    appid.append(j)
                                    typehtml.append(val['type'])
                            
                            
                        else:
                            print("nooooo")



        except ValueError as err:
            appid.append(j)
            typehtml.append(err.args)
                    


























            


    output = {'#001appid' :appid ,
                  '#002type-html' : typehtml,
                  
          }
    df = pd.DataFrame.from_dict(output, orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    
    df.to_excel(xlsheet[i], sheet_name='storedata', index=False)




    del appid [:]
    del typehtml[:]

    

    
           

