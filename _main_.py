
# BIBLIOTECAS \/
import time # responsavel pelo controle da função de sono do aplicativo
import schedule # responsavel pelo controle de agendamento da execução dos scripts
import csv # responsavel pelo controle de arquivos monitor_network
import ctypes # responsavel pelo controle de comandos com o teclado
import os # responsavel pela alteração e controle de diretórios
import subprocess # responsavel pela execução dos scripts
import psutil # responsavel pela identificação e controle de apps sendo executado
import logging # responsavel pela criação e manipulação do arquivo "zassit_log" de registro
from datetime import datetime # responsavel pelo controle da nomenclatura do arquivo log


# CONTROLE DE LOG \/
# variavel que define o padrão de nomenclatura do arq. log registrando sempre que INICIAR a data/tempo junto do nome p/ não repitir \/
log_assist = f'zassit_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
# função responsavel pela criação do arquivo log \/
logging.basicConfig(
    filename = log_assist, # defina o nome do arquivo de acordo com a variavel
    level = logging.INFO, # defina o nivel de informação em INFO
    filemode =  'w', # defina como modo escrita
    format = '%(asctime)s | %(levelname)s | %(message)s' # captura o data/tempo, o nome do nivel e a mensagem 
)

## FUNÇÔES \/
# função responsavel por executar o restart \/
def restart_app(name_bat):
    bat_filename = name_bat # pega o nome como referência para a busca
    road_script = os.path.dirname(os.path.abspath(__file__)) # coleta o caminho em que o .py se encontra
    road = os.path.join(road_script, bat_filename) # coleta o caminho pego do .py informando o nome do script desejado
    # EXECUTE normalmente \/
    try:
        result = subprocess.run(road, shell=True, check=True) # execute a variavel "road" como subprocesso win, validando seu caminho e sua execução, e adicione a variavel local "result"
        time.sleep(3) # ESPERE 3 segundos
        # ENVIAR tecla de função F11: \/
        ctypes.windll.user32.keybd_event(0x7A, 0, 0, 0)  # código da tecla F11
        ctypes.windll.user32.keybd_event(0x7A, 0, 0x0002, 0)  # liberação da tecla F11
        # SE o valor retornado pela variavel "result" FOR IGUAL a ZERO, FAÇA \/
        if result.returncode == 0:
            logging.info(f'EXECUTE {name_bat} <{result.returncode}>') # registre no log que foi executado e retorne o código
        # SE o valor retornado pela variavel "result" FOR DIFRENTE de ZERO, FAÇA \/
        if result.returncode != 0:
            logging.error(f'NOT EXECUTE {name_bat} <{result.returncode}>') # registre no log que não foi executado e retorne o código
    # CASO NÃO execute normamente e ERROR seja no caminho, FAÇA \/
    except subprocess.CalledProcessError as e:
       logging.error(f'NOT WHERE ROAD {name_bat} <{e.returncode}>') # registre no log que não foi executado e retorne o código que não foi encontrado o caminho
    # CASO ERROR seja outro, FAÇA \/
    except exec as ee:
        logging.error(f'NOT IDENTIFY {name_bat} <{ee.returncode}>') # registre no log que não foi executado e retorne o código que não identificou o erro
# função responsavel por executar o clear \/
def clear_routine(name_bat):
    bat_filename = name_bat # pega o nome como referência para a busca
    road_script = os.path.dirname(os.path.abspath(__file__)) # coleta o caminho em que o .py se encontra
    road = os.path.join(road_script, bat_filename) # coleta o caminho pego do .py informando o nome do script desejado
    # EXECUTE normalmente \/
    try:
        result = subprocess.run(road, shell=True, check=True) # execute a variavel "road" como subprocesso win, validando seu caminho e sua execução, e adicione a variavel local "result"
        # SE o valor retornado pela variavel "result" FOR IGUAL a ZERO, FAÇA \/
        if result.returncode == 0:
            logging.info(f'EXECUTE {name_bat} <{result.returncode}>') # informa no log mensagem de execução bem sucedida
        # SE NÃO o valor retornado pela variavel "result" FOR DIFRENTE de ZERO, FAÇA \/
        else:
            logging.error(f'NOT EXECUTE {name_bat} <{result.returncode}>') # informa no log o código de error capturado
    # CASO NÃO execute normamente e ERROR seja no caminho, FAÇA \/
    except subprocess.CalledProcessError as e:
       logging.error(f'NOT WHERE ROAD {name_bat} - Path issue <{e.returncode}>') # informa no log mensagem e código de error capturado pela exeção
    # CASO ERROR seja outro, FAÇA \/
    except Exception as ee:
        logging.error(f'NOT IDENTIFY {name_bat} - Unknown error <{str(ee)}>') # informa no log mensagem e código de error capturado pela exeção
# função responsavel por executar a checagem de aplicativo online \/
def monitor_app(app_name):
    app_running = False # retorna o valor verdadeiro na variavel de controle de verificação
    # PARA cada processo interado pela bibliotaca, pegue o pid e o nome, FAÇA: \/
    for process in psutil.process_iter(['pid', 'name']):
        # SE nome do processo for igual a nome do paramentro, FAÇA: \/
        if process.info['name'] == app_name:
            logging.info(f'CHECK ON {app_name} (PID: {process.info["pid"]})') # registre no log que foi executado e retorne o id de processo
            app_running = True # retorna o valor verdadeiro na variavel
            break # quebre o fluxo
    # SE NÃO for verdadeiro a variavel, FAÇA: \/
    if not app_running:
        logging.error(f'CHECK OFF {app_name}') # registre no log que app não está aberto e retorne o processo
        time.sleep(10) # ESPERE 10 segundos
        logging.info(f'RESTARTING {app_name}') # registre no log que app não está aberto, retornando o processo e que será reiniciado
        restart_app('restart.bat') # reinicie o app pelo script restart

            ### REALIZAR TRATAMENTO PARA TESTAR NOVAMENTE, SE CONDIÇÂO ATENDIDA, REINICAR PROGRAMA E RGISTRAR EM LOG   
# função responsavel por executar a checagem do assist online \/
def monitor_assist():
    logging.info('CHECK ON ASSIST') # informa no log a mensagem de checagem de aplicativo online
    return True # retorna o valor verdadeiro

## FUNÇÕES REDE \/
# função responsavel por executar e extrair os valores ping: \/
def ping_ms():
    # EXECUTE normalmente \/
    try:
        os.system("ping -c 1 fast.com > output_ping.txt") #
        # abra COM arquivo em mode leitura e FAÇA: \/
        with open("output_ping.txt", "r") as file:
            lines = file.readlines() # leia cada linha
        # PARA cada linha em linhas, FAÇA: \/
        for line in lines:
            # SE a frase "tempo=" estiver em linhas, FAÇA: \/
            if "tempo=" in line:
                # separe em cada linha que conter a frase "tempo=", os valores após o espaço e atribua a variavel: \/
                time_ms = line.split("tempo=")[-1].split(" ")[0].rstrip("ms")
                time_ms = int(time_ms)
                os.remove("output_ping.txt") # apague o arquivo
                return time_ms # retorne o valor atribuido a variavel
        return time_ms # retorne o valor atribuido a variavel
    # CASO NÃO execute normamente e ERROR qualquer, FAÇA \/
    except Exception as e:
        time_ms = 1000 # defina o valor da variavel para mil
        return time_ms # retorne a variavel
    # função controle responsavel por criar e regravar os dados no arquivo de registro p/ função "monitor_network": \/
def save_to_csv(data, filename='znetwork_monitor.csv'):
    # abra COM arquivo em modo de sobre escrita criando linha vazia, usando o parametro de nome para entrada e FAÇA: \/
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file) # escreva em arquivo a formatação csv
        writer.writerow(data) # escreva continuando em arquivo os dados continos na variavel com a formatação presqcrita
# função responsavel por extrair os valores de monitoramento e gravar em arquivo registro: \/
def monitor_network(app_name):
    # Título das colunas no CSV \/
    header = ['Timestamp', 'Download (Mb)', 'Upload (Mb)', 'Ping (Ms)\n']
    # Verifica se o arquivo CSV já existe \/
    # EXECUTE normalmente \/
    try:
        # abra COM arquivo em mode leitura e FAÇA: \/
        with open('znetwork_monitor.csv', 'r') as file:
            existing_data = list(csv.reader(file)) # abra o arquivo em .csv, leia cada valor das linha e associe a variavel (converta p/ lista)
    # CASO NÃO execute normamente e ERROR seja no arquivo não encontrado, FAÇA \/
    except FileNotFoundError:
        existing_data = [] # atribua lista vazia p/ a variavel
    # SE o arquivo não existir ou estiver vazio,FAÇA: \/
    if not existing_data:
        # abra COM arquivo em modo escrita, podo nova linha vazia e FAÇA: \/
        with open('znetwork_monitor.csv', 'w', newline='') as file:
            writer = csv.writer(file) # abra o arquivo em .csv, ecreva na linha vazia e associe a variavel
            writer.writerow(header) # escreva cabeçalho na primeira linha do arquivo
    # ENQUANTO for VERDADE que programa roda, FAÇA: \/
    while True:
        network_stats = psutil.net_io_counters() # extrai conteines da propria biblioteca p/ usar de referencia de servidor
        download = round(network_stats.bytes_recv/(1024**2), 2) # utiliza da variavel de "servidor" p/ descarregar arquivos e retornar valores da velocidade de down (formatando p/ mega)
        upload = round(network_stats.bytes_sent/(1024**2), 2) # utiliza da variavel de "servidor" p/ enviar arquivos e retornar valores da velocidade de up (formatando p/ mega)
        ping = ping_ms() # chama a funçã e associa a variavel
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Obtém a data e hora atual
        data = [timestamp, download, upload, ping] # salva os dados em uma lista
        save_to_csv(data) # salva os dados no arquivo CSV
        # SE ping for menor que 70, FAÇA: \/
        if ping < 70:
            logging.info(f'CHECK OK NETWORK (Ping: {ping})') # registre no log que a rede está boa e retorne o valor do ping
            return True # retorna o valor verdadeiro
        # SE NAO, mas SE ping for igual a 1000, FAÇA: \/
        elif ping == 1000:
            logging.error(f'CHECK DISCONNECTED NETWORK (Ping: {ping})') # registre no log que a rede está desconectada e retorne o valor do ping
            time.sleep(10) # ESPERE 10 segundos
            logging.info(f'RESTARTING {app_name}') # registre no log que o processo de renicialização do app será executado
            restart_app('restart.bat') # reinicie o app pelo script restart
        # SE NAO, mas SE ping for maior que 200, FAÇA: \/
        elif ping >= 200 < 1000:
            logging.error(f'CHECK VERY BAD NETWORK (Ping: {ping})') # registre no log que a rede está péssima e retorne o valor do ping
            ### ADD TRATAMENTO DE ENVIO DE MENSAGEM A SUPORTE
            return True # retorna o valor verdadeiro
        # SE NAO, mas SE ping for maior que 70, FAÇA: \/
        elif ping >= 70 < 200:
            logging.error(f'CHECK BAD NETWORK (Ping: {ping})') # registre no log que a rede está ruim e retorne o valor do ping
            # execute rotinas de limpeza de tcp, udp e dns: \/
            time.sleep(10) # ESPERE 10 segundos
            logging.info(f'CLENING NETWORK') # registre no log que o processo de limpeza de rede será executado
            subprocess.run(["ipconfig", "/renew"], check=True) # execute o comando cmd pedido, validando a execução (limpa cache tcp e udp renovando a configuração do adaptador de rede)
            subprocess.run(["ipconfig", "/flushdns"], check=True) # execute o comando cmd pedido, validando a execução (limpa cache dns)
            return True # retorna o valor verdadeiro

# FUNÇÃO EXECUÇÃO \/
# função responsavel pelo controle do agendamento de cada função_rotina \/
def time_out():
    restart_app('restart.bat') # executa função ao iniciar app (reciclando para uma inicialização)
    schedule.every().day.at("09:50").do(lambda: restart_app('restart.bat')) # executa a função todos os dias ás 09:50h
    schedule.every().wednesday.at("09:30").do(lambda: clear_routine('clear.bat')) # executa a função todas as quartas ás 09:30h
    schedule.every().hour.do(monitor_assist) # executa a função a cada hora
    schedule.every(10).minutes.do(lambda: monitor_app('appname.exe')) # executa a função a cada hora, pegando a tarefa indicada como parametro da função interna
    schedule.every(10).minutes.do(lambda: monitor_network('appname.exe')) # executa a função a cada hora, realizando ações caso nescessario

    return True # retorna o valor verdadeiro

# EXECUÇÃO \/
# SE nome do arquivo FOR IGUAL ao arquivo principal, FAÇA \/
if __name__ == "__main__":
    logging.info('Ass.: Leonardo Rodrigues') # ao iniciar o aplicativo assina no log o app
    logging.info('START') # ao iniciar o aplicativo registra no log o ponto de inicio
    time_out() # chama a função de agendamento das rotinas para execução
    print('RUN')
    # ENQUANTO FOR verdadade o app ON, FAÇA \/    
    while True:
        # EXECUTE normalmente: \/
        try:
            schedule.run_pending() # execute a biblioteca schedule, realizando a checagem
            time.sleep(1) # espere 1 segundo para cada checagem
        # CASO NÃO execute normamente e ERROR seja na entrada do teclado, FAÇA \/
        except KeyboardInterrupt:
            break  # encerre o loop se o usuário pressionar Ctrl+C
        # CASO NÃO execute normamente e ERROR seja qualquer, FAÇA \/
        except Exception as e:
            print(f"Erro: {e}") # mostre o error capturado