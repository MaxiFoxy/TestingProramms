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
    delimiter()
    print(prov[0],rez[0])
    time.sleep(3)

    search = main.data_input('xpath', '//*[@id="text"]', 'тензор')
    delimiter()

    #suggest = browser.find_elements_by_class_name('mini-suggest__item_type_fulltext')
    #for i in suggest:
    #   print(i.text)

    rez.append(case_rez(main.check_for_element_class_name('mini-suggest__item_type_fulltext',1)))
    print(prov[1],rez[1])
    delimiter()
    time.sleep(5)

    search.send_keys(main.Keys.ENTER)
    browser.implicitly_wait(5)
    rezult = browser.find_elements_by_xpath('//*[@id="search-result"]/li')
    colurl = 0

    for i in rezult:
        rez_url = i.find_element_by_class_name('Link').get_attribute('href')

        print('tensor.ru' in str(rez_url))
        print(str(rez_url))
        if('tensor.ru' in str(rez_url)): colurl += 1

    #print(browser.page_source.encode('utf-8'))

    rez.append(case_rez(colurl >= rez_cout_url))
    print(prov[2],rez[2],"|","Найдено",colurl,"из",rez_cout_url)
    delimiter()

    if(rez.count("Есть") == len(prov)): print("positive : test")
    else: print("negative : test")
    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
