import xlsxwriter


workbook = xlsxwriter.Workbook('v2_storedata_single_appid.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'ID')
worksheet.write('B1', 'HAS')
worksheet.write('C1', 'TYPE')
worksheet.write('D1', 'VALUE')
worksheet.write('E1', 'FINAL')




import requests 
import json
import os.path
import sys

app_id = input("Enter app id: ")
url = requests.get("https://api.vajro.com/v2/storedata?appid=" +str(app_id) )
store_data = url.json()



if store_data['status'] == "success":
    print("valid app_id")

    if 'addonconfig' in store_data:
        
        worksheet.write('B2', 'true')
        
        

        if store_data['addonconfig'] != '':
            print("addonconfig:" , type(store_data['addonconfig']) )
            a=str(type(store_data['addonconfig']))
            worksheet.write('A2', 'addonconfig')
            worksheet.write('C2', a )
            worksheet.write('E2', 'true')
            
        
        else:
            print("addonconfig:",type(store_data['addonconfig'])," empty ")
            a=str(type(store_data['addonconfig']))
            worksheet.write('A2, addonconfig')
            worksheet.write('C2', a )
            worksheet.write('D2', '-')
            worksheet.write('E2', 'false')
            
    else:
        print("addonconfig key missing")
        worksheet.write('A2', 'addonconfig')
        worksheet.write('B2', 'false')
        worksheet.write('E2', 'false')
        
        




    if 'addonflags' in store_data:
        worksheet.write('B3', "true")

        if store_data['addonflags'] != '':
            print("addonflags:" , type(store_data['addonflags']) )
            b=str(type(store_data['addonflags']))
            worksheet.write('A3', "addonflags")
            worksheet.write('C3', b )
            worksheet.write('E3', "true")
            
        else:
            print("addonflags:",type(store_data['addonflags'])," empty ")
            b=str(type(store_data['addonflags']))
            worksheet.write('A3', "addonflags")
            worksheet.write('C3', b )
            worksheet.write('D3', "-")
            worksheet.write('E3', "false")
            
            
    else:
        print("addonflags key missing")
        worksheet.write('A3', "addonflags")
        worksheet.write('B3', "false")
        worksheet.write('E3', "false")
        





    if 'analytics' in store_data:
         worksheet.write('B4', "true")
         
        
         if store_data['analytics'] != '':
               
             print("analytics:" , type(store_data['analytics']) )
             c=str(type(store_data['analytics']))
             worksheet.write('A4', "analytics")
             worksheet.write('C4', c )
             worksheet.write('E4', "true")
             
         else:
             print("analytics:",type(store_data['analytics'])," empty ")
             c=str(type(store_data['analytics']))
             worksheet.write('A4', "analytics")
             worksheet.write('C4', c )
             worksheet.write('D4', "-")
             worksheet.write('E4', "false")
             
             
    else:
        print("analytics key missing")
        worksheet.write('A4', "analytics")
        worksheet.write('B4', "false")
        worksheet.write('E4', "false")




    if 'apidata' in store_data:
         worksheet.write('B5', "true")
        

         if store_data['apidata'] != '':
             print("apidata:" , type(store_data['apidata']) )
             d=str(type(store_data['apidata']))
             worksheet.write('A5', "apidata")
             worksheet.write('C5', d )
             worksheet.write('E5', "true")
         else:
             print("apidata:",type(store_data['apidata'])," empty ")
             d=str(type(store_data['apidata']))
             worksheet.write('A5', "apidata")
             worksheet.write('C5', d )
             worksheet.write('D5', "-")
             worksheet.write('E5', "false")
             
    else:
        print("apidata key missing")
        worksheet.write('A5', "apidata")
        worksheet.write('B5', "false")
        worksheet.write('E5', "false")




    if 'app_version' in store_data:
         worksheet.write('B6', "true")
        

         if store_data['app_version'] != '':
             print("app_version:" , type(store_data['app_version']) )
             e=str(type(store_data['app_version']))
             worksheet.write('A6', "app_version")
             worksheet.write('C6', e )
             worksheet.write('E6', "true")
         else:
             print("app_version:",type(store_data['app_version'])," empty ")
             e=str(type(store_data['app_version']))
             worksheet.write('A6', "app_version")
             worksheet.write('C6', e )
             worksheet.write('D6', "-")
             worksheet.write('E6', "false")
    else:
        print("app_version key missing")
        worksheet.write('A6', "app_version")
        worksheet.write('B6', "false")
        worksheet.write('E6', "false")
        
        


    if 'appId' in store_data:
        worksheet.write('B7', "true")
        

        if store_data['appId'] != '':
            print("appId:" , type(store_data['appId']) , store_data['appId'] )
            f=str(type(store_data['appId']))
            fv=str(store_data['appId'])
            worksheet.write('A7', "appId")
            worksheet.write('C7', f )
            worksheet.write('D7', fv )
            worksheet.write('E7', "true")
        else:
            print("appId:",type(store_data['appId'])," empty ")
            f=str(type(store_data['appId']))
            worksheet.write('A7', "appId")
            worksheet.write('C7', f )
            worksheet.write('D7', "-" )
            worksheet.write('E7', "false")
    else:
        print("appId key missing")
        worksheet.write('A7', "appId")
        worksheet.write('B7', "false")
        worksheet.write('E7', "false")




    if 'bottom_bar' in store_data:
        worksheet.write('B8', "true")
        

        if store_data['bottom_bar'] != '':
            print("bottom_bar:" , type(store_data['bottom_bar']) )
            g=str(type(store_data['bottom_bar']))
            worksheet.write('A8', "bottom_bar")
            worksheet.write('C8', g )
            worksheet.write('E8', "true")
        else:
            print("bottom_bar:",type(store_data['bottom_bar'])," empty ")
            g=str(type(store_data['bottom_bar']))
            worksheet.write('A8', "bottom_bar")
            worksheet.write('C8', g )
            worksheet.write('D8', "-")
            worksheet.write('E8', "false")
            
    else:
        print("bottom_bar key missing")
        worksheet.write('A8', "bottom_bar")
        worksheet.write('B8', "false")
        worksheet.write('E8', "false")


        

    if 'categories' in store_data:
        worksheet.write('B9', "true")
       

        if store_data['categories'] != '':
            print("categories:" , type(store_data['categories']) )
            h=str(type(store_data['categories']))
            worksheet.write('A9', "categories")
            worksheet.write('C9', h )
            worksheet.write('E9', "true")
            
        else:
            print("categories:",type(store_data['categories'])," empty ")
            h=str(type(store_data['categories']))
            worksheet.write('A9', "categories")
            worksheet.write('C9', h )
            worksheet.write('D9', "-")
            worksheet.write('E9', "falsr")
    else:
        print("categories key missing")
        worksheet.write('A9', "categories")
        worksheet.write('B9', "false")
        worksheet.write('E9', "false")





    if 'colors' in store_data:
        worksheet.write('B10', "true")
        

        if store_data['colors'] != '':
            print("colors:" , type(store_data['colors']) )
            h=str(type(store_data['colors']))
            worksheet.write('A10', "colors")
            worksheet.write('C10', h )
            worksheet.write('E10', "true")
        else:
            print("colors:",type(store_data['colors'])," empty ")
            h=str(type(store_data['colors']))
            worksheet.write('A10', "colors")
            worksheet.write('C10', h )
            worksheet.write('D10', "-")
            worksheet.write('E10', "false")
    else:
        print("colors key missing")
        worksheet.write('A10', "colors")
        worksheet.write('B10', "false")
        worksheet.write('E10', "false")







    if 'currency_comma_enabled' in store_data:
        worksheet.write('B11', "true")
        

        if store_data['currency_comma_enabled']:
            print("currency_comma_enabled:" , type(store_data['currency_comma_enabled']) , store_data['currency_comma_enabled'] )
            i=str(type(store_data['currency_comma_enabled']))
            iv=str(store_data['currency_comma_enabled'])
            worksheet.write('A11', "currency_comma_enabled")
            worksheet.write('C11', i )
            worksheet.write('D11', iv )
            worksheet.write('E11', "true")
        else:
            print("currency_comma_enabled:" , type(store_data['currency_comma_enabled']) , store_data['currency_comma_enabled'])
            ie=str(type(store_data['currency_comma_enabled']))
            iev=str(store_data['currency_comma_enabled'])
            worksheet.write('A11', "currency_comma_enabled")
            worksheet.write('C11', ie )
            worksheet.write('D11', iev )
            worksheet.write('E11', "true")
            
    else:
        print("currency_comma_enabled key missing")
        worksheet.write('A11', "currency_comma_enabled")
        worksheet.write('B11', "false")
        worksheet.write('E11', "false")



    if 'currency_decimal_places' in store_data:
        worksheet.write('B12', "true")
        

        if store_data['currency_decimal_places']:
            print("currency_decimal_places:" , type(store_data['currency_decimal_places']) , store_data['currency_decimal_places'] )
            j=str(type(store_data['currency_decimal_places']))
            jv=str(store_data['currency_decimal_places'])
            worksheet.write('A12', "currency_decimal_places")
            worksheet.write('C12', j )
            worksheet.write('D12', jv )
            worksheet.write('E12', "true")
        else:
            print("currency_decimal_places:" , type(store_data['currency_decimal_places']) , store_data['currency_decimal_places'])
            je=str(type(store_data['currency_decimal_places']))
            jev=str(store_data['currency_decimal_places'])
            worksheet.write('A12', "currency_decimal_places")
            worksheet.write('C12', je )
            worksheet.write('D12', jev )
            worksheet.write('E12', "true")
    else:
        print("currency_decimal_places key missing")
        worksheet.write('A12', "currency_decimal_places")
        worksheet.write('B12', "false")
        worksheet.write('E12', "false")




    if 'currency_decimal_separator' in store_data:
        worksheet.write('B13', "true")
        

        if store_data['currency_decimal_separator']:
            print("currency_decimal_separator:" , type(store_data['currency_decimal_separator']) , store_data['currency_decimal_separator'] )
            k=str(type(store_data['currency_decimal_separator']))
            kv=str(store_data['currency_decimal_separator'])
            worksheet.write('A13', "currency_decimal_separator")
            worksheet.write('C13', k )
            worksheet.write('D13', kv )
            worksheet.write('E13', "true")
        else:
            print("currency_decimal_separator:" , type(store_data['currency_decimal_separator']) , store_data['currency_decimal_separator'])
            ke=str(type(store_data['currency_decimal_separator']))
            kev=str(store_data['currency_decimal_separator'])
            worksheet.write('A13', "currency_decimal_separator")
            worksheet.write('C13', ke )
            worksheet.write('D13', kev )
            worksheet.write('E13', "true")
    else:
        print("currency_decimal_separator key missing")
        worksheet.write('A13', "currency_decimal_separator")
        worksheet.write('B13', "false")
        worksheet.write('E13', "false")






    if 'currency_grouping_separator' in store_data:
        worksheet.write('A14', "true")
        

        if store_data['currency_grouping_separator']:
            print("currency_grouping_separator:" , type(store_data['currency_grouping_separator']) , store_data['currency_grouping_separator'] )
            l=str(type(store_data['currency_grouping_separator']))
            lv=str(store_data['currency_grouping_separator'])
            worksheet.write('A14', "currency_grouping_separator")
            worksheet.write('C14', l )
            worksheet.write('D14', lv )
            worksheet.write('E14', "true")
        else:
            print("currency_grouping_separator:" , type(store_data['currency_grouping_separator']) , store_data['currency_grouping_separator'] )
            le=str(type(store_data['currency_grouping_separator']))
            lev=str(store_data['currency_grouping_separator'])
            worksheet.write('A14', "currency_grouping_separator")
            worksheet.write('C14', le )
            worksheet.write('D14', lev )
            worksheet.write('E14', "true")
            
    else:
        print("currency_grouping_separator key missing")
        worksheet.write('A14', "currency_grouping_separator")
        worksheet.write('B14', "false")
        worksheet.write('E14', "false")




    if 'custom_font_bold' in store_data:
        worksheet.write('B15', "true")
        

        if store_data['custom_font_bold'] != '':
            print("custom_font_bold:" , type(store_data['custom_font_bold']) , store_data['custom_font_bold'] )
            m=str(type(store_data['custom_font_bold']))
            mv=str(store_data['custom_font_bold'])
            worksheet.write('A15', "custom_font_bold")
            worksheet.write('C15', m )
            worksheet.write('D15', mv )
            worksheet.write('E15', "true")
        else:
            print("custom_font_bold:",type(store_data['custom_font_bold'])," empty ")
            m=str(type(store_data['custom_font_bold']))
            worksheet.write('A15', "custom_font_bold")
            worksheet.write('C15', m )
            worksheet.write('D15', "-" )
            worksheet.write('E15', "false")
            
    else:
        print("custom_font_bold key missing")
        worksheet.write('A15', "custom_font_bold")
        worksheet.write('B15', "false")
        worksheet.write('E15', "false")





    if 'custom_font_regular' in store_data:
        worksheet.write('B16', "true")
        

        if store_data['custom_font_regular'] != '':
            print("custom_font_regular:" , type(store_data['custom_font_regular']) , store_data['custom_font_regular'] )
            n=str(type(store_data['custom_font_regular']))
            nv=str(store_data['custom_font_regular'])
            worksheet.write('A16', "custom_font_regular")
            worksheet.write('C16', n )
            worksheet.write('D16', nv )
            worksheet.write('E16', "true")
        else:
            print("custom_font_regular:",type(store_data['custom_font_regular'])," empty ")
            n=str(type(store_data['custom_font_regular']))
            nv=str(store_data['custom_font_regular'])
            worksheet.write('A16', "custom_font_regular")
            worksheet.write('C16', n )
            worksheet.write('D16', "-" )
            worksheet.write('E16', "false")
    else:
        print("custom_font_regular key missing")
        worksheet.write('A16', "custom_font_regular")
        worksheet.write('B16', "false")
        worksheet.write('E16', "false")






    if 'data' in store_data:
        worksheet.write('B17', "true")
        

        if store_data['data'] != '':
            print("data:" , type(store_data['data']) )
            o=str(type(store_data['data']))
            worksheet.write('A17', "data")
            worksheet.write('C17', o )
            worksheet.write('E17', "true")
        else:
            print("data:",type(store_data['data'])," empty ")
            o=str(type(store_data['data']))
            worksheet.write('A17', "data")
            worksheet.write('C17', o )
            worksheet.write('D17', "-")
            worksheet.write('E17', "false")
            
    else:
        print("data key missing")
        worksheet.write('A17', "data")
        worksheet.write('B17', "false")
        worksheet.write('E17', "false")




    if 'default_country' in store_data:
        worksheet.write('B18', "true")
        

        if store_data['default_country'] != '':
            print("default_country:" , type(store_data['default_country']) , store_data['default_country'] )
            p=str(type(store_data['default_country']))
            pv=str(store_data['default_country'])
            worksheet.write('A18', "default_country")
            worksheet.write('C18', p )
            worksheet.write('D18', pv )
            worksheet.write('E18', "true")
        else:
            print("default_country:",type(store_data['default_country'])," empty ")
            p=str(type(store_data['default_country']))
            worksheet.write('A18', "default_country")
            worksheet.write('C18', p )
            worksheet.write('D18', "-" )
            worksheet.write('E18', "false")
    else:
        print("default_country key missing")
        worksheet.write('A18', "default_country")
        worksheet.write('B18', "false")
        worksheet.write('E18', "false")





    if 'default_language' in store_data:
        worksheet.write('B19', "true")
        

        if store_data['default_language'] != '':
            print("default_language:" , type(store_data['default_language']) , store_data['default_language'] )
            q=str(type(store_data['default_language']))
            qv=str(store_data['default_language'])
            worksheet.write('A19', "default_language")
            worksheet.write('C19', q )
            worksheet.write('D19', qv )
            worksheet.write('E19', "true")
        else:
            print("default_language:",type(store_data['default_language'])," empty ")
            q=str(type(store_data['default_language']))
            worksheet.write('A19', "default_language")
            worksheet.write('C19', q )
            worksheet.write('D19', "-" )
            worksheet.write('E19', "false")
    else:
        print("default_language key missing")
        worksheet.write('A19', "default_country")
        worksheet.write('B19', "false")
        worksheet.write('E19', "false")





    if 'default-pages' in store_data:
        worksheet.write('B20', "true")
        

        if store_data['default-pages'] != '':
            print("default-pages:" , type(store_data['default-pages']) )
            r=str(type(store_data['default-pages']))
            worksheet.write('A20', "default-pages")
            worksheet.write('C20', r )
            worksheet.write('E20', "true")
        else:
            print("default-pages:",type(store_data['default-pages'])," empty ")
            r=str(type(store_data['default-pages']))
            worksheet.write('A20', "default-pages")
            worksheet.write('C20', r )
            worksheet.write('D20', "-" )
            worksheet.write('E20', "false")
            
    else:
        print("default-pages key missing")
        worksheet.write('A20', "default-pages")
        worksheet.write('B20', "false")
        worksheet.write('E20', "false")





    if 'force_default_country' in store_data:
        worksheet.write('B21', "true")
        

        if store_data['force_default_country'] != '':
            print("force_default_country:" , type(store_data['force_default_country']) , store_data['force_default_country'] )
            s=str(type(store_data['force_default_country']))
            sv=str(store_data['force_default_country'])
            worksheet.write('A21', "force_default_country")
            worksheet.write('C21', s )
            worksheet.write('D21', sv )
            worksheet.write('E21', "true")
        else:
            print("force_default_country:",type(store_data['force_default_country'])," empty ")
            s=str(type(store_data['force_default_country']))
            worksheet.write('A21', "force_default_country")
            worksheet.write('C21', s )
            worksheet.write('D21', "-" )
            worksheet.write('E21', "false")
    else:
        print("force_default_country key missing")
        worksheet.write('A21', "force_default_country")
        worksheet.write('B21', "false")
        worksheet.write('E21', "false")

            
    

    if 'images' in store_data:
        worksheet.write('B22', "true")
        

        if store_data['images'] != '':
            print("images:" , type(store_data['images']) )
            t=str(type(store_data['images']))
            worksheet.write('A22', "images")
            worksheet.write('C22', t )
            worksheet.write('E22', "true")
        else:
            print("images:",type(store_data['images'])," empty ")
            t=str(type(store_data['images']))
            worksheet.write('A22', "images")
            worksheet.write('C22', t )
            worksheet.write('D22', "-" )
            worksheet.write('E22', "false")
            
    else:
        print("default-pages key missing")
        worksheet.write('A22', "images")
        worksheet.write('B22', "false")
        worksheet.write('E22', "false")




    if 'isActive' in store_data:
        worksheet.write('B23', "true")
        

        if store_data['isActive']:
            print("isActive:" , type(store_data['isActive']) , store_data['isActive'] )
            u=str(type(store_data['isActive']))
            uv=str(store_data['isActive'])
            worksheet.write('A23', "isActive")
            worksheet.write('C23', u )
            worksheet.write('D23', uv )
            worksheet.write('E23', "true")
        else:
            print("isActive:" , type(store_data['isActive']) , store_data['isActive'])
            ue=str(type(store_data['isActive']))
            uev=str(store_data['isActive'])
            worksheet.write('A23', "isActive")
            worksheet.write('C23', ue )
            worksheet.write('D23', uev )
            worksheet.write('E23', "true")
    else:
        print("isActive key missing")
        worksheet.write('A23', "isActive")
        worksheet.write('B23', "false")
        worksheet.write('E23', "false")



    if 'iso_currency_code' in store_data:
        worksheet.write('B24', "true")
       

        if store_data['iso_currency_code'] != '':
            print("iso_currency_code:" , type(store_data['iso_currency_code']) , store_data['iso_currency_code'] )
            v=str(type(store_data['iso_currency_code']))
            vv=str(store_data['iso_currency_code'])
            worksheet.write('A24', "iso_currency_code")
            worksheet.write('C24', v )
            worksheet.write('D24', vv )
            worksheet.write('E24', "true")
        else:
            print("iso_currency_code:",type(store_data['iso_currency_code'])," empty ")
            v=str(type(store_data['iso_currency_code']))
            worksheet.write('A24', "iso_currency_code")
            worksheet.write('C24', v )
            worksheet.write('D24', "-" )
            worksheet.write('E24', "false")
    else:
        print("iso_currency_code key missing")
        worksheet.write('A24', "iso_currency_code")
        worksheet.write('B24', "false")
        worksheet.write('E24', "false")





    if 'isTrial' in store_data:
        worksheet.write('B25', "true")
        

        if store_data['isTrial']:
            print("isTrial:" , type(store_data['isTrial']) , store_data['isTrial'] )
            w=str(type(store_data['isTrial']))
            wv=str(store_data['isTrial'])
            worksheet.write('A25', "isTrial")
            worksheet.write('C25', w )
            worksheet.write('D25', wv )
            worksheet.write('E25', "true")
        else:
            print("isTrial:" , type(store_data['isTrial']) , store_data['isTrial'])
            we=str(type(store_data['isTrial']))
            wev=str(store_data['isTrial'])
            worksheet.write('A25', "isTrial")
            worksheet.write('C25', we )
            worksheet.write('D25', wev )
            worksheet.write('E25', "true")
    else:
        print("isTrial key missing")
        worksheet.write('A25', "isTrial")
        worksheet.write('B25', "false")
        worksheet.write('E25', "false")


    


    if 'logo' in store_data:
        worksheet.write('B26', "true")
        

        if store_data['logo'] != '':
            print("logo:" , type(store_data['logo']) , store_data['logo'] )
            x=str(type(store_data['logo']))
            xv=str(store_data['logo'])
            worksheet.write('A26', "logo")
            worksheet.write('C26', x )
            worksheet.write('D26', xv )
            worksheet.write('E26', "true")
        else:
            print("logo:",type(store_data['logo'])," empty ")
            x=str(type(store_data['logo']))
            worksheet.write('A26', "logo")
            worksheet.write('C26', x )
            worksheet.write('D26', "-" )
            worksheet.write('E26', "false")
    else:
        print("logo key missing")
        worksheet.write('A26', "logo")
        worksheet.write('B26', "false")
        worksheet.write('E26', "false")



    if 'maintenanceMode' in store_data:
        worksheet.write('B27', "true")
        

        if store_data['maintenanceMode']:
            print("maintenanceMode:" , type(store_data['maintenanceMode']) , store_data['maintenanceMode'] )
            y=str(type(store_data['maintenanceMode']))
            yv=str(store_data['maintenanceMode'])
            worksheet.write('A27', "maintenanceMode")
            worksheet.write('C27', y )
            worksheet.write('D27', yv )
            worksheet.write('E27', "true")
        else:
            print("maintenanceMode:" , type(store_data['maintenanceMode']) , store_data['maintenanceMode'])
            y=str(type(store_data['maintenanceMode']))
            yv=str(store_data['maintenanceMode'])
            worksheet.write('A27', "maintenanceMode")
            worksheet.write('C27', y )
            worksheet.write('D27', yv )
            worksheet.write('E27', "true")
    else:
        print("maintenanceMode key missing")
        worksheet.write('A27', "maintenanceMode")
        worksheet.write('B27', "false")
        worksheet.write('E27', "false")




    if 'message' in store_data:
        worksheet.write('B28', "true")
        

        if store_data['message'] != '':
            print("message:" , type(store_data['message']) , store_data['message'] )
            z=str(type(store_data['message']))
            zv=str(store_data['message'])
            worksheet.write('A28', "message")
            worksheet.write('C28', x )
            worksheet.write('D28', xv )
            worksheet.write('E28', "true")
        else:
            print("logo:",type(store_data['message'])," empty ")
            z=str(type(store_data['message']))
            worksheet.write('A28', "message")
            worksheet.write('C28', z )
            worksheet.write('D28', "-" )
            worksheet.write('E28', "false")
    else:
        print("message key missing")
        worksheet.write('A28', "message")
        worksheet.write('B28', "false")
        worksheet.write('E28', "false")


    if 'name' in store_data:
        worksheet.write('B29', "true")
        

        if store_data['name'] != '':
            print("name:" , type(store_data['name']) , store_data['name'] )
            aa=str(type(store_data['name']))
            aav=str(store_data['name'])
            worksheet.write('A29', "name")
            worksheet.write('C29', a )
            worksheet.write('D29', aav )
            worksheet.write('E29', "true")
        else:
            print("name:",type(store_data['name'])," empty ")
            aa=str(type(store_data['name']))
            worksheet.write('A29', "name")
            worksheet.write('C29', aa )
            worksheet.write('D29', "-" )
            worksheet.write('E29', "false")
    else:
        print("name key missing")
        worksheet.write('A29', "name")
        worksheet.write('B29', "false")
        worksheet.write('E29', "false")



    if 'nonboard' in store_data:
        worksheet.write('B30', "true")
        

        if store_data['nonboard'] != '':
            print("nonboard:" , type(store_data['nonboard']))
            bb=str(type(store_data['nonboard']))
            worksheet.write('A30', "nonboard")
            worksheet.write('C30', bb )
            worksheet.write('E30', "true")
            
        else:
            print("nonboard:",type(store_data['nonboard'])," empty ")
            bb=str(type(store_data['nonboard']))
            worksheet.write('A30', "nonboard")
            worksheet.write('C30', bb )
            worksheet.write('D30', "-" )
            worksheet.write('E30', "false")
            
    else:
        print("nonboard key missing")
        worksheet.write('A30', "nonboard")
        worksheet.write('B30', "false")
        worksheet.write('E30', "false")




    if 'page-list' in store_data:
        worksheet.write('B31', "true")
        

        if store_data['page-list'] != '':
            print("page-list:" , type(store_data['page-list']))
            cc=str(type(store_data['page-list']))
            worksheet.write('A31', "page-list")
            worksheet.write('C31', cc )
            worksheet.write('E31', "true")
        else:
            print("page-list:",type(store_data['page-list'])," empty ")
            cc=str(type(store_data['page-list']))
            worksheet.write('A31', "page-list")
            worksheet.write('C31', cc )
            worksheet.write('D31', "-" )
            worksheet.write('E31', "false")
            
    else:
        print("page-list key missing")
        worksheet.write('A31', "page-list")
        worksheet.write('B31', "false")
        worksheet.write('E31', "false")



    if 'pages' in store_data:
        worksheet.write('B32', "true")
        

        if store_data['pages'] != '':
            print("pages:" , type(store_data['pages']))
            dd=str(type(store_data['pages']))
            worksheet.write('A32', "pages")
            worksheet.write('C32', dd )
            worksheet.write('E32', "true")
        else:
            print("pages:",type(store_data['pages'])," empty ")
            dd=str(type(store_data['pages']))
            worksheet.write('A32', "pages")
            worksheet.write('C32', dd )
            worksheet.write('D32', "-" )
            worksheet.write('E32', "false")
    else:
        print("pages key missing")
        worksheet.write('A32', "page-list")
        worksheet.write('B32', "false")
        worksheet.write('E32', "false")





    if 'platform' in store_data:
        worksheet.write('B33', "true")
        

        if store_data['platform'] != '':
            print("platform:" , type(store_data['platform']) , store_data['platform'] )
            ee=str(type(store_data['platform']))
            eev=str(store_data['platform'])
            worksheet.write('A33', "platform")
            worksheet.write('C33', ee )
            worksheet.write('D33', eev )
            worksheet.write('E33', "true")
        else:
            print("platform:",type(store_data['platform'])," empty ")
            ee=str(type(store_data['platform']))
            worksheet.write('A33', "platform")
            worksheet.write('C33', ee )
            worksheet.write('E33', "-" )
            worksheet.write('E33', "false")
            
    else:
        print("platform key missing")
        worksheet.write('A33', "platform")
        worksheet.write('B33', "false")
        worksheet.write('E33', "false")



    if 'priceFormat' in store_data:
        worksheet.write('B34', "true")
        

        if store_data['priceFormat'] != '':
            print("priceFormat:" , type(store_data['priceFormat']) , store_data['priceFormat'] )
            ff=str(type(store_data['priceFormat']))
            ffv=str(store_data['priceFormat'])
            worksheet.write('A34', "priceFormat")
            worksheet.write('C34', ff )
            worksheet.write('D34', ffv )
            worksheet.write('E34', "true")
        else:
            print("priceFormat:",type(store_data['priceFormat'])," empty ")
            ff=str(type(store_data['priceFormat']))
            worksheet.write('A34', "priceFormat")
            worksheet.write('C34', ff )
            worksheet.write('D34', "-" )
            worksheet.write('E34', "false")
    else:
        print("priceFormat key missing")
        worksheet.write('A34', "priceFormat")
        worksheet.write('B34', "false")
        worksheet.write('E34', "false")

        





    if 'priceSuffix' in store_data:
        worksheet.write('B35', "true")
        

        if store_data['priceSuffix']:
            print("priceSuffix:" , type(store_data['priceSuffix']) , store_data['priceSuffix'] )
            gg=str(type(store_data['priceSuffix']))
            ggv=str(store_data['priceSuffix'])
            worksheet.write('A35', "priceSuffix")
            worksheet.write('C35', gg )
            worksheet.write('D35', ggv )
            worksheet.write('E35', "true")
        else:
            print("priceSuffix:" , type(store_data['priceSuffix']) , store_data['priceSuffix'])
            gg=str(type(store_data['priceSuffix']))
            ggv=str(store_data['priceSuffix'])
            worksheet.write('A35', "priceSuffix")
            worksheet.write('C35', gg )
            worksheet.write('D35', ggv )
            worksheet.write('E35', "true")
    else:
        print("priceSuffix key missing")
        worksheet.write('A35', "priceSuffix")
        worksheet.write('B35', "false")
        worksheet.write('E35', "false")




    if 'shopify_auto_login' in store_data:
        worksheet.write('B36', "true")
        

        if store_data['shopify_auto_login'] != '':
            print("shopify_auto_login:" , type(store_data['shopify_auto_login']))
            hh=str(type(store_data['shopify_auto_login']))
            worksheet.write('A36', "shopify_auto_login")
            worksheet.write('C36', hh )
            worksheet.write('E36', "true")
        else:
            print("shopify_auto_login:",type(store_data['shopify_auto_login']) ,  "empty ")
            hh=str(type(store_data['shopify_auto_login']))
            worksheet.write('A36', "shopify_auto_login")
            worksheet.write('C36', hh )
            worksheet.write('D36', "-")
            worksheet.write('E36', "false")
    else:
        print("shopify_auto_login key missing")
        worksheet.write('A36', "shopify_auto_login")
        worksheet.write('B36', "false")
        worksheet.write('E36', "false")



    if 'status' in store_data:
        worksheet.write('B37', "true")
        

        if store_data['status'] != '':
            print("status:" , type(store_data['status']) , store_data['status'] )
            pp=str(type(store_data['status']))
            ppv=str(store_data['status'])
            worksheet.write('A37', "status")
            worksheet.write('C37', pp )
            worksheet.write('D37', ppv )
            worksheet.write('E37', "true")
        else:
            print("status:",type(store_data['status'])," empty ")
            pp=str(type(store_data['status']))
            worksheet.write('A37', "status")
            worksheet.write('C37', pp )
            worksheet.write('D37', "-" )
            worksheet.write('E37', "false")
            
    else:
        print("status key missing")
        worksheet.write('A37', "status")
        worksheet.write('B37', "false")
        worksheet.write('E37', "false")





    

    




    if 'storeUrl' in store_data:
        worksheet.write('B39', "true")
        

        if store_data['storeUrl'] != '':
            print("storeUrl:" , type(store_data['storeUrl']) , store_data['storeUrl'] )
            ii=str(type(store_data['storeUrl']))
            iiv=str(store_data['storeUrl'])
            worksheet.write('A39', "storeUrl")
            worksheet.write('C39', ii )
            worksheet.write('D39', iiv )
            worksheet.write('E39', "true")
        else:
            print("storeUrl:",type(store_data['storeUrl'])," empty ")
            ii=str(type(store_data['storeUrl']))
            worksheet.write('A39', "storeUrl")
            worksheet.write('C39', ii )
            worksheet.write('D39', "-")
            worksheet.write('E39', "false")
    else:
        print("storeUrl key missing")
        worksheet.write('A39', "storeUrl")
        worksheet.write('B39', "false")
        worksheet.write('E39', "false")





    if 'storedata' in store_data:
        worksheet.write('B38', "true")
        

        if store_data['storedata'] != '':
            print("storedata:" , type(store_data['storedata']))
            jj=str(type(store_data['storedata']))
            worksheet.write('A38', "storedata")
            worksheet.write('C38', jj )
            worksheet.write('E38', "true")
        else:
            print("storedata:",type(store_data['storedata']) ," empty ")
            jj=str(type(store_data['storedata']))
            worksheet.write('A38', "storedata")
            worksheet.write('C38', jj )
            worksheet.write('D38', "-")
            worksheet.write('E38', "false")
    else:
        print("storedata key missing")
        worksheet.write('A38', "storedata")
        worksheet.write('B38', "false")
        worksheet.write('E38', "false")




    if 'text_zipcode_enabled' in store_data:
        worksheet.write('B40', "true")
        

        if store_data['text_zipcode_enabled']:
            print("text_zipcode_enabled:" , type(store_data['text_zipcode_enabled']) , store_data['text_zipcode_enabled'] )
            kk=str(type(store_data['text_zipcode_enabled']))
            kkv=str(store_data['text_zipcode_enabled'])
            worksheet.write('A40', "text_zipcode_enabled")
            worksheet.write('C40', kk )
            worksheet.write('D40', kkv )
            worksheet.write('E40', "true")
        else:
            print("text_zipcode_enabled:" , type(store_data['text_zipcode_enabled']) , store_data['text_zipcode_enabled'] )
            kk=str(type(store_data['text_zipcode_enabled']))
            kkv=str(store_data['text_zipcode_enabled'])
            worksheet.write('A40', "text_zipcode_enabled")
            worksheet.write('C40', kk )
            worksheet.write('D40', kkv )
            worksheet.write('E40', "true")
    else:
        print("text_zipcode_enabled key missing")
        worksheet.write('A40', "text_zipcode_enabled")
        worksheet.write('B40', "false")
        worksheet.write('E40', "false")





    if 'uid' in store_data:
        worksheet.write('B41', "true")
        

        if store_data['uid'] != '':
            print("uid:" , type(store_data['uid']) , store_data['uid'] )
            ll=str(type(store_data['uid']))
            llv=str(store_data['uid'])
            worksheet.write('A41', "uid")
            worksheet.write('C41', ll )
            worksheet.write('D41', llv )
            worksheet.write('E41', "true")
        else:
            print("uid:",type(store_data['uid']) , " empty ")
            ll=str(type(store_data['uid']))
            worksheet.write('A41', "uid")
            worksheet.write('C41', ll )
            worksheet.write('D41',"-"  )
            worksheet.write('E41', "false")
    else:
        print("uid key missing")
        worksheet.write('A41', "uid")
        worksheet.write('B41', "false")
        worksheet.write('E41', "false")
        




    if 'version_android' in store_data:
        worksheet.write('B42', "true")
        

        if store_data['version_android'] != '':
            print("version_android:" , type(store_data['version_android']) , store_data['version_android'] )
            nn=str(type(store_data['version_android']))
            nnv=str(store_data['version_android'])
            worksheet.write('A42', "version_android")
            worksheet.write('C42', nn )
            worksheet.write('D42', nnv )
            worksheet.write('E42', "true")
        else:
            print("version_android:", type(store_data['version_android']) ,"empty ")
            nn=str(type(store_data['version_android']))
            worksheet.write('A42', "version_android")
            worksheet.write('C42', nn )
            worksheet.write('D42', "-" )
            worksheet.write('E42', "false")
    else:
        print("version_android key missing")
        worksheet.write('A42', "version_android")
        worksheet.write('B42', "false")
        worksheet.write('E42', "false")





    if 'version_ios' in store_data:
        worksheet.write('B43', "true")
        

        if store_data['version_ios'] != '':
            print("version_ios:" , type(store_data['version_ios']) , store_data['version_ios'] )
            oo=str(type(store_data['version_ios']))
            oov=str(store_data['version_ios'])
            worksheet.write('A43', "version_ios")
            worksheet.write('C43', oo )
            worksheet.write('D43', oov )
            worksheet.write('E43', "true")
        else:
            print("version_ios:", type(store_data['version_ios']) ,"empty ")
            oo=str(type(store_data['version_ios']))
            worksheet.write('A43', "version_ios")
            worksheet.write('C43', oo )
            worksheet.write('D43', "-" )
            worksheet.write('E43', "false")
    else:
        print("version_ios key missing")
        worksheet.write('A43', "version_ios")
        worksheet.write('B43', "false")
        worksheet.write('E43', "false")







    if 'vVersion' in store_data:
        worksheet.write('B44', "true")
        

        if store_data['vVersion'] != '':
            print("vVersion:" , type(store_data['vVersion']) , store_data['vVersion'] )
            mm=str(type(store_data['vVersion']))
            mmv=str(store_data['vVersion'])
            worksheet.write('A44', "vVersion")
            worksheet.write('C44', mm )
            worksheet.write('D44', mmv )
            worksheet.write('E44', "true")
        else:
            print("vVersion:", type(store_data['vVersion']) ,"empty ")
            mm=str(type(store_data['vVersion']))
            worksheet.write('A44', "vVersion")
            worksheet.write('C44', mm )
            worksheet.write('D44', "-" )
            worksheet.write('E44', "false")
    else:
        print("vVersion key missing")
        worksheet.write('A44', "vVersion")
        worksheet.write('B44', "false")
        worksheet.write('E44', "false")

    
else:
    print("invalid app_id")


workbook.close() 
