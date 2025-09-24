import time
import requests
import random

def simular_indisponibilidade(url, tentativas=5, tempo_espera=2):
    """
    Simula indisponibilidade de rede ou serviço ao tentar fazer
    requisições para uma URL.

    Args:
        url (str): A URL do serviço a ser testado.
        tentativas (int): O número máximo de tentativas de conexão.
        tempo_espera (int): O tempo de espera entre as tentativas (em segundos).
    """
    for tentativa in range(1, tentativas + 1):
        print(f"Tentativa {tentativa} de {tentativas} para acessar: {url}")

        # Simula uma chance de falha aleatória para testar a resiliência
        if random.random() < 0.4:  # 40% de chance de falha
            print("Simulando falha de conexão...")
            time.sleep(tempo_espera)
            continue

        try:
            resposta = requests.get(url, timeout=5)
            # A linha abaixo vai gerar um erro caso o código de status seja >= 400
            resposta.raise_for_status()
            print(f"Sucesso! Serviço online. Status: {resposta.status_code}")
            return resposta
        except requests.exceptions.RequestException as e:
            print(f"Erro ao conectar: {e}")
            if tentativa < tentativas:
                print(f"Tentando novamente em {tempo_espera} segundos...")
                time.sleep(tempo_espera)
            else:
                print("Número máximo de tentativas alcançado. Falha na conexão.")
                return None

if __name__ == '__main__':
    # Exemplo de uso com uma URL de teste
    url_alvo = "https://www.youtube.com/"
    simular_indisponibilidade(url_alvo, tentativas=3, tempo_espera=3)