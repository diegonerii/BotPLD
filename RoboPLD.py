from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


# driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

# driver.set_window_size(1024, 600)
# driver.maximize_window()
driver.get(
    'https://www.ccee.org.br/portal/faces/pages_publico/o-que-fazemos/como_ccee_atua/precos/preco_horario?_afrLoop'
    '=131575298728896&_adf.ctrl-state=70mm2vyzk_54#!%40%40%3F_afrLoop%3D131575298728896%26_adf.ctrl-state'
    '%3D70mm2vyzk_58')

time.sleep(5)

lista_horas = []
lista_pld_atual_se, lista_pld_atual_s, lista_pld_atual_ne, lista_pld_atual_n = [], [], [], []
lista_pld_min_se, lista_pld_min_s, lista_pld_min_ne, lista_pld_min_n = [], [], [], []
lista_pld_hora_min_se, lista_pld_hora_min_s, lista_pld_hora_min_ne, lista_pld_hora_min_n = [], [], [], []
lista_pld_med_se, lista_pld_med_s, lista_pld_med_ne, lista_pld_med_n = [], [], [], []
lista_pld_max_se, lista_pld_max_s, lista_pld_max_ne, lista_pld_max_n = [], [], [], []
lista_pld_hora_max_se, lista_pld_hora_max_s, lista_pld_hora_max_ne, lista_pld_hora_max_n = [], [], [], []
write_tweet_se, write_tweet_s, write_tweet_ne, write_tweet_n = [], [], [], []


def write_tweet(lista):
    write_tweet = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[' \
                  '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[' \
                  '2]/div/div/div/div '
    tweet = driver.find_element_by_xpath(write_tweet)
    tweet.click()
    time.sleep(10)
    lista.append(tweet)


def send_tweet():
    send_tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[' \
                       '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div '
    send_tweet = driver.find_element_by_xpath(send_tweet_xpath)
    send_tweet.click()

    time.sleep(10)


def captura_informacoes(atual, minimo, hr_min, medio, maximo, hr_max):
    preco_atual = driver.find_element_by_xpath('//*[@id="precoAtual"]').text
    atual.append(preco_atual)

    preco_minimo = driver.find_element_by_xpath('//*[@id="precoMin"]').text
    minimo.append(preco_minimo)

    hora_minima = driver.find_element_by_xpath('//*[@id="horaPatamarTabela"]/ul/li[2]/span[2]').text
    hr_min.append(hora_minima)

    preco_medio = driver.find_element_by_xpath('//*[@id="precoMed"]').text
    medio.append(preco_medio)

    preco_maximo = driver.find_element_by_xpath('//*[@id="precoMax"]').text
    maximo.append(preco_maximo)

    hora_maxima = driver.find_element_by_xpath('//*[@id="horaPatamarTabela"]/ul/li[4]/span[2]').text
    hr_max.append(hora_maxima)

    print(atual, minimo, hr_min, medio, maximo, hr_max)

while True:
    hoje = datetime.today().strftime('%d/%m/%Y')
    driver.get(
        'https://www.ccee.org.br/portal/faces/pages_publico/o-que-fazemos/como_ccee_atua/precos/preco_horario?_afrLoop'
        '=131575298728896&_adf.ctrl-state=70mm2vyzk_54#!%40%40%3F_afrLoop%3D131575298728896%26_adf.ctrl-state'
        '%3D70mm2vyzk_58')

    time.sleep(10)

    hora = driver.find_element_by_xpath('//*[@id="horaAtual"]').text
    lista_horas.append(hora)

    captura_informacoes(lista_pld_atual_se, lista_pld_min_se, lista_pld_hora_min_se,
                        lista_pld_med_se, lista_pld_max_se, lista_pld_hora_max_se)

    driver.find_element_by_xpath('//*[@id="SUL"]/a').click()
    time.sleep(10)

    captura_informacoes(lista_pld_atual_s, lista_pld_min_s, lista_pld_hora_min_s,
                        lista_pld_med_s, lista_pld_max_s, lista_pld_hora_max_s)

    driver.find_element_by_xpath('//*[@id="NORDESTE"]/a').click()
    time.sleep(10)

    captura_informacoes(lista_pld_atual_ne, lista_pld_min_ne, lista_pld_hora_min_ne,
                        lista_pld_med_ne, lista_pld_max_ne, lista_pld_hora_max_ne)

    driver.find_element_by_xpath('//*[@id="NORTE"]/a').click()
    time.sleep(10)

    captura_informacoes(lista_pld_atual_n, lista_pld_min_n, lista_pld_hora_min_n,
                        lista_pld_med_n, lista_pld_max_n, lista_pld_hora_max_n)

    ###### TWITTER ######

    driver.get('https://twitter.com/login')
    time.sleep(10)
    try:
        driver.find_element_by_name('session[username_or_email]').send_keys("protecaoeaterramento@gmail.com")
        driver.find_element_by_name("session[password]").send_keys("deusdeus" + Keys.RETURN)
        print("Entrou com o e-mail")
        time.sleep(10)

    except:
        pass
        """driver.find_element_by_name('session[username_or_email]').send_keys("PldHorario")
        driver.find_element_by_name("session[password]").send_keys("deusdeus" + Keys.RETURN)
        print("Entrou com o login")
        time.sleep(10)"""

    try:
      autenticacao = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
      autenticacao.send_keys('PldHorario')
      senha = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
      senha.send_keys('deusdeus' + Keys.RETURN)
      print("Entrou com o número do @")
      time.sleep(10)
    except:
        pass

    write_tweet(write_tweet_se)
    try:
        write_tweet_se[0].send_keys(
            "PLD Horário \nData: {}\nHora: {}\n\nSE/CO\n\nAtual: {} R$/MWh\nMínimo: {} R$/MWh\nHora Mínimo: {}"
            "\nMédio: {} R$/MWh\nMáximo: {} R$/MWh\nHora Máximo: {}"
                .format(hoje, lista_horas[-1], lista_pld_atual_se[-1], lista_pld_min_se[-1],
                        lista_pld_hora_min_se[-1][:5], lista_pld_med_se[-1], lista_pld_max_se[-1],
                        lista_pld_hora_max_se[-1][:5]))
        time.sleep(60)
        send_tweet()

        write_tweet(write_tweet_s)
        write_tweet_s[0].send_keys(
            "PLD Horário \nData: {}\nHora: {}\n\nSul\n\nAtual: {} R$/MWh\nMínimo: {} R$/MWh\nHora Mínimo: {}"
            "\nMédio: {} R$/MWh\nMáximo: {} R$/MWh\nHora Máximo: {}"
                .format(hoje, lista_horas[-1], lista_pld_atual_s[-1], lista_pld_min_s[-1],
                        lista_pld_hora_min_s[-1][:5], lista_pld_med_s[-1], lista_pld_max_s[-1],
                        lista_pld_hora_max_s[-1][:5]))

        time.sleep(60)
        send_tweet()

        write_tweet(write_tweet_ne)
        write_tweet_ne[0].send_keys(
            "PLD Horário \nData: {}\nHora: {}\n\nNordeste\n\nAtual: {} R$/MWh\nMínimo: {} R$/MWh\nHora Mínimo: {}"
            "\nMédio: {} R$/MWh\nMáximo: {} R$/MWh\nHora Máximo: {}"
                .format(hoje, lista_horas[-1], lista_pld_atual_ne[-1], lista_pld_min_ne[-1],
                        lista_pld_hora_min_ne[-1][:5], lista_pld_med_ne[-1], lista_pld_max_ne[-1],
                        lista_pld_hora_max_ne[-1][:5]))

        time.sleep(60)
        send_tweet()

        write_tweet(write_tweet_n)
        write_tweet_n[0].send_keys(
            "PLD Horário \nData: {}\nHora: {}\n\nNorte\n\nAtual: {} R$/MWh\nMínimo: {} R$/MWh\nHora Mínimo: {}"
            "\nMédio: {} R$/MWh\nMáximo: {} R$/MWh\nHora Máximo: {}"
                .format(hoje, lista_horas[-1], lista_pld_atual_n[-1], lista_pld_min_n[-1],
                        lista_pld_hora_min_n[-1][:5], lista_pld_med_n[-1], lista_pld_max_n[-1],
                        lista_pld_hora_max_n[-1][:5]))

        time.sleep(60)
        send_tweet()

        driver.close()

    except:
        pass
        print("DEU ERRO")
    print("ESTOU VIVO")
    time.sleep(3600)
