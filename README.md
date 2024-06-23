# Projeto: Automação de Ponto no Tangerino
## Descrição
Este projeto visa automatizar o processo de batimento de ponto no sistema Tangerino, utilizando Python e diversas bibliotecas. A automação é realizada através do agendamento de tarefas que executam ações no navegador, simulando o batimento de ponto pelo funcionário. Além disso, o sistema notifica o usuário sobre o status do batimento de ponto.

## Funcionalidades
- **Automação do Batimento de Ponto**: Utilização do Selenium para automatizar o login e o registro de ponto no Tangerino.
- **Agendamento de Tarefas**: Uso da biblioteca schedule para agendar automaticamente os horários de batimento de ponto.
- **Notificações**: Utilização do Tkinter para exibir notificações sobre o status do batimento de ponto.
- **Configuração Dinâmica**: Permite a configuração dos horários de entrada e saída.
## Tecnologias Utilizadas
* Linguagem de Programação:

    * Python
* Bibliotecas e Ferramentas:

    * schedule (para agendamento de tarefas)
    * selenium (para automação do navegador)
    * webdriver_manager (para gerenciamento do WebDriver)
    * tkinter (para exibição de notificações)
    * time (para manipulação de horários e espera)
## Estrutura do Projeto
``` bash
/automacao-ponto-tangerino
│
├── main.py                    # Script principal para automação do batimento de ponto
├── requirements.txt           # Arquivo de requisitos com as dependências do projeto
└── README.md                  # Documentação do projeto
└── .gitignore                 # Arquivo .gitignore
```

# Instalação e Configuração
1. Clonar o Repositório:
``` bash
git clone https://github.com/seu-usuario/automacao-ponto-tangerino.git
cd automacao-ponto-tangerino
```
2. Criar e ativar um ambiente Virtual caso julgue necessário
``` bash
python -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
```
3. Instalar dependências
``` bash
pip install -r requirements.txt
```
4. Configurar Variáveis de Ambiente (Opcional):
    * Configure variáveis de ambiente se necessário.
5. Alterar variáveis conforme seu uso
    * codigo_empregador
    * codigo_pin
6. Executar o Script:

``` bash
python main.py
```

# Contribuição
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (git checkout -b feature/sua-feature)
3. Commit suas mudanças (git commit -m 'Adiciona nova feature')
4. Faça um Push para a Branch (git push origin feature/sua-feature)
5. Abra um Pull Request