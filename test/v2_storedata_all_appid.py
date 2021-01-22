import requests        #to access http link 
import json            #convert to json string
import os.path
import sys
import pandas as pd    #to wrangle the data

import gspread         #to access google sheets

from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/lubna/Downloads/lubnatest-16b0d291d690.json', scope)      #path for default credentioals file from google developers
client = gspread.authorize(credentials)
#sheet_instance = work_sheet.get_worksheet(0)     #to access particular sheet 
#sheet_instance = 1438190586                      # sheet id
work_sheet = client.open('lubna62').sheet1           #sheet name
#append data to list
appId_list = []
appid_list = []
isactive_list= []
bottom_bar_list = []
isTrial_list = []
custom_font_bold_list = []
custom_font_regular_list = []
currency_comma_enabled_list = []
default_country_list = []
default_language_list = []
iso_currency_code_list = []
logo_list = []
name_list = []
platform_list = []
priceFormat_list = []
priceSuffix_list = []
storeUrl_list = []
text_zipcode_enabled_list = []
status_list = []



abandonedCartEnabled_list = []
autoApplyCouponEnabled_list = []
backToStockAlertEnaled_list = []
blogEnabled_list = []
branchSDKEnabled_list = []
brandPlaceholderEnabled_list=[]
cleverTapEnabled_list=[]
crossSellEnabled_list=[]
customProductOptionsEnabled_list=[]
customerChatEnabled_list=[]
deliveryAreaEnabled_list=[]
deliveryOptionsEnabled_list=[]
deliverySlotEnabled_list=[]
fbLoginEnabled_list=[]
firebaseAnalyticsEnabled_list=[]
flitsEnabled_list=[]
googleLoginEnabled_list=[]
guestCheckoutEnabled_list=[]
isForceUpdate_list=[]
shopifyMobileSalesChannelEnabled_list=[]
multiLanguageEnabled_list=[]
multiVendorCheckoutEnabled_list=[]
nativeCheckoutEnabled_list = []
nativeCheckoutProcessEnabled_list = []
new_cart_design_enabled_list = []
postAffiliateProEnabled_list =[]
productGridWishlistEnabled_list = []
productReviewsEnabled_list =[]
rateUsEnabled_list = []
refreshCartEnabled_list =[]
reorderEnabled_list =[]
rewardEnabled_list = []
shareCollectionEnabled_list = []
sortFilterEnabled_list = []
suggestionsEnabled_list = []
deliveryRegionEnabled_list =[]
liveVideoEnabled_list = []
orderNoteEnabled_list = []
showLineItemCount_list = []
webAppleGooglePayEnabled_list = []
applePayEnabled_list = []
smartSearchEnabled_list = []
deepLinkingEnabled_list = []
switch_search_suggestion_section_list = []
savedSearchNotifEnabled_list =[]
appsflyerEnabled_list = []
boldSubscriptionEnabled_list = []
christmasModeEnabled_list = []
imageSearchEnabled_list = []
rewardifyEnabled_list = []
valentinesDayEnabled_list = []
swapMyShopifyDomain_list = []
agePopupEnabled_list = []
viaEnabled_list = []
quantityBreaksEnabled_list = []
browserDeeplinkEnabled_list = []
multiCurrencyEnabled_list = []
pullToRefreshEnabled_list = []
related_products_enabled_list = []
show_collection_description_list = []
shopifyEmiEnabled_list = []
mobileSalesChannelEnabled_list = []
accent_color_list = []
badge_color_list = []
badge_text_color_list = []
buy_button_color_list = []
option_value_color_list = []
primary_color_list = []
primary_color_dark_list = []
share_button_color_list = []
splash_bg_color_list = []
splash_spinner_color_list = []
sub_collection_color_list = []
toolbar_color_list = []
toolbar_content_color_list = []
discount_color_list = []
vendor_color_list = []

social_login_list =[]
android_google_client_id_list = []
google_client_id_list = []
google_uri_scheme_list = []


#to create local xl sheet 
xlsheet = ['./2020_01_22_sheet0_v2_storedata_all_appid.xlsx', './2020_01_22_sheet1_v2_storedata_all_appid.xlsx','./2020_01_22_sheet2_v2_storedata_all_appid.xlsx','./2020_01_22_sheet3_v2_storedata_all_appid.xlsx','./2020_01_22_sheet4_v2_storedata_all_appid.xlsx','./2020_01_22_sheet5_v2_storedata_all_appid.xlsx','./2020_01_22_sheet6_v2_storedata_all_appid.xlsx','./2020_01_22_sheet7_v2_storedata_all_appid.xlsx','./2020_01_22_sheet8_v2_storedata_all_appid.xlsx','./2020_01_22_sheet9_v2_storedata_all_appid.xlsx','./2020_01_22_sheet10_v2_storedata_all_appid.xlsx']

i=1
for i in range(8,10):
    print(i)
    values = work_sheet.col_values(i)
    for j in values:

        #for val in values:
    
    
            
            
    
        url =requests.get("https://api.vajro.com/v2/storedata?appid=" +str(j))              #fetch url 
        store_data = url.json()
        

        if store_data['status'] == "success":
        
            appid_list.append(j)

            if 'isActive' in store_data:

                if store_data['isActive']:
                    
                    isactive_list.append(store_data['isActive'] )

                
                    
                else:
                    
                    isactive_list.append(store_data['isActive'])

            else:
                isactive_list.append("key missing")




            if 'bottom_bar' in store_data:
                bottom_bar_list.append("true")

            else:
                bottom_bar_list.append("false")


            if 'isTrial' in store_data:

                if store_data['isTrial']:
                    
                    isTrial_list.append(store_data['isTrial'] )

                
                    
                else:
                    
                    isTrial_list.append(store_data['isTrial'])

            else:
                isTrial_list.append("key missing")



            if 'currency_comma_enabled' in store_data:

                if store_data['currency_comma_enabled']:
                    
                    currency_comma_enabled_list.append(store_data['currency_comma_enabled'] )

                
                    
                else:
                    
                    currency_comma_enabled_list.append(store_data['currency_comma_enabled'])

            else:
                currency_comma_enabled_list.append("key missing")




            if 'custom_font_bold' in store_data:

                if store_data['custom_font_bold']:
                    custom_font_bold_list.append(store_data['custom_font_bold'])

                else:
                    custom_font_bold_list.append("-----")

            else:
                custom_font_bold_list.append("false")
            




            if 'custom_font_regular' in store_data:

                if store_data['custom_font_regular']:
                    custom_font_regular_list.append(store_data['custom_font_regular'])

                else:
                    custom_font_regular_list.append("-----")


            else:
                custom_font_regular_list.append("false")







            if 'default_country' in store_data:

                if store_data['default_country']:
                    default_country_list.append(store_data['default_country'])

                else:
                    default_country_list.append("-----")


            else:
                default_country_list.append("false")






            if 'default_language' in store_data:

                if store_data['default_language']:
                    default_language_list.append(store_data['default_language'])

                else:
                    default_language_list.append("-----")


            else:
                default_language_list.append("false")



            if 'iso_currency_code' in store_data:

                if store_data['iso_currency_code']:
                    iso_currency_code_list.append(store_data['iso_currency_code'])

                else:
                    iso_currency_code_list.append("-----")


            else:
                iso_currency_code_list.append("false")


            if 'logo' in store_data:

                if store_data['logo']:
                    logo_list.append(store_data['logo'])

                else:
                    logo_list.append("-----")


            else:
                logo_list.append("key missing")

            if 'name' in store_data:

                if store_data['name']:
                    name_list.append(store_data['name'])

                else:
                    name_list.append("-----")


            else:
                name_list.append("key missing")




            if 'platform' in store_data:

                if store_data['platform']:
                    platform_list.append(store_data['platform'])

                else:
                    platform_list.append("-----")


            else:
                platform_list.append("key missing")



            if 'priceFormat' in store_data:

                if store_data['priceFormat']:
                    priceFormat_list.append(store_data['priceFormat'])

                else:
                    priceFormat_list.append("-----")


            else:
                priceFormat_list.append("key missing")



            if 'priceSuffix' in store_data:

                if store_data['priceSuffix']:
                    priceSuffix_list.append(store_data['priceSuffix'])

                else:
                    priceSuffix_list.append("-----")


            else:
                priceSuffix_list.append("key missing")



            if 'storeUrl' in store_data:

                if store_data['storeUrl']:
                    storeUrl_list.append(store_data['storeUrl'])

                else:
                    storeUrl_list.append("-----")


            else:
                storeUrl_list.append("key missing")




            if 'text_zipcode_enabled' in store_data:

                if store_data['text_zipcode_enabled']:
                    
                    text_zipcode_enabled_list.append(store_data['text_zipcode_enabled'] )

                
                    
                else:
                    
                    text_zipcode_enabled_list.append(store_data['text_zipcode_enabled'])

            else:
                text_zipcode_enabled_list.append("key missing")




            if 'status' in store_data:

                if store_data['status']:
                    status_list.append(store_data['status'])

                else:
                    status_list.append("-----")


            else:
                status_list.append("key missing")





            if 'addonflags' in store_data:

                    v = store_data['addonflags']
                    if 'abandonedCartEnabled' in store_data['addonflags']:
        
                        if v:
                            abandonedCartEnabled_list.append(v['abandonedCartEnabled'])

                        else:
                            abandonedCartEnabled_list.append(v['abandonedCartEnabled'])
                    
                    else:
                        abandonedCartEnabled_list.append("key missing")
            


                    if 'autoApplyCouponEnabled' in store_data['addonflags']:
        
                        if v:
                            autoApplyCouponEnabled_list.append(v['autoApplyCouponEnabled'])

                        else:
                            autoApplyCouponEnabled_list.append(v['autoApplyCouponEnabled'])
                    
                    else:
                        autoApplyCouponEnabled_list.append("key missing")
            
                



                    if 'backToStockAlertEnaled' in store_data['addonflags']:
        
                        if v:
                            backToStockAlertEnaled_list.append(v['backToStockAlertEnaled'])

                        else:
                            backToStockAlertEnaled_list.append(v['backToStockAlertEnaled'])
                    
                    else:
                        backToStockAlertEnaled_list.append("key missing")
            
                



                    if 'blogEnabled' in store_data['addonflags']:
        
                        if v:
                            blogEnabled_list.append(v['blogEnabled'])

                        else:
                            blogEnabled_list.append(v['blogEnabled'])
                    
                    else:
                        blogEnabled_list.append("key missing")
            
                





                    if 'branchSDKEnabled' in store_data['addonflags']:
        
                        if v:
                            branchSDKEnabled_list.append(v['branchSDKEnabled'])

                        else:
                            branchSDKEnabled_list.append(v['branchSDKEnabled'])
                    
                    else:
                        branchSDKEnabled_list.append("key missing")
            
                




                    if 'brandPlaceholderEnabled' in store_data['addonflags']:
        
                        if v:
                            brandPlaceholderEnabled_list.append(v['brandPlaceholderEnabled'])

                        else:
                            brandPlaceholderEnabled_list.append(v['brandPlaceholderEnabled'])
                    
                    else:
                        brandPlaceholderEnabled_list.append("key missing")
            
                




                    if 'cleverTapEnabled' in store_data['addonflags']:
        
                        if v:
                            cleverTapEnabled_list.append(v['cleverTapEnabled'])

                        else:
                            cleverTapEnabled_list.append(v['cleverTapEnabled'])
                    
                    else:
                        cleverTapEnabled_list.append("key missing")
            
                




                    if 'crossSellEnabled' in store_data['addonflags']:
        
                        if v:
                            crossSellEnabled_list.append(v['crossSellEnabled'])

                        else:
                            crossSellEnabled_list.append(v['crossSellEnabled'])
                    
                    else:
                        crossSellEnabled_list.append("key missing")
            
                




                    if 'customProductOptionsEnabled' in store_data['addonflags']:
        
                        if v:
                            customProductOptionsEnabled_list.append(v['customProductOptionsEnabled'])

                        else:
                            customProductOptionsEnabled_list.append(v['customProductOptionsEnabled'])
                    
                    else:
                        customProductOptionsEnabled_list.append("key missing")
            
                





                    if 'customerChatEnabled' in store_data['addonflags']:
        
                        if v:
                            customerChatEnabled_list.append(v['customerChatEnabled'])

                        else:
                            customerChatEnabled_list.append(v['customerChatEnabled'])
                    
                    else:
                        customerChatEnabled_list.append("key missing")
            
               





                    if 'deliveryAreaEnabled' in store_data['addonflags']:
        
                        if v:
                            deliveryAreaEnabled_list.append(v['deliveryAreaEnabled'])

                        else:
                            deliveryAreaEnabled_list.append(v['deliveryAreaEnabled'])
                    
                    else:
                        deliveryAreaEnabled_list.append("key missing")
            
                




                    if 'deliveryOptionsEnabled' in store_data['addonflags']:
        
                        if v:
                            deliveryOptionsEnabled_list.append(v['deliveryOptionsEnabled'])

                        else:
                            deliveryOptionsEnabled_list.append(v['deliveryOptionsEnabled'])
                    
                    else:
                        deliveryOptionsEnabled_list.append("key missing")
            
                





                    if 'deliverySlotEnabled' in store_data['addonflags']:
        
                        if v:
                            deliverySlotEnabled_list.append(v['deliverySlotEnabled'])

                        else:
                            deliverySlotEnabled_list.append(v['deliverySlotEnabled'])
                    
                    else:
                        deliverySlotEnabled_list.append("key missing")
            
                






                    if 'fbLoginEnabled' in store_data['addonflags']:
        
                        if v:
                            fbLoginEnabled_list.append(v['fbLoginEnabled'])

                        else:
                            fbLoginEnabled_list.append(v['fbLoginEnabled'])
                    
                    else:
                        fbLoginEnabled_list.append("key missing")
            
                






                    if 'firebaseAnalyticsEnabled' in store_data['addonflags']:
        
                        if v:
                            firebaseAnalyticsEnabled_list.append(v['firebaseAnalyticsEnabled'])

                        else:
                            firebaseAnalyticsEnabled_list.append(v['firebaseAnalyticsEnabled'])
                    
                    else:
                        firebaseAnalyticsEnabled_list.append("key missing")
            
                



                    

                    
                    if 'flitsEnabled' in store_data['addonflags']:
        
                        if v:
                            flitsEnabled_list.append(v['flitsEnabled'])

                        else:
                            flitsEnabled_list.append(v['flitsEnabled'])
                    
                    else:
                        flitsEnabled_list.append("key missing")
           
                





                    if 'googleLoginEnabled' in store_data['addonflags']:
        
                        if v:
                            googleLoginEnabled_list.append(v['googleLoginEnabled'])

                        else:
                            googleLoginEnabled_list.append(v['googleLoginEnabled'])
                    
                    else:
                        googleLoginEnabled_list.append("key missing")
           
                




                    if 'guestCheckoutEnabled' in store_data['addonflags']:
        
                        if v:
                            guestCheckoutEnabled_list.append(v['guestCheckoutEnabled'])

                        else:
                            guestCheckoutEnabled_list.append(v['guestCheckoutEnabled'])
                    
                    else:
                        guestCheckoutEnabled_list.append("key missing")
            
                





                    if 'isForceUpdate' in store_data['addonflags']:
        
                        if v:
                            isForceUpdate_list.append(v['isForceUpdate'])

                        else:
                            isForceUpdate_list.append(v['isForceUpdate'])
                    
                    else:
                        isForceUpdate_list.append("key missing")
            
                





                    if 'shopifyMobileSalesChannelEnabled' in store_data['addonflags']:
        
                        if v:
                            shopifyMobileSalesChannelEnabled_list.append(v['shopifyMobileSalesChannelEnabled'])

                        else:
                            shopifyMobileSalesChannelEnabled_list.append(v['shopifyMobileSalesChannelEnabled'])
                    
                    else:
                        shopifyMobileSalesChannelEnabled_list.append("key missing")
           






                    if 'multiLanguageEnabled' in store_data['addonflags']:
        
                        if v:
                            multiLanguageEnabled_list.append(v['multiLanguageEnabled'])

                        else:
                            multiLanguageEnabled_list.append(v['multiLanguageEnabled'])
                    
                    else:
                        multiLanguageEnabled_list.append("key missing")





                    if 'multiVendorCheckoutEnabled' in store_data['addonflags']:
        
                        if v:
                            multiVendorCheckoutEnabled_list.append(v['multiVendorCheckoutEnabled'])

                        else:
                            multiVendorCheckoutEnabled_list.append(v['multiVendorCheckoutEnabled'])
                    
                    else:
                        multiVendorCheckoutEnabled_list.append("key missing")







                    if 'nativeCheckoutEnabled' in store_data['addonflags']:
        
                        if v:
                            nativeCheckoutEnabled_list.append(v['nativeCheckoutEnabled'])

                        else:
                            nativeCheckoutEnabled_list.append(v['nativeCheckoutEnabled'])
                    
                    else:
                        nativeCheckoutEnabled_list.append("key missing")






                    if 'nativeCheckoutProcessEnabled' in store_data['addonflags']:
        
                        if v:
                            nativeCheckoutProcessEnabled_list.append(v['nativeCheckoutProcessEnabled'])

                        else:
                            nativeCheckoutProcessEnabled_list.append(v['nativeCheckoutProcessEnabled'])
                    
                    else:
                        nativeCheckoutProcessEnabled_list.append("key missing")




                    if 'new_cart_design_enabled' in store_data['addonflags']:
        
                        if v:
                            new_cart_design_enabled_list.append(v['new_cart_design_enabled'])

                        else:
                            new_cart_design_enabled_list.append(v['new_cart_design_enabled'])
                    
                    else:
                        new_cart_design_enabled_list.append("key missing")





                    if 'postAffiliateProEnabled' in store_data['addonflags']:
        
                        if v:
                            postAffiliateProEnabled_list.append(v['postAffiliateProEnabled'])

                        else:
                            postAffiliateProEnabled_list.append(v['postAffiliateProEnabled'])
                    
                    else:
                        postAffiliateProEnabled_list.append("key missing")



                    if 'productGridWishlistEnabled' in store_data['addonflags']:
        
                        if v:
                            productGridWishlistEnabled_list.append(v['productGridWishlistEnabled'])

                        else:
                            productGridWishlistEnabled_list.append(v['productGridWishlistEnabled'])
                    
                    else:
                        productGridWishlistEnabled_list.append("key missing")




                    if 'productReviewsEnabled' in store_data['addonflags']:
        
                        if v:
                            productReviewsEnabled_list.append(v['productReviewsEnabled'])

                        else:
                            productReviewsEnabled_list.append(v['productReviewsEnabled'])
                    
                    else:
                        productReviewsEnabled_list.append("key missing")



                    if 'rateUsEnabled' in store_data['addonflags']:
        
                        if v:
                            rateUsEnabled_list.append(v['rateUsEnabled'])

                        else:
                            rateUsEnabled_list.append(v['rateUsEnabled'])
                    
                    else:
                        rateUsEnabled_list.append("key missing")



                    if 'refreshCartEnabled' in store_data['addonflags']:
        
                        if v:
                            refreshCartEnabled_list.append(v['refreshCartEnabled'])

                        else:
                            refreshCartEnabled_list.append(v['refreshCartEnabled'])
                    
                    else:
                        refreshCartEnabled_list.append("key missing")



                    if 'reorderEnabled' in store_data['addonflags']:
        
                        if v:
                            reorderEnabled_list.append(v['reorderEnabled'])

                        else:
                            reorderEnabled_list.append(v['reorderEnabled'])
                    
                    else:
                        reorderEnabled_list.append("key missing")


                    if 'rewardEnabled' in store_data['addonflags']:
        
                        if v:
                            rewardEnabled_list.append(v['rewardEnabled'])

                        else:
                            rewardEnabled_list.append(v['rewardEnabled'])
                    
                    else:
                        rewardEnabled_list.append("key missing")




                    if 'shareCollectionEnabled' in store_data['addonflags']:
        
                        if v:
                            shareCollectionEnabled_list.append(v['shareCollectionEnabled'])

                        else:
                            shareCollectionEnabled_list.append(v['shareCollectionEnabled'])
                    
                    else:
                        shareCollectionEnabled_list.append("key missing")




                    if 'sortFilterEnabled' in store_data['addonflags']:
        
                        if v:
                            sortFilterEnabled_list.append(v['sortFilterEnabled'])

                        else:
                            sortFilterEnabled_list.append(v['sortFilterEnabled'])
                    
                    else:
                        sortFilterEnabled_list.append("key missing")






                    if 'suggestionsEnabled' in store_data['addonflags']:
        
                        if v:
                            suggestionsEnabled_list.append(v['suggestionsEnabled'])

                        else:
                            suggestionsEnabled_list.append(v['suggestionsEnabled'])
                    
                    else:
                        suggestionsEnabled_list.append("key missing")







                    if 'deliveryRegionEnabled' in store_data['addonflags']:
        
                        if v:
                            deliveryRegionEnabled_list.append(v['deliveryRegionEnabled'])

                        else:
                            deliveryRegionEnabled_list.append(v['deliveryRegionEnabled'])
                    
                    else:
                        deliveryRegionEnabled_list.append("key missing")



                    if 'liveVideoEnabled' in store_data['addonflags']:
        
                        if v:
                            liveVideoEnabled_list.append(v['liveVideoEnabled'])

                        else:
                            liveVideoEnabled_list.append(v['liveVideoEnabled'])
                    
                    else:
                        liveVideoEnabled_list.append("key missing")



                    if 'orderNoteEnabled' in store_data['addonflags']:
        
                        if v:
                            orderNoteEnabled_list.append(v['orderNoteEnabled'])

                        else:
                            orderNoteEnabled_list.append(v['orderNoteEnabled'])
                    
                    else:
                        orderNoteEnabled_list.append("key missing")




                    if 'showLineItemCount' in store_data['addonflags']:
        
                        if v:
                            showLineItemCount_list.append(v['showLineItemCount'])

                        else:
                            showLineItemCount_list.append(v['showLineItemCount'])
                    
                    else:
                        showLineItemCount_list.append("key missing")




                    if 'webAppleGooglePayEnabled' in store_data['addonflags']:
        
                        if v:
                            webAppleGooglePayEnabled_list.append(v['webAppleGooglePayEnabled'])

                        else:
                            webAppleGooglePayEnabled_list.append(v['webAppleGooglePayEnabled'])
                    
                    else:
                        webAppleGooglePayEnabled_list.append("key missing")




                    if 'applePayEnabled' in store_data['addonflags']:
        
                        if v:
                            applePayEnabled_list.append(v['applePayEnabled'])

                        else:
                            applePayEnabled_list.append(v['applePayEnabled'])
                    
                    else:
                        applePayEnabled_list.append("key missing")



                    if 'smartSearchEnabled' in store_data['addonflags']:
        
                        if v:
                            smartSearchEnabled_list.append(v['smartSearchEnabled'])

                        else:
                            smartSearchEnabled_list.append(v['smartSearchEnabled'])
                    
                    else:
                        smartSearchEnabled_list.append("key missing")



                    if 'deepLinkingEnabled' in store_data['addonflags']:
        
                        if v:
                            deepLinkingEnabled_list.append(v['deepLinkingEnabled'])

                        else:
                            deepLinkingEnabled_list.append(v['deepLinkingEnabled'])
                    
                    else:
                        deepLinkingEnabled_list.append("key missing")



                    if 'switch_search_suggestion_section' in store_data['addonflags']:
        
                        if v:
                            switch_search_suggestion_section_list.append(v['switch_search_suggestion_section'])

                        else:
                            switch_search_suggestion_section_list.append(v['switch_search_suggestion_section'])
                    
                    else:
                        switch_search_suggestion_section_list.append("key missing")




                    if 'savedSearchNotifEnabled' in store_data['addonflags']:
        
                        if v:
                            savedSearchNotifEnabled_list.append(v['savedSearchNotifEnabled'])

                        else:
                            savedSearchNotifEnabled_list.append(v['savedSearchNotifEnabled'])
                    
                    else:
                        savedSearchNotifEnabled_list.append("key missing")





                    if 'appsflyerEnabled' in store_data['addonflags']:
        
                        if v:
                            appsflyerEnabled_list.append(v['appsflyerEnabled'])

                        else:
                            appsflyerEnabled_list.append(v['appsflyerEnabled'])
                    
                    else:
                        appsflyerEnabled_list.append("key missing")





                    if 'boldSubscriptionEnabled' in store_data['addonflags']:
        
                        if v:
                            boldSubscriptionEnabled_list.append(v['boldSubscriptionEnabled'])

                        else:
                            boldSubscriptionEnabled_list.append(v['boldSubscriptionEnabled'])
                    
                    else:
                        boldSubscriptionEnabled_list.append("key missing")



                    if 'christmasModeEnabled' in store_data['addonflags']:
        
                        if v:
                            christmasModeEnabled_list.append(v['christmasModeEnabled'])

                        else:
                            christmasModeEnabled_list.append(v['christmasModeEnabled'])
                    
                    else:
                        christmasModeEnabled_list.append("key missing")




                    if 'imageSearchEnabled' in store_data['addonflags']:
        
                        if v:
                            imageSearchEnabled_list.append(v['imageSearchEnabled'])

                        else:
                            imageSearchEnabled_list.append(v['imageSearchEnabled'])
                    
                    else:
                        imageSearchEnabled_list.append("key missing")



                    if 'rewardifyEnabled' in store_data['addonflags']:
        
                        if v:
                            rewardifyEnabled_list.append(v['rewardifyEnabled'])

                        else:
                            rewardifyEnabled_list.append(v['rewardifyEnabled'])
                    
                    else:
                        rewardifyEnabled_list.append("key missing")



                    if 'valentinesDayEnabled' in store_data['addonflags']:
        
                        if v:
                            valentinesDayEnabled_list.append(v['valentinesDayEnabled'])

                        else:
                            valentinesDayEnabled_list.append(v['valentinesDayEnabled'])
                    
                    else:
                        valentinesDayEnabled_list.append("key missing")





                    if 'swapMyShopifyDomain' in store_data['addonflags']:
        
                        if v:
                            swapMyShopifyDomain_list.append(v['swapMyShopifyDomain'])

                        else:
                            swapMyShopifyDomain_list.append(v['swapMyShopifyDomain'])
                    
                    else:
                        swapMyShopifyDomain_list.append("key missing")





                    if 'agePopupEnabled' in store_data['addonflags']:
        
                        if v:
                            agePopupEnabled_list.append(v['agePopupEnabled'])

                        else:
                            agePopupEnabled_list.append(v['agePopupEnabled'])
                    
                    else:
                        agePopupEnabled_list.append("key missing")




                    if 'viaEnabled' in store_data['addonflags']:
        
                        if v:
                            viaEnabled_list.append(v['viaEnabled'])

                        else:
                            viaEnabled_list.append(v['viaEnabled'])
                    
                    else:
                        viaEnabled_list.append("key missing")




                    if 'quantityBreaksEnabled' in store_data['addonflags']:
        
                        if v:
                            quantityBreaksEnabled_list.append(v['quantityBreaksEnabled'])

                        else:
                            quantityBreaksEnabled_list.append(v['quantityBreaksEnabled'])
                    
                    else:
                        quantityBreaksEnabled_list.append("key missing")





                    if 'browserDeeplinkEnabled' in store_data['addonflags']:
        
                        if v:
                            browserDeeplinkEnabled_list.append(v['browserDeeplinkEnabled'])

                        else:
                            browserDeeplinkEnabled_list.append(v['browserDeeplinkEnabled'])
                    
                    else:
                        browserDeeplinkEnabled_list.append("key missing")





                    if 'multiCurrencyEnabled' in store_data['addonflags']:
        
                        if v:
                            multiCurrencyEnabled_list.append(v['multiCurrencyEnabled'])

                        else:
                            multiCurrencyEnabled_list.append(v['multiCurrencyEnabled'])
                    
                    else:
                        multiCurrencyEnabled_list.append("key missing")




                    if 'pullToRefreshEnabled' in store_data['addonflags']:
        
                        if v:
                            pullToRefreshEnabled_list.append(v['pullToRefreshEnabled'])

                        else:
                            pullToRefreshEnabled_list.append(v['pullToRefreshEnabled'])
                    
                    else:
                        pullToRefreshEnabled_list.append("key missing")




                    if 'related_products_enabled' in store_data['addonflags']:
        
                        if v:
                            related_products_enabled_list.append(v['related_products_enabled'])

                        else:
                            related_products_enabled_list.append(v['related_products_enabled'])
                    
                    else:
                        related_products_enabled_list.append("key missing")





                    if 'show_collection_description' in store_data['addonflags']:
        
                        if v:
                            show_collection_description_list.append(v['show_collection_description'])

                        else:
                            show_collection_description_list.append(v['show_collection_description'])
                    
                    else:
                        show_collection_description_list.append("key missing")




                    if 'shopifyEmiEnabled' in store_data['addonflags']:
        
                        if v:
                            shopifyEmiEnabled_list.append(v['shopifyEmiEnabled'])

                        else:
                            shopifyEmiEnabled_list.append(v['shopifyEmiEnabled'])
                    
                    else:
                        shopifyEmiEnabled_list.append("key missing")





                    if 'mobileSalesChannelEnabled' in store_data['addonflags']:
        
                        if v:
                            mobileSalesChannelEnabled_list.append(v['mobileSalesChannelEnabled'])

                        else:
                            mobileSalesChannelEnabled_list.append(v['mobileSalesChannelEnabled'])
                    
                    else:
                        mobileSalesChannelEnabled_list.append("key missing")
            else:
                
                abandonedCartEnabled_list.append("addon flag key missing")
                autoApplyCouponEnabled_list.append("addon flag key missing")
                backToStockAlertEnaled_list.append("addon flag key missing")
                blogEnabled_list.append("addon flag key missing")
                branchSDKEnabled_list.append("addon flag key missing")
                brandPlaceholderEnabled_list.append("addon flag key missing")
                cleverTapEnabled_list.append("addon flag key missing")
                crossSellEnabled_list.append("addon flag key missing")
                customProductOptionsEnabled_list.append("addon flag key missing")
                customerChatEnabled_list.append("addon flag key missing")
                deliveryAreaEnabled_list.append("addon flag key missing")
                deliveryOptionsEnabled_list.append("addon flag key missing")
                deliverySlotEnabled_list.append("addon flag key missing")
                fbLoginEnabled_list.append("addon flag key missing")
                firebaseAnalyticsEnabled_list.append("addon flag key missing")
                flitsEnabled_list.append("addon flag key missing")
                googleLoginEnabled_list.append("addon flag key missing")
                guestCheckoutEnabled_list.append("addon flag key missing")
                isForceUpdate_list.append("addon flag key missing")
                shopifyMobileSalesChannelEnabled_list.append("addon flag key missing")
                multiLanguageEnabled_list.append("addon flag key missing")
                multiVendorCheckoutEnabled_list.append("addon flag key missing")
                nativeCheckoutEnabled_list.append("addon flag key missing")
                nativeCheckoutProcessEnabled_list.append("addon flag key missing")
                new_cart_design_enabled_list.append("addon flag key missing")
                postAffiliateProEnabled_list.append("addon flag key missing")
                productGridWishlistEnabled_list.append("addon flag key missing")
                productReviewsEnabled_list.append("addon flag key missing")
                rateUsEnabled_list.append("addon flag key missing")
                refreshCartEnabled_list.append("addon flag key missing")
                reorderEnabled_list.append("addon flag key missing")
                rewardEnabled_list.append("addon flag key missing")
                shareCollectionEnabled_list.append("addon flag key missing")
                sortFilterEnabled_list.append("addon flag key missing")
                suggestionsEnabled_list.append("addon flag key missing")
                deliveryRegionEnabled_list.append("addon flag key missing")
                liveVideoEnabled_list.append("addon flag key missing")
                orderNoteEnabled_list.append("addon flag key missing")
                showLineItemCount_list.append("addon flag key missing")
                webAppleGooglePayEnabled_list.append("addon flag key missing")
                applePayEnabled_list.append("addon flag key missing")
                smartSearchEnabled_list.append("addon flag key missing")
                deepLinkingEnabled_list.append("addon flag key missing")
                switch_search_suggestion_section_list.append("addon flag key missing")
                savedSearchNotifEnabled_list.append("addon flag key missing")
                appsflyerEnabled_list.append("addon flag key missing")
                boldSubscriptionEnabled_list.append("addon flag key missing")
                christmasModeEnabled_list.append("addon flag key missing")
                imageSearchEnabled_list.append("addon flag key missing")
                rewardifyEnabled_list.append("addon flag key missing")
                valentinesDayEnabled_list.append("addon flag key missing")
                swapMyShopifyDomain_list.append("addon flag key missing")
                agePopupEnabled_list.append("addon flag key missing")
                viaEnabled_list.append("addon flag key missing")
                quantityBreaksEnabled_list.append("addon flag key missing")
                browserDeeplinkEnabled_list.append("addon flag key missing")
                multiCurrencyEnabled_list.append("addon flag key missing")
                pullToRefreshEnabled_list.append("addon flag key missing")
                related_products_enabled_list.append("addon flag key missing")
                show_collection_description_list.append("addon flag key missing")
                shopifyEmiEnabled_list.append("addon flag key missing")
                mobileSalesChannelEnabled_list.append("addon flag key missing")

            if 'colors' in store_data:
                v = store_data['colors']
                if 'accent_color' in store_data['colors']:
        
                    if v:
                        if len(v['accent_color'])==7 and v['accent_color'][0]=='#':
                            accent_color_list.append(v['accent_color'])

                        else:
                            accent_color_list.append("error")
                    
                else:
                    accent_color_list.append("key missing")




                if 'badge_color' in store_data['colors']:
        
                    if v:
                        if len(v['badge_color'])==7 and v['badge_color'][0]=='#':
                            badge_color_list.append(v['badge_color'])

                        else:
                            badge_color_list.append("error")
                    
                else:
                    badge_color_list.append("key missing")




                if 'badge_text_color' in store_data['colors']:
        
                    if v:
                        if len(v['badge_text_color'])==7 and v['badge_text_color'][0]=='#':
                            badge_text_color_list.append(v['badge_text_color'])

                        else:
                            badge_text_color_list.append("error")
                    
                else:
                    badge_text_color_list.append("key missing")





                if 'buy_button_color' in store_data['colors']:
        
                    if v:
                        if len(v['buy_button_color'])==7 and v['buy_button_color'][0]=='#':
                            buy_button_color_list.append(v['buy_button_color'])
    
                    else:
                            buy_button_color_list.append("error")
                        
                else:
                    buy_button_color_list.append("key missing")





                if 'option_value_color' in store_data['colors']:
        
                    if v:
                        if len(v['option_value_color'])==7 and v['option_value_color'][0]=='#':
                            option_value_color_list.append(v['option_value_color'])

                        else:
                            option_value_color_list.append("error")
                    
                else:
                    option_value_color_list.append("key missing")




                if 'primary_color' in store_data['colors']:
        
                    if v:
                        if len(v['primary_color'])==7 and v['primary_color'][0]=='#':
                            primary_color_list.append(v['primary_color'])

                        else:
                            primary_color_list.append("error")
                    
                else:
                    primary_color_list.append("key missing")




                if 'primary_color_dark' in store_data['colors']:
        
                    if v:
                        if len(v['primary_color_dark'])==7 and v['primary_color_dark'][0]=='#':
                            primary_color_dark_list.append(v['primary_color_dark'])

                        else:
                            primary_color_dark_list.append("error")
                    
                else:
                    primary_color_dark_list.append("key missing")




                if 'share_button_color' in store_data['colors']:
        
                    if v:
                        if len(v['share_button_color'])==7 and v['share_button_color'][0]=='#':
                            share_button_color_list.append(v['share_button_color'])

                        else:
                            share_button_color_list.append("error")
                    
                else:
                    share_button_color_list.append("key missing")



                if 'splash_bg_color' in store_data['colors']:
        
                    if v:
                        if len(v['splash_bg_color'])==7 and v['splash_bg_color'][0]=='#':
                            splash_bg_color_list.append(v['splash_bg_color'])

                        else:
                            splash_bg_color_list.append("error")
                    
                else:
                    splash_bg_color_list.append("key missing")




                if 'splash_spinner_color' in store_data['colors']:
        
                    if v:
                        if len(v['splash_spinner_color'])==7 and v['splash_spinner_color'][0]=='#':
                            splash_spinner_color_list.append(v['splash_spinner_color'])

                        else:
                            splash_spinner_color_list.append("error")
                    
                else:
                    splash_spinner_color_list.append("key missing")




                if 'sub_collection_color' in store_data['colors']:
        
                    if v:
                        if len(v['sub_collection_color'])==7 and v['sub_collection_color'][0]=='#':
                            sub_collection_color_list.append(v['sub_collection_color'])

                        else:
                            sub_collection_color_list.append("error")
                    
                else:
                    sub_collection_color_list.append("key missing")





                if 'toolbar_color' in store_data['colors']:
        
                    if v:
                        if len(v['toolbar_color'])==7 and v['toolbar_color'][0]=='#':
                            toolbar_color_list.append(v['toolbar_color'])

                        else:
                            toolbar_color_list.append("error")
                    
                else:
                    toolbar_color_list.append("key missing")




                if 'toolbar_content_color' in store_data['colors']:
        
                    if v:
                        if len(v['toolbar_content_color'])==7 and v['toolbar_content_color'][0]=='#':
                            toolbar_content_color_list.append(v['toolbar_content_color'])

                        else:
                            toolbar_content_color_list.append("error")
                    
                else:
                    toolbar_content_color_list.append("key missing")





                if 'discount_color' in store_data['colors']:
        
                    if v:
                        if len(v['discount_color'])==7 and v['discount_color'][0]=='#':
                            discount_color_list.append(v['discount_color'])

                        else:
                            discount_color_list.append("error")
                    
                else:
                    discount_color_list.append("key missing")




                if 'vendor_color' in store_data['colors']:
        
                    if v:
                        if len(v['vendor_color'])==7 and v['vendor_color'][0]=='#':
                            vendor_color_list.append(v['vendor_color'])

                        else:
                            vendor_color_list.append("error")
                    
                else:
                    vendor_color_list.append("key missing")

            else:
                accent_color_list.append("colors key missing")
                badge_color_list.append("colors key missing")
                badge_text_color_list.append("colors key missing")
                buy_button_color_list.append("colors key missing")
                option_value_color_list.append("colors key missing")
                primary_color_list.append("colors key missing")
                primary_color_dark_list.append("colors key missing")
                share_button_color_list.append("colors key missing")
                splash_bg_color_list.append("colors key missing")
                splash_spinner_color_list.append("colors key missing")
                sub_collection_color_list.append("colors key missing")
                toolbar_color_list.append("colors key missing")
                toolbar_content_color_list.append("colors key missing")
                discount_color_list.append("colors key missing")
                vendor_color_list.append("colors key missing")







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
            appid_list.append(j)
            bottom_bar_list.append("invalid")
            name_list.append("invalid")
            platform_list.append("invalid")
            storeUrl_list.append("invalid")
            isactive_list.append("invalid")
            isTrial_list.append("invalid")
            custom_font_bold_list.append("invalid")
            custom_font_regular_list.append("invalid")
            currency_comma_enabled_list.append("invalid")
            default_country_list.append("invalid")
            default_language_list.append("invalid")
            iso_currency_code_list.append("invalid")
            logo_list.append("invalid")
            priceFormat_list.append("invalid")
            priceSuffix_list.append("invalid")
            text_zipcode_enabled_list.append("invalid")
            status_list.append("invalid")
            abandonedCartEnabled_list.append("invalid")
            autoApplyCouponEnabled_list.append("invalid")
            backToStockAlertEnaled_list.append("invalid")
            blogEnabled_list.append("invalid")
            branchSDKEnabled_list.append("invald")
            brandPlaceholderEnabled_list.append("invalid")
            cleverTapEnabled_list.append("invalid")
            crossSellEnabled_list.append("invalid")
            customProductOptionsEnabled_list.append("invalid")
            customerChatEnabled_list.append("invalid")
            deliveryAreaEnabled_list.append("invalid")
            deliveryOptionsEnabled_list.append("invalid")
            deliverySlotEnabled_list.append("invalid")
            fbLoginEnabled_list.append("invalid")
            firebaseAnalyticsEnabled_list.append("invalid")
            flitsEnabled_list.append("invalid")
            googleLoginEnabled_list.append("invalid")
            guestCheckoutEnabled_list.append("invalid")
            isForceUpdate_list.append("invalid")
            shopifyMobileSalesChannelEnabled_list.append("invalid")
            multiLanguageEnabled_list.append("invalid")
            multiVendorCheckoutEnabled_list.append("invalid")
            nativeCheckoutEnabled_list.append("invalid")
            nativeCheckoutProcessEnabled_list.append("invalid")
            new_cart_design_enabled_list.append("invalid")
            postAffiliateProEnabled_list.append("invalid")
            productGridWishlistEnabled_list.append("invalid")
            productReviewsEnabled_list.append("invalid")
            rateUsEnabled_list.append("invalid")
            refreshCartEnabled_list.append("invalid")
            reorderEnabled_list.append("invalid")
            rewardEnabled_list.append("invalid")
            shareCollectionEnabled_list.append("invalid")
            sortFilterEnabled_list.append("invalid")
            suggestionsEnabled_list.append("invalid")
            deliveryRegionEnabled_list.append("invalid")
            liveVideoEnabled_list.append("invalid")
            orderNoteEnabled_list.append("invalid")
            showLineItemCount_list.append("invalid")
            webAppleGooglePayEnabled_list.append("invalid")
            applePayEnabled_list.append("invalid")
            smartSearchEnabled_list.append("invalid")
            deepLinkingEnabled_list.append("invalid")
            switch_search_suggestion_section_list.append("invalid")
            savedSearchNotifEnabled_list.append("invalid")
            appsflyerEnabled_list.append("invalid")
            boldSubscriptionEnabled_list.append("invalid")
            christmasModeEnabled_list.append("invalid")
            imageSearchEnabled_list.append("invalid")
            rewardifyEnabled_list.append("invalid")
            valentinesDayEnabled_list.append("invalid")
            swapMyShopifyDomain_list.append("invalid")
            agePopupEnabled_list.append("invalid")
            viaEnabled_list.append("invalid")
            quantityBreaksEnabled_list.append("invalid")
            browserDeeplinkEnabled_list.append("invalid")
            multiCurrencyEnabled_list.append("invalid")
            pullToRefreshEnabled_list.append("invalid")
            related_products_enabled_list.append("invalid")
            show_collection_description_list.append("invalid")
            shopifyEmiEnabled_list.append("invalid")
            mobileSalesChannelEnabled_list.append("invalid")
            accent_color_list.append("invalid")
            badge_color_list.append("invalid")
            badge_text_color_list.append("invalid")
            buy_button_color_list.append("invalid")
            option_value_color_list.append("invalid")
            primary_color_list.append("invalid")
            primary_color_dark_list.append("invalid")
            share_button_color_list.append("invalid")
            splash_bg_color_list.append("invalid")
            splash_spinner_color_list.append("invalid")
            sub_collection_color_list.append("invalid")
            toolbar_color_list.append("invalid")
            toolbar_content_color_list.append("invalid")
            discount_color_list.append("invalid")
            vendor_color_list.append("invalid")
            social_login_list.append("invalid")
            android_google_client_id_list.append("invalid")
            google_client_id_list.append("invalid") 
            google_uri_scheme_list.append("invalid")








                
    output = {'#001appid' : appid_list ,
                  '#002name' : name_list,
                  '#003platform' : platform_list,
                  '#004storeUrl' : storeUrl_list ,
                  '#005_bottom_bar' : bottom_bar_list, 
                  '#006isActive'  : isactive_list ,
                  '#007isTrial' : isTrial_list ,
                  '#008custom_font_bold' : custom_font_bold_list ,
                  '#009custom_font_regular' : custom_font_regular_list,
                  '#010currency_comma_enabled': currency_comma_enabled_list ,
                  '#011default_country' : default_country_list ,
                  '#012default_language' : default_language_list,
                  '#013iso_currency_code' : iso_currency_code_list,
                  '#014logo' : logo_list ,
                  '#015priceFormat' : priceFormat_list ,
                  '#016priceSuffix' : priceSuffix_list ,
                  '#017text_zipcode_enabled' : text_zipcode_enabled_list ,
                  '#018status' : status_list,
                  '#019abandonedCartEnabled' :abandonedCartEnabled_list,
                  '#020autoApplyCouponEnabled' :autoApplyCouponEnabled_list,
                  '#021backToStockAlertEnaled' :backToStockAlertEnaled_list,
                  '#022blogEnabled' : blogEnabled_list,
                  '#023branchSDKEnabled' : branchSDKEnabled_list,
                  '#024brandPlaceholderEnabled' : brandPlaceholderEnabled_list,
                  '#025cleverTapEnabled' : cleverTapEnabled_list,
                  '#026crossSellEnabled' : crossSellEnabled_list,
                  '#027customProductOptionsEnabled' : customProductOptionsEnabled_list,
                  '#028customerChatEnabled' : customerChatEnabled_list,
                  '#029deliveryAreaEnabled' : deliveryAreaEnabled_list,
                  '#030deliveryOptionsEnabled' : deliveryOptionsEnabled_list,
                  '#031deliverySlotEnabled' : deliverySlotEnabled_list,
                  '#032fbLoginEnabled' : fbLoginEnabled_list ,
                  '#033firebaseAnalyticsEnabled' : firebaseAnalyticsEnabled_list,
                  '#034flitsEnabled' : flitsEnabled_list,
                  '#035googleLoginEnabled' : googleLoginEnabled_list,
                  '#036guestCheckoutEnabled' : guestCheckoutEnabled_list,
                  '#037isForceUpdate' : isForceUpdate_list,
                  '#038shopifyMobileSalesChannelEnabled' : shopifyMobileSalesChannelEnabled_list,
                  '#039multiLanguageEnabled' : multiLanguageEnabled_list,
                  '#040multiVendorCheckoutEnabled' : multiVendorCheckoutEnabled_list,
                  '#041nativeCheckoutEnabled' : nativeCheckoutEnabled_list,
                  '#042nativeCheckoutProcessEnabled' : nativeCheckoutProcessEnabled_list,
                  '#043new_cart_design_enabled' : new_cart_design_enabled_list,
                  '#044postAffiliateProEnabled' :postAffiliateProEnabled_list ,
                  '#045productGridWishlistEnabled' : productGridWishlistEnabled_list,
                  '#046productReviewsEnabled_list' : productReviewsEnabled_list,
                  '#047rateUsEnabled_list' : rateUsEnabled_list,
                  '#048refreshCartEnabled' :refreshCartEnabled_list,
                  '#049reorderEnabled' : reorderEnabled_list,
                  '#050rewardEnabled' : rewardEnabled_list,
                  '#051shareCollectionEnabled' : shareCollectionEnabled_list,
                  '#052sortFilterEnabled' : sortFilterEnabled_list,
                  '#053suggestionsEnabled' : suggestionsEnabled_list,
                  '#054deliveryRegionEnabled' : deliveryRegionEnabled_list,
                  '#055liveVideoEnabled' : liveVideoEnabled_list,
                  '#056orderNoteEnabled' : orderNoteEnabled_list,
                  '#057showLineItemCount' : showLineItemCount_list,
                  '#058webAppleGooglePayEnabled' : webAppleGooglePayEnabled_list,
                  '#059applePayEnabled' : applePayEnabled_list,
                  '#060smartSearchEnabled' : smartSearchEnabled_list,
                  '#061deepLinkingEnabled' : deepLinkingEnabled_list,
                  '#062switch_search_suggestion_section' : switch_search_suggestion_section_list,
                  '#063savedSearchNotifEnabled' : savedSearchNotifEnabled_list,
                  '#064appsflyerEnabled' : appsflyerEnabled_list,
                  '#065boldSubscriptionEnabled' : boldSubscriptionEnabled_list,
                  '#065christmasModeEnabled' : christmasModeEnabled_list,
                  '#066imageSearchEnabled' : imageSearchEnabled_list,
                  '#067rewardifyEnabled' : rewardifyEnabled_list,
                  '#068valentinesDayEnabled' : valentinesDayEnabled_list,
                  '#069swapMyShopifyDomain' : swapMyShopifyDomain_list,
                  '#070agePopupEnabled' : agePopupEnabled_list,
                  '#071viaEnabled' : viaEnabled_list,
                  '#072quantityBreaksEnabled' : quantityBreaksEnabled_list,
                  '#073browserDeeplinkEnabled' : browserDeeplinkEnabled_list,
                  '#074multiCurrencyEnabled' : multiCurrencyEnabled_list,
                  '#075pullToRefreshEnabled' : pullToRefreshEnabled_list,
                  '#076related_products_enabled' : related_products_enabled_list,
                  '#077show_collection_description' : show_collection_description_list,
                  '#078shopifyEmiEnabled' : shopifyEmiEnabled_list,
                  '#079mobileSalesChannelEnabled' : mobileSalesChannelEnabled_list,
                  '#080accent_color' : accent_color_list,
                  '#081badge_color' :badge_color_list,
                  '#082badge_text_color' : badge_text_color_list,
                  '#083buy_button_color' : buy_button_color_list,
                  '#084option_value_color': option_value_color_list,
                  '#085primary_color' : primary_color_list,
                  '#086primary_color_dark' : primary_color_dark_list,
                  '#087share_button_color': share_button_color_list,
                  '#088splash_bg_color': splash_bg_color_list,
                  '#089splash_spinner_color':splash_spinner_color_list, 
                  '#090sub_collection_color':sub_collection_color_list,
                  '#091toolbar_color': toolbar_color_list,
                  '#092toolbar_content_color': toolbar_content_color_list,
                  '#093discount_color' :discount_color_list,
                  '#094vendor_color' : vendor_color_list,
                  '#095social_login': social_login_list,
                  '#096android_google_client_id' : android_google_client_id_list,
                  '#097google_client_id' : google_client_id_list,
                  '#098google_uri_scheme' : google_uri_scheme_list
                  
                  }

    
    df = pd.DataFrame.from_dict(output, orient='index')
    df = df.transpose()
    df = df.sort_index(axis=1)
    print(df)
    
    df.to_excel(xlsheet[i], sheet_name='storedata', index=False)
    del appid_list [:]
    del isactive_list [:]
    del bottom_bar_list [:]
    del isTrial_list [:]
    del custom_font_bold_list [:]
    del custom_font_regular_list [:]
    del currency_comma_enabled_list [:]
    del default_country_list [:]
    del default_language_list [:]
    del iso_currency_code_list [:]
    del logo_list [:]
    del name_list [:]
    del platform_list [:]
    del priceFormat_list [:]
    del priceSuffix_list [:]
    del storeUrl_list [:]
    del text_zipcode_enabled_list [:]
    del status_list [:]
    del abandonedCartEnabled_list [:]
    del autoApplyCouponEnabled_list [:]
    del backToStockAlertEnaled_list [:]
    del blogEnabled_list [:]
    del branchSDKEnabled_list [:]
    del brandPlaceholderEnabled_list [:]
    del cleverTapEnabled_list [:]
    del crossSellEnabled_list [:]
    del customProductOptionsEnabled_list [:]
    del customerChatEnabled_list [:]
    del deliveryAreaEnabled_list [:]
    del deliveryOptionsEnabled_list [:]
    del deliverySlotEnabled_list [:]
    del fbLoginEnabled_list [:]
    del firebaseAnalyticsEnabled_list [:]
    del flitsEnabled_list [:]
    del googleLoginEnabled_list [:]
    del guestCheckoutEnabled_list [:]
    del isForceUpdate_list [:]
    del shopifyMobileSalesChannelEnabled_list [:]
    del multiLanguageEnabled_list [:]
    del multiVendorCheckoutEnabled_list [:]
    del nativeCheckoutEnabled_list [:]
    del nativeCheckoutProcessEnabled_list [:]
    del new_cart_design_enabled_list [:]
    del postAffiliateProEnabled_list [:]
    del productGridWishlistEnabled_list [:]
    del productReviewsEnabled_list [:]
    del rateUsEnabled_list [:]
    del refreshCartEnabled_list [:]
    del reorderEnabled_list [:]
    del rewardEnabled_list [:]
    del shareCollectionEnabled_list [:]
    del sortFilterEnabled_list [:]
    del suggestionsEnabled_list [:]
    del deliveryRegionEnabled_list [:]
    del liveVideoEnabled_list [:]
    del orderNoteEnabled_list [:]
    del showLineItemCount_list [:]
    del webAppleGooglePayEnabled_list [:]
    del applePayEnabled_list [:]
    del smartSearchEnabled_list [:]
    del deepLinkingEnabled_list [:]
    del switch_search_suggestion_section_list [:]
    del savedSearchNotifEnabled_list [:]
    del appsflyerEnabled_list [:]
    del boldSubscriptionEnabled_list [:]
    del christmasModeEnabled_list [:]
    del imageSearchEnabled_list [:]
    del rewardifyEnabled_list [:]
    del valentinesDayEnabled_list [:]
    del swapMyShopifyDomain_list [:]
    del agePopupEnabled_list [:]
    del viaEnabled_list [:]
    del quantityBreaksEnabled_list [:]
    del browserDeeplinkEnabled_list [:]
    del multiCurrencyEnabled_list [:]
    del pullToRefreshEnabled_list [:]
    del related_products_enabled_list [:]
    del show_collection_description_list [:]
    del shopifyEmiEnabled_list [:]
    del mobileSalesChannelEnabled_list [:]
    del accent_color_list [:]
    del badge_color_list [:]
    del badge_text_color_list [:]
    del buy_button_color_list [:]
    del option_value_color_list [:]
    del primary_color_list [:]
    del primary_color_dark_list [:]
    del share_button_color_list [:]
    del splash_bg_color_list [:]
    del splash_spinner_color_list [:]
    del sub_collection_color_list [:]
    del toolbar_color_list [:]
    del toolbar_content_color_list [:]
    del discount_color_list [:]
    del vendor_color_list [:]
    del social_login_list [:]
    del android_google_client_id_list [:]
    del google_client_id_list [:]
    del google_uri_scheme_list[:]
        
    print("----------------------------------------------------------")
    
            
    
            


