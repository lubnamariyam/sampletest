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
fblogingoogle = []
sociallogin = []





#xlsheet = ['./batch1.xlsx', './batch2.xlsx','./batch3.xlsx','./batch4.xlsx','./batch5.xlsx','./batch6.xlsx','./batch7.xlsx','./batch8.xlsx']

i=1
for i in range(1,11):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:

        #for val in values:
    
    
            
            
    
        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))
        store_data = url.json()
        #appid_list.append(val)

        if store_data['status'] == "success":
            appid.append(j)
        
    




            if 'addonflags' in store_data:

                v = store_data['addonflags']
                if 'fbLoginEnabled' in store_data['addonflags'] and 'googleLoginEnabled' in store_data['addonflags']:
                    fblogingoogle.append("true")
        
                    if 'addonconfig' in store_data:
                        c=store_data['addonconfig']
                        if 'social_login' in store_data['addonconfig']:
                            if 'android_google_client_id' in c['social_login']!= '' and 'google_client_id' in c['social_login']!= '' and 'google_uri_scheme' in c['social_login']!= '':
                                sociallogin.append("social login enabled")
                            else:
                                sociallogin.append("empty")
                        else:
                            sociallogin.append("social login key missing")
                    else:
                        sociallogin.append("addonconfig key missing")
                else:
                    fblogingoogle.append("false")
                    sociallogin.append("social login not enabled")
                    
            else:
                fblogingoogle.append("addonflag key missing")
                sociallogin.append("addonflag key missing")


        else:
            appid.append(j)
            fblogingoogle.append("invalid")
            sociallogin.append("invalid")





    output = {'#001appid' :appid ,
                  '#002fblogingoogle' : fblogingoogle,
                  '#003sociallogin' : sociallogin,
          }
    df = pd.DataFrame.from_dict(output, orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    
    df.to_excel('./v2_storedata_fb&google_login.xlsx', sheet_name='storedata', index=False)





    del appid [:]
    del fblogingoogle[:]
    del sociallogin [:]

    

    
           
