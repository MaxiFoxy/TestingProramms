import time
import main
from main import delimiter
from main import case_rez
prov = ['Поле поиска','Подсказки', 'Ожидаемый результат поиска']
rez = []
rez_cout_url = 5

browser = main.driver


try:
    browser.get(url=main.starturl)
    browser.implicitly_wait(5)
    rez.append(case_rez(main.check_for_element_class_name('search2__input', '1')))
    delimiter(prov[0],rez[0])
    time.sleep(2)

    search = main.data_input('xpath', '//*[@id="text"]', 'тензор')

    #suggest = browser.find_elements_by_class_name('mini-suggest__item_type_fulltext')
    #for i in suggest:
    #   print(i.text)

    rez.append(case_rez(main.check_for_element_class_name('mini-suggest__item_type_fulltext',1)))
    delimiter(prov[1],rez[1])
    time.sleep(2)

    search.send_keys(main.Keys.ENTER)
    browser.implicitly_wait(5)
    rezult = browser.find_elements_by_xpath('//*[@id="search-result"]/li')
    colurl = 0

    for i in rezult:
        rez_url = i.find_element_by_class_name('Link').get_attribute('href')

        #print('tensor.ru' in str(rez_url))
        #print(str(rez_url))
        if('tensor.ru' in str(rez_url)): colurl += 1

    rez.append(case_rez(colurl >= rez_cout_url))
    delimiter(prov[2],rez[2],"|","Найдено",colurl,"из",rez_cout_url)
    delimiter()
    if(rez.count("Есть") == len(prov)): print("test : positive")
    else: print("test : negative")
    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
