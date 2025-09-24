Script Python simples para testar resiliência de aplicações simulando indisponibilidade de rede/serviço ao fazer requisições HTTP. Útil para validar lógica de retry, timeouts e tratamento de exceções em integrações com serviços externos.

O que faz

O script tenta acessar uma URL configurada várias vezes (tentativas) com um intervalo (tempo_espera) entre tentativas. Em cada tentativa há uma chance aleatória de simular uma falha (útil para testar comportamento em condições instáveis). Caso a requisição HTTP falhe (timeout, status >= 400 ou erro de conexão), o script realiza novas tentativas até o limite definido.
