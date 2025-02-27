#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

print("Here we go!")
#print('Enter email: ')
email = ''
#print('Enter pass: ')
passw = ''

global driver
driver = webdriver
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
chrome_options.add_argument('disable-infobars')
driver = driver.Chrome(options=chrome_options)
driver.implicitly_wait(5)
driver.maximize_window()
skipped = 0
dAr = {'وا':'waa','رَ':'ra','دَ':'da','وي':'wii','دا':'daa','زود':'zuud','زار':'zaar','داد':'daad','زَ':'za','وَ':'wa','زو':'zuu','راي':'raay','يَ':'ya','زي':'zii','زو':'zuu','دي':'dii','زا':'zaa','رو':'ruu','رود':'ruud','رَ':'ra','را':'raa','دور':'duur','ي':'ii','دو':'duu','دود':'duud','و':'uu','راو':'raaw','ا':'aa','وو':'wuu','ري':'rii'}
dJa = {'あ':'a', 'い':'i', 'う':'u', 'お':'o', 'か':'ka', 'く':'ku', 'さ':'sa', 'し':'shi', 'ち':'chi', 'に':'ni', 'は':'ha', 'よ':'yo', 'ん':'n', 'な':'na', 'ろ':'ro'}


#Begin 
driver.get("https://www.duolingo.com/log-in")
sleep(2)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[1]/div/input').send_keys(email)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/div[1]/label[2]/div/input').send_keys(passw)
driver.find_element_by_xpath('/html/body/div[5]/div/div/form/button').click()
sleep(5)

def x(xpath):
    return driver.find_element_by_xpath(xpath)

def skip():
    print('Skipping...')
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[1]/button').click()
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
    sleep(0.1) #was 0.5

def whichone(challenge):
    cw = re.findall('(\w+).\?', challenge)
    print('cw = ', cw)
    if cw:
        print('tryna crack')
    else:
        print('Could not find match with ', challenge, 'see whichone()')
        skip()


def url():
    #driver.get('https://www.duolingo.com/skill/ar/Alphabet1/practice')
    driver.get('https://www.duolingo.com/skill/ja/Hiragana-1/practice')
    x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button[2]').click()

def solve():
    challenge = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/h1/span').text
    print('\nNew challenge: ', challenge)
    try:
        if 'Match the pairs' in challenge:
            print('TYPE: Math the pairs')
            skip()
        elif 'Which one of these is' in challenge:
            try:
                print('whichone(challenge)?')
                whichone(challenge)
            except:
                skip()
        elif 'What sound does this make?' in challenge:
            challengeLetter = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/span').text
            print('Challenge is: ', challengeLetter)
            d = dJa #dAr?
            c = d.get(challengeLetter)
            print('For challenge', challenge, '\nAnswer should be: ', c)

            # Debug view, listing the challenge and some of the answers
            a1 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[1]/label/div[2]').text
            print('Answer1: ', a1)
            a2 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[2]/label/div[2]').text
            print('Answer2: ', a2)
            a3 = x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[3]/label/div[2]').text
            print('Answer3: ', a3)

            if c == a1:
                print('>>1')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[1]/label').click()
            elif c == a2:
                print('>>2')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[1]/label').click()
            elif c == a3:
                print('>>3')
                x('//*[@id="root"]/div/div/div/div/div[2]/div/div/div/div/div[2]/ul/li[1]/label').click()
            else:
                print('Challenge not found, letter: ', challengeLetter, ', Options', b1.text, b2.text, b3.text)
                skip()
            # Assuming correct answer is selected, check and move on
            # Check
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[3]/button').click()
            # Continue
            x('//*[@id="root"]/div/div/div/div/div[3]/div/div/div[4]/button').click()
            sleep(0.1) #works with 0.3
        else:
            print('Reached exception on main while\nNo answer set for challenge, skipping question. Challenge is: ', challenge)
            skip()
    except:
        print('\nNo more challenges detected, refreshing', challenge)
        return
    solve()

while True:
    url()
    solve()
