from splinter.browser import Browser
from twilio.rest import TwilioRestClient # for sending a SMS to the phone
import time

b = Browser()
acked = []
tex = []

b.driver.maximize_window()

#b.visit('http://test.service-now.com') # for test site
b.visit('http://test.service-now.com')

with b.get_iframe('gsft_main') as ifr:
    ifr.fill('user_name','your_login')
    ifr.fill('user_password','your_pwd') # fill your own login and pwd
    
    # "not_important" is the name for login button they have assigned
    # can you believe it :)
    ifr.find_by_name('not_important').first.click()
    
time.sleep(10) #for page loading

while True:
    b.reload() #refreshes the whole browser tab.
    time.sleep(5)
    
    with b.get_iframe('gsft_main') as iFrame:
        f = iFrame.find_link_by_partial_text('INC')
        for one in f:
            tex.append(one['text']) #this turns webdriver elements into text links.
        tmp = tex.copy()
        
        
        for i in tmp:
        
            if i not in acked: #this checks for already acknowledged incidents.
                iFrame.click_link_by_text(i)
                time.sleep(5) #incident loading.
                
                if iFrame.find_option_by_text('Waiting').first.selected:
                    acked.append(i)
                    iFrame.find_by_id('sysverb_update').first.click()
                    time.sleep(10)
                else:
                    iFrame.find_option_by_text('Acknowledged').first.click()
                    iFrame.fill('sys_display.incident.assigned_to','Your_name')
                    time.sleep(1)
                    iFrame.find_by_id('incident.comments').first.click() #this is to bypass the 'data not filled' exception
                    time.sleep(1)
                    iFrame.find_by_id('sysverb_update').first.click()
                    acked.append(i)
                    
                    # the sms part...this is just to know an incident has been acknowledged
                    # you can get your accound_sid and auth_token from your twilio account
                    
                    account_sid = "your_sid_here"
                    auth_token  = "your_auth_token_here"
                    client = TwilioRestClient(account_sid, auth_token)
                    message = client.messages.create(body = "your_message" ,
                                               	to = "your_mobile_no",
                                               	from_ = "your_twilio_no")
                                                
                    time.sleep(10)   #choose the time limit after which you want to refresh
        tex.clear()
