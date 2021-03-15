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

key_list = ['abandonedCartEnabled',
'autoApplyCouponEnabled',
'backToStockAlertEnaled',
'blogEnabled',
'branchSDKEnabled',
'brandPlaceholderEnabled',
'cleverTapEnabled',
'crossSellEnabled',
'customProductOptionsEnabled',
'customerChatEnabled',
'deliveryAreaEnabled',
'deliveryOptionsEnabled',
'deliverySlotEnabled',
'fbLoginEnabled',
'firebaseAnalyticsEnabled',
'flitsEnabled',
'googleLoginEnabled',
'guestCheckoutEnabled',
'isForceUpdate',
'shopifyMobileSalesChannelEnabled',
'multiLanguageEnabled',
'multiVendorCheckoutEnabled',
'nativeCheckoutEnabled',
'nativeCheckoutProcessEnabled',
'new_cart_design_enabled',
'postAffiliateProEnabled',
'productGridWishlistEnabled',
'productReviewsEnabled',
'rateUsEnabled',
'refreshCartEnabled',
'reorderEnabled',
'rewardEnabled',
'shareCollectionEnabled'
'sortFilterEnabled',
'suggestionsEnabled',
'deliveryRegionEnabled',
'liveVideoEnabled',
'orderNoteEnabled',
'showLineItemCount',
'webAppleGooglePayEnabled',
'applePayEnabled',
'smartSearchEnabled',
'deepLinkingEnabled',
'switch_search_suggestion_section',
'savedSearchNotifEnabled',
'appsflyerEnabled',
'boldSubscriptionEnabled',
'christmasModeEnabled',
'imageSearchEnabled',
'rewardifyEnabled',
'valentinesDayEnabled',
'swapMyShopifyDomain',
'agePopupEnabled',
'viaEnabled',
'quantityBreaksEnabled',
'browserDeeplinkEnabled',
'multiCurrencyEnabled',
'pullToRefreshEnabled',
'related_products_enabled',
'show_collection_description',
'shopifyEmiEnabled',
'mobileSalesChannelEnabled']


addonflag_1key = []
addonflag_value =[]
i=1
for i in range(1,4):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:
        print(j)

        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))
        store_data = url.json()

        if store_data['status'] == "success":

            if 'addonflags' in store_data:

                for i in key_list:
                    #addonflag_1key.append(i)
                    v = store_data['addonflags']
                    if i in store_data['addonflags']:
                        addonflag_1key.append(i)
                        if v:
                            addonflag_value.append(v[i])

                        else:
                            addonflag_value.append(v[i])
                    
                    else:
                        addonflag_1key.append(i),
                        addonflag_value.append("key missing")
                        

                
            


        





                    output = {'columns' : addonflag_1key , 'addonflag_value': addonflag_value}
                    df = pd.DataFrame.from_dict(output , orient = 'index')
                    
                    #df = df.transpose()
                    #df = df.sort_index(axis=1)
                    print(df)
                    df.to_excel('./vvv.xlsx', sheet_name='storedata', index=False)
        























"""if store_data['addonflags']:
            v = store_data['addonflags']
            x = store_data['addonflags'].keys()
            #print(x)
            #y = store_data['addonflags'].value()
            if 'abandonedCartEnabled' in x:
                y = v['abandonedCartEnabled']
                print(y)
            else:
                print("key missing")


            if 'abandonedCartEnabled' in x:
                y = v['abandonedCartEnabled']
                print(y)
            else:
                print("key missing")

    else:
        print("key missing")"""
