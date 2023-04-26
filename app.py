from datetime import datetime, timezone
from time import sleep

import psycopg2
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as condicao_esperada
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

conexao = psycopg2.connect(
    database='',
    user='',
    password='',
    host='',
    port=''
)

sql = conexao.cursor()


def novo_produto(sql, conexao, nome, preco, site, data_cotacao, link_imagem):
    query = "SELECT * FROM app_buscapreco_produto WHERE nome=%s and preco=%s and site=%s"
    valores = (nome, preco, site)
    resultado = sql.execute(query, valores)
    dados = sql.fetchall()

    if len(dados) == 0:
