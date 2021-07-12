import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from urllib.parse import unquote
from selenium.webdriver.common.keys import Keys

starturl = "https://yandex.ru/"
driver = webdriver.Chrome(executable_path=".\chromedriver.exe")


def data_input(type_elment, element, send):
    """
    Очистка и Ввод строки
    :param type_elment:
    :param element: Элемент по которому искать
    :param send: текст
    :return:
    """
    try:
        search = driver.find_element(type_elment, element)
        search.clear()
        search.send_keys(send)
        return search
    except Exception as ex:
        return ex


def check_for_element_class_name(element, rez="0"):
    """
    Проверка существоания элемента на стр
    если не найдёт элемент вернёт пустое значение
    :param type_elment:
    :param element:
    :param rez: возращает обект при значении 0 при 1 возращает Boolean type
    :return:
    """
    try:
        chek = driver.find_elements_by_class_name(element)
    except NoSuchElementException:
        if (rez == '0'):return None
        else:return False
    if (rez == '0'):return chek
    else:return True

def delimiter(*text):
    print("-" * 30)
    print(*text)

def case_rez(boolean):
    if(boolean):return 'Есть'
    else:return 'Нет!'

def select_list(element,text_select):
    select = driver.find_elements_by_class_name(element)
    for item in select:
        if(item.text == text_select):
            item.click()
            return True
            break
        else:
            continue
        return False

def the_last_tab(browser):
    if (len(browser.window_handles) >= 2): browser.switch_to.window(browser.window_handles[len(browser.window_handles) - 1])

def read_get_request(driver):
    dict = {}
    list = unquote(str(driver.current_url)).split('?')[1].split('&')
    for i in list:
        key,value=i.split('=')
        #print(key,value)
        try:
            value = value.decode('utf-8')
            print(value)
        except Exception:
            value = value
        dict[key]=value
    return dict