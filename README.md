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
