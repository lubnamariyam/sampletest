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


appid=[]
live_android_list=[]
live_ios_list=[]
sneakpeek_android_list=[]
sneakpeek_ios_list=[]





xlsheet = ['./version0.xlsx', './version1.xlsx','./version2.xlsx','./version3.xlsx','./version4.xlsx','./version5.xlsx','./version6.xlsx','./version7.xlsx','./version8.xlsx','./version9.xlsx','./version10.xlsx','./version11.xlsx']

i=1
for i in range(7,11):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:

        #for val in values:
    
    
            
            
    
        try:
            
            url =requests.get("https://dev-api.vajro.com/appinfo?appid=" +str(j))
            appinfo = url.json()

            if appinfo['status'] == "success":
                appid.append(j)


                try: 
                    if 'apps' in appinfo and appinfo['apps'] !=[]:
                        #print(appinfo['apps'])
                        a =appinfo['apps']
                        for sub in a:
                            #if 'vajro_version' in a:
                            ver = sub['vajro_version']
                
                            if 'live_android' in sub['vajro_version']:
                                live_android_list.append(ver['live_android'])
                            else:
                                live_android_list.append("live_android key missing")


                            if 'live_ios' in ver:
                                live_ios_list.append(ver['live_ios'])
                            else:
                                live_ios_list.append("live_ios key missing")


                            if 'sneakpeek_android' in ver:
                                sneakpeek_android_list.append(ver['sneakpeek_android'])
                            else:
                                sneakpeek_android_list.append("sneakpeek_android key missing")


                            if 'sneakpeek_ios' in ver:
                                sneakpeek_ios_list.append(ver['sneakpeek_ios'])
                            else:
                                sneakpeek_ios_list.append("sneakpeek_ios key missing")
                    else:
                        live_android_list.append("key missing")
                        live_ios_list.append("key missing")
                        sneakpeek_android_list.append("key missing")
                        sneakpeek_ios_list.append("key missing")


                except:
                    live_android_list.append("vajroversion key missing error")
                    live_ios_list.append("vajroversion key missing")
                    sneakpeek_android_list.append("vajroversion key missing")
                    sneakpeek_ios_list.append("vajroversion key missing")
                
            

            

            else:
                appid.append(j)
                live_android_list.append("invalid")
                live_ios_list.append("invalid")
                sneakpeek_android_list.append("invalid")
                sneakpeek_ios_list.append("invalid")

    

        except ValueError as err:
            appid.append(j)
            live_android_list.append(err.args)
            live_ios_list.append(err.args)
            sneakpeek_android_list.append(err.args)
            sneakpeek_ios_list.append(err.args)




    output = {'#001appid' : appid,
                  '#002live_android' : live_android_list,
                  '#003live_ios' : live_ios_list,
                  '#004sneakpeek_android' :sneakpeek_android_list,
                  '#005sneakpeek_ios' : sneakpeek_ios_list
                  }
    df = pd.DataFrame.from_dict(output,orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    
    df.to_excel(xlsheet[i], sheet_name='appinfo', index=False)


    del appid [:]
    del live_android_list [:]
    del live_ios_list [:]
    del sneakpeek_android_list [:]
    del sneakpeek_ios_list [:]


    print("----------------------------------------------------")
    
    
