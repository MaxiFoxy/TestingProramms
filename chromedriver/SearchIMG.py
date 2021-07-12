import time
import main
from main import delimiter
from main import case_rez
from main import select_list
prov = ['Ссылка «Картинки» присутствует на странице','Проверить, что перешли на url https://yandex.ru/images/ ','проверить что открылась, в поиске верный текст ', 'Открыть 1 картинку , проверить что открылась', 'Необходимо проверить, что переходе это то же изображение.']
rez = []
chek_url='https://yandex.ru/images/'

browser = main.driver

try:
    browser.get(url=main.starturl)

    browser.implicitly_wait(5)
    #rez.append(case_rez(main.check_for_element_class_name('search2__input', '1')))
    time.sleep(3)
    rez.append(case_rez(select_list('home-link','Картинки')))
    delimiter(prov[0],rez[0])
    time.sleep(4)
    main.the_last_tab(browser)
    rez.append(case_rez(str(browser.current_url).split('?')[0]==chek_url))
    delimiter(prov[1], rez[1])

    item = browser.find_elements_by_class_name('PopularRequestList-Item')
    item[0].click()
    save_obj = item[0].text
    browser.implicitly_wait(5)
    time.sleep(2)
    rez.append(case_rez(main.read_get_request(browser)['text']==save_obj))
    delimiter(prov[2], rez[2])

    time.sleep(5)
    img = browser.find_elements_by_class_name('serp-item__link')
    img[0].click()
    time.sleep(3)
    browser.implicitly_wait(5)

    button_next = browser.find_element_by_class_name('CircleButton_type_next')
    button_next.click()
    save_obj = browser.find_element_by_class_name('MMImage-Origin')
    time.sleep(1)
    button_prev = browser.find_element_by_class_name('CircleButton_type_prev')
    button_prev.click()
    rez.append(case_rez(browser.find_element_by_class_name('MMImage-Origin')==save_obj))
    delimiter(prov[3],rez[3])

    time.sleep(5)
    print(rez)
except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
