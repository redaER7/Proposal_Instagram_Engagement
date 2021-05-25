# -*- coding: utf-8 -*-
#                               ﻢﻴﺣﺮﻟا ﻥﺎﻤﺣﺮﻟا ﻪﻠﻟا ﻢﺳﺎﺑ
#                       ﺮﻳﺪﻗ ءﻲﺷ ﻞﻛ ﻰﻠﻋ ﻮﻫ ﻭ ﻚﻠﻤﻟا ﻪﻟ ﻞﻛﻮﺘﻧ ﻪﻴﻠﻋ
#
#
from lib import*
#from func import*
##
##
print('     Phase 0 : AUTO TASKS')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
now = dt.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Started at :", current_time)
print('-----------------------------------------------------------------')
##
tmin=3
tmax=6
t1=6
t2=12
####################################################################################
df=pd.read_csv("credentials.txt","r",delimiter=',',header=None)
login=df.values[0][0]
passw=df.values[0][1]
####################################################################################
print('Initializing Profile...\n')
print('-----------------------------------------------------------------')
#SELENIUM ENTRIES
cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True
cap['acceptInsecureCerts'] = True
binary = FirefoxBinary('/usr/bin/firefox')
##
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
#options.add_argument('--load-images=no')
#options.add_argument("window-size=1400,600")
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--proxy-server=%s' % proxy)
##
profile = webdriver.FirefoxProfile()
#profile.set_preference("general.useragent.override", "[user-agent string]")
profile.set_preference("general.useragent.override", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
####################################################################################
#SELENIUM REQUESTS
url='https://www.instagram.com/'
#
driver = webdriver.Firefox(profile,options = options,capabilities=cap,firefox_binary=binary)
#
driver.get(url)
driver.set_page_load_timeout(np.random.randint(tmin,tmax))

if driver.title.startswith('Insta')==True:
	pass
##
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
#
username_input.send_keys(login)
password_input.send_keys(passw)
##
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
time.sleep(np.random.randint(t1,t2))
#
f = codecs.open("page_source.txt", "w", "utf−8")
h = driver.page_source
f.write(h)

not_now_button=driver.find_element_by_xpath("//button[normalize-space()='Not Now']")
not_now_button.click()
time.sleep(np.random.randint(t1,t2))
##
## LOOK FOR TAGS

url='https://www.instagram.com/markruffalo/'
driver.get(url)
#time.sleep(np.random.randint(t1,t2))

url='https://www.instagram.com/campuscoding/followers'
r=driver.find_element_by_xpath('//a[@href="/markruffalo/followers/"]')
r.click()
#driver.get(url)
####################################################################################
# GO TO USER PROFILE
first_user=driver.find_element_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
first_user.click()
####################################################################################
#FOLLOW USER
follow_button = driver.find_element_by_xpath("//button[@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
follow_button.click()
####################################################################################
#CLICK ON MESSAGE BUTTON
message_button = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
message_button.click()
not_now_button.click()
####################################################################################
##
#
#
#
#
#