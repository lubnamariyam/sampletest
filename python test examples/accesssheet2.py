import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']


creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/lubna/Downloads/lubnatest-16b0d291d690.json', scope)

 
client = gspread.authorize(creds)

sheet = client.open('lubna62')


sheet_instance = sheet.get_worksheet(2)

#sheet_instance.col_count

#records_data = sheet_instance.get_all_records()
#print(records_data)

student = {'NAME' : ['lubna', 'usuf', 'kiya', 'chittu'] ,
           'AGE'  : ['22', '21' , '33', '5'] }

df = pd.DataFrame(student)
print(df)
set_with_dataframe(sheet_instance,df)


