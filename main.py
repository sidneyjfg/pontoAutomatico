import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import messagebox, Tk

codigo_empregador= ""
codigo_pin = 0
cpf_user = ""

def exibir_notificacao(horario):
    root = Tk()
    root.withdraw()  # Esconde a janela principal

    # Configura a janela de notificação para ser exibida no topo
    root.attributes('-topmost', True)

    # Exibe uma caixa de diálogo com a pergunta e o horário
    resposta = messagebox.askquestion("Executar Programa de Registro de Ponto",
                                      f"São {horario}. Deseja registrar o ponto agora?", parent=root)

    root.attributes('-topmost', False)  # Reseta a janela para não ser sempre a principal
    root.destroy()  # Destroi a janela root

    return resposta == 'yes'
def bater_ponto():
    """
    Função que simula o processo de bater ponto no Tangerino.

    Ajustes realizados:
    * Validação da existência do elemento antes de tentar interagir com ele.
    * Utilização de técnicas de espera para aguardar que o elemento esteja disponível.
    * Adição de comentários explicativos para melhorar a legibilidade do código.
    """

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Executa o navegador em segundo plano

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Abre o navegador e navega para o site do Tangerino
        driver.get("https://app.tangerino.com.br/Tangerino/pages/LoginPage/")
        print("Site acessado com sucesso!")

        # Espera até que o elemento da aba "RegistraPonto" seja clicável
        colaborador_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//ul[contains(@class, "login-abas")]//a[@class="login-aba" and text()="Registrar Ponto"]'))
        )
        colaborador_link.click()
        print("Aba 'Registrar Ponto' selecionada com sucesso.")

        # Espera até que o campo do código do empregador esteja presente e seja visível
        codigo_empregador_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="codigoEmpregador"]'))
        )
        codigo_empregador_input.send_keys(codigo_empregador)
        print("Código do Empregador inserido!")

        # Espera até que o campo do código PIN esteja presente e seja visível
        codigo_pin_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="codigoPin"]'))
        )
        codigo_pin_input.send_keys(codigo_pin)
        print("Código Pin inserido!")

        # Espera até que o botão "Registrar Ponto" esteja clicável
        registra_ponto_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="registraPonto"]'))
        )
        registra_ponto_button.click()
        print("Botão Registrar Ponto acionado")

        # Espera até que o campo CPF esteja presente e seja visível
        cpf_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//input[@id="cpf"]'))
        )
        if cpf_input.is_enabled:
            cpf_input.send_keys(cpf_user)
            print("CPF inserido!")
        else:
            time.sleep(13)
            button_continuar = driver.find_element(By.XPATH, '//button[contains(@class,"btn btn-primary w-full btnContinuar")]')
            button_continuar.click()
            print("Botão Continuar acionado")
            time.sleep(15)
        

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        driver.quit()
        print("Ponto registrado com sucesso")

def verificar_e_bater_ponto(horario):
    if exibir_notificacao(horario):
        bater_ponto()
    else:
        print(f"Registro de ponto não foi realizado para o horário {horario}.")

# Agendamento dos horários
schedule.every().day.at("08:00").do(verificar_e_bater_ponto, horario="08:00")
schedule.every().day.at("12:00").do(verificar_e_bater_ponto, horario="12:00")
schedule.every().day.at("13:20").do(verificar_e_bater_ponto, horario="13:20")
schedule.every().day.at("17:20").do(verificar_e_bater_ponto, horario="17:20")

# Loop principal para manter o script rodando e checar os agendamentos
while True:
    schedule.run_pending()
    time.sleep(1)
