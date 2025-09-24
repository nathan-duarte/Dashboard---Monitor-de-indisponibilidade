Script Python simples para testar resiliência de aplicações simulando indisponibilidade de rede/serviço ao fazer requisições HTTP. Útil para validar lógica de retry, timeouts e tratamento de exceções em integrações com serviços externos.

O que faz

O script tenta acessar uma URL configurada várias vezes (tentativas) com um intervalo (tempo_espera) entre tentativas. Em cada tentativa há uma chance aleatória de simular uma falha (útil para testar comportamento em condições instáveis). Caso a requisição HTTP falhe (timeout, status >= 400 ou erro de conexão), o script realiza novas tentativas até o limite definido.

Recursos / Benefícios

Simula falhas intermitentes (chance configurável no código).

Implementa retry com timeout e tratamento de exceções usando requests.

Saída em console com informações de tentativa, sucesso e falha.

Fácil de adaptar para testes locais, automação ou integração com scripts maiores.

Requisitos

Python 3.7+

Biblioteca requests

Instalação rápida:

pip install requests

Uso

Exemplo de execução (arquivo principal já contém um if __name__ == '__main__'):

python simular_indisponibilidade.py


No código, você pode ajustar:

url_alvo — URL a ser testada.

tentativas — número máximo de tentativas (ex.: 3).

tempo_espera — segundos de espera entre tentativas (ex.: 3).

API / Parâmetros da função

simular_indisponibilidade(url, tentativas=5, tempo_espera=2)

url (str): URL do serviço a ser testado.

tentativas (int): quantidade máxima de tentativas (padrão 5).

tempo_espera (int): tempo de espera entre tentativas em segundos (padrão 2).

Retorna o objeto Response do requests em caso de sucesso, ou None se todas as tentativas falharem.

Exemplo
from simular_indisponibilidade import simular_indisponibilidade

resposta = simular_indisponibilidade("https://www.example.com", tentativas=3, tempo_espera=2)
if resposta:
    print("Conteúdo:", resposta.text[:200])
else:
    print("Falha ao conectar após as tentativas.")

Sugestões de melhoria

Tornar a taxa de falha (atualmente 0.4) um parâmetro da função para maior controle.

Adicionar logging ao invés de print para integração com sistemas de observabilidade.

Implementar backoff exponencial entre tentativas.

Converter em CLI com argparse para facilitar testes automatizados.

Licença

MIT — sinta-se livre para adaptar e usar conforme necessário.
