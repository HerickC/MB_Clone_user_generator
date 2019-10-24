
import time
import random
import math
import string
from selenium import webdriver


def gera_random():
    return random.randrange(10)


def mod(dividendo, divisor):
    return round(dividendo % divisor)


def cpf():
    n1 = gera_random()
    n2 = gera_random()
    n3 = gera_random()
    n4 = gera_random()
    n5 = gera_random()
    n6 = gera_random()
    n7 = gera_random()
    n8 = gera_random()
    n9 = gera_random()

    a1 = n9 * 2
    a2 = n8 * 3
    a3 = n7 * 4
    a4 = n6 * 5
    a5 = n5 * 6
    a6 = n4 * 7
    a7 = n3 * 8
    a8 = n2 * 9
    a9 = n1 * 10

    d1 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
    d1 = 11 - mod(d1, 11)

    if d1 >= 10:
        d1 = 0

    a1 = d1 * 2
    a2 = n9 * 3
    a3 = n8 * 4
    a4 = n7 * 5
    a5 = n6 * 6
    a6 = n5 * 7
    a7 = n4 * 8
    a8 = n3 * 9
    a9 = n2 * 10
    a10 = n1 * 11

    d2 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
    d2 = 11 - mod(d2, 11)

    if d2 >= 10:
        d2 = 0

    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % \
        (n1, n2, n3,  n4, n5, n6,  n7, n8, n9,  d1, d2)


def randomString(stringLength=10, token=False):
    if(token):
        letters = string.digits
    else:
        letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


driver = webdriver.Chrome('./chromedriver')
for x in range(100):
    driver.get('https://mercadobitcoin.com.br.mbatendimento.com/login')
    driver.find_element_by_id('id_cpfcnpj').send_keys(cpf())
    driver.find_element_by_id('id_password').send_keys(
        randomString(random.randint(8, 15)))
    driver.find_element_by_id('hasTwoSteps').click()
    driver.find_element_by_id('senha').send_keys(randomString(6, True))
    driver.find_element_by_id('signup_button').click()
    print(x)
    time.sleep(3)
