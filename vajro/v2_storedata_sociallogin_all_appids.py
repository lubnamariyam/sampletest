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
social_login_list =[]
android_google_client_id_list = []
google_client_id_list = []
google_uri_scheme_list = []






xlsheet = ['./v2_storedata_sheet0_sociallogin.xlsx', './v2_storedata_sheet1_sociallogin.xlsx','./v2_storedata_sheet2_sociallogin.xlsx','./v2_storedata_sheet3_sociallogin.xlsx','./v2_storedata_sheet4_sociallogin.xlsx','./v2_storedata_sheet5_sociallogin.xlsx','./v2_storedata_sheet6_sociallogin.xlsx','./v2_storedata_sheet7_sociallogin.xlsx','./v2_storedata_sheet8_sociallogin.xlsx','./v2_storedata_sheet9_sociallogin.xlsx','./v2_storedata_sheet10_sociallogin.xlsx']

i=1
for i in range(9,10):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:
       

        
        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))
        store_data = url.json()
        

        if store_data['status'] == "success":
        
            appid_list.append(j)
    

            
            if 'addonconfig' in store_data:

                v = store_data['addonconfig']
                if 'social_login' in store_data['addonconfig']:
                    social_login_list.append("true")
        
                    if v:
                        c = v['social_login']
                        if 'android_google_client_id' in v['social_login']:
                            android_google_client_id_list.append(c['android_google_client_id'])
                        else:
                            android_google_client_id_list.append("android_google_client_id key missing")


                        if 'google_client_id' in v['social_login']:
                            google_client_id_list.append(c['google_client_id'])
                        else:
                            google_client_id_list.append("google_client_id key missing")


                        if 'google_uri_scheme' in v['social_login']:
                            google_uri_scheme_list.append(c['google_uri_scheme'])
                        else:
                            google_uri_scheme_list.append("google_uri_scheme key missing")
                        

                else:
                    social_login_list.append("key missing")
                    android_google_client_id_list.append("social_login key missing")
                    google_client_id_list.append("social_login key missing")
                    google_uri_scheme_list.append("social_login key missing")
                    
            else:
                social_login_list.append("addonconfig key missing")
                android_google_client_id_list.append("addonconfig key missing")
                google_client_id_list.append("addonconfig key missing")
                google_uri_scheme_list.append("addonconfig key missing")

            
        else:
            social_login_list.append("invalid")
            android_google_client_id_list.append("invalid")
            google_client_id_list.append("invalid") 
            google_uri_scheme_list.append("invalid")























            


    output = {'#001appid' :appid ,
                  '#002social_login': social_login_list,
                  '#003android_google_client_id' : android_google_client_id_list,
                  '#004google_client_id' : google_client_id_list,
                  '#005google_uri_scheme' : google_uri_scheme_list
                  
          }
    df = pd.DataFrame.from_dict(output, orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    
    df.to_excel(xlsheet[i], sheet_name='storedata', index=False)





del appid [:]
del social_login_list [:]
del android_google_client_id_list [:]
del google_client_id_list [:]
del google_uri_scheme_list[:]

    

    
           

