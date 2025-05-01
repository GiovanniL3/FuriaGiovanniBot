🤖 FuriaGiovanniBot

Um bot do Telegram feito em Python para fãs da FURIA Esports, com funcionalidades como notícias, curiosidades, minigame trivia e ranking dos usuários mais engajados. Projeto didático para treinar funções de chatbot do Telaram e Peyton em geral.

🚀 Funcionalidades

    /start – Mensagem de boas-vindas e lista de comandos.

    /lista – Exibe novamente a lista de comandos disponíveis.

    /noticias – Últimas notícias da FURIA.

    /agenda – Agenda dos próximos jogos (link para Instagram oficial).

    /curiosidades – Mostra curiosidades aleatórias sobre o time.

    /trivia – Minigame de perguntas e respostas sobre a FURIA.

    /ranking – Ranking atualizado dos usuários mais ativos no trivia.

    /loja – Link para a loja oficial da FURIA.


🛠️ Como rodar

    Clone o repositório:

git clone https://github.com/GiovanniL3/FuriaGiovanniBot.git
cd FuriaGiovanniBot

    Instale as dependências:

pip install -r requirements.txt

    Configure o token do bot:

No arquivo bot.py, substitua a variável botToken pelo token do seu bot criado no BotFather:

botToken = 'SEU_TOKEN_AQUI'

    Execute o bot:

python bot.py

🗂️ Estrutura do projeto

FuriaGiovanniBot/
├── bot.py            # Configuração e inicialização do bot.
├── commands.py       # Todos os comandos
├── db.json           # Arquivo de banco de dados para ranking.
├── requirements.txt  # Dependências do projeto.
└── README.md         

🚩 Feito com ❤️ por Giovanni Luigi Fasciana Machado.
