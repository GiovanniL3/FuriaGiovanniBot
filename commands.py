from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import os, json, random

botToken: Final = '7272480776:AAHJ2QpwQWVIdaRGIO3-P4ixNrLc9fs_rwk'
botUsername: Final = '@FuriaGiovanniBot'

ranking_db = 'db.json'

#comandos

mensagemInicial = (
    "Segue a gente lá no insta: @furiagg\n\n📢 /noticias – Recebe as últimas notícias da FURIA direto no Telegram.\n\n"
    "📅 /agenda – Exibe os próximos jogos da Furia.\n\n"
    "🎯 /curiosidades – Curiosidades aleatórias sobre os jogadores, times e conquistas.\n\n"
    "🧠 /trivia – Minigame com perguntas sobre a história da FURIA, valendo pontos.\n\n"
    "🏆 /ranking – Mostra os top fãs do trivia ou interação com o bot.\n\n"
    "🛒 /loja – Link e novidades da loja oficial da FURIA.\n"
)

#start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{mensagemInicial}')

#lista
async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{mensagemInicial}')

#agenda
async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = f'OS proximos jogos da FURIA sempre estão no nosso do insta -> https://www.instagram.com/furiagg/' #procurar melhor uma fonte de agenda da furia como base de dados
    await update.message.reply_text(f'{news}')


#noticias
listaNews = {
        "curiosidade": "FURIA leva virada da Complexity e sofre primeira derrota na PGL Bucharest 2025",
        "fonte": "draft5.gg"
    }#procurar melhor uma fonte de noticias especificas da furia como base de dados
 
async def noticias(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(f'{listaNews["curiosidade"]} \n\n Fonte: {listaNews["fonte"]}')


#lojas
async def loja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Vista as cores dos furiosos e mostre seu apoio com estilo! Na loja oficial da FURIA, você encontra jerseys exclusivas, hoodies, acessórios e muito mais. Produtos de alta qualidade para quem vive o e-sports com paixão. \n\n 🛒 Acesse agora: furia.gg/produtos \n\n #GoFURIA')


#curiosidades
listaCuriosidades = [
    'Curiosidade - 1', 'Curiosidade - 2', 'Curiosidade - 4', 'Curiosidade - 5', 'Curiosidade - 6', 'Curiosidade - 7', 'Curiosidade - 8', 'Curiosidade - 9', 'Curiosidade - 10', 'Curiosidade - 11', 'Curiosidade - 12', 'Curiosidade - 21', 'Curiosidade - 13', 'Curiosidade - 14', 'Curiosidade - 15', 'Curiosidade - 16', 'Curiosidade - 17', 'Curiosidade - 18', 'Curiosidade - 19', 'Curiosidade - 20'
    ]

async def curiosidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    curiosidadeAleatoria = random.choice(listaCuriosidades)
    await update.message.reply_text(f'{curiosidadeAleatoria}')


#trivia
perguntas = [
    {
        "id": 1,
        "pergunta": "pergunta 1",
        "opcoes": ["opcao 1", "opcao 2", "opcao 3"],
        "correta": "opcao 2"
    },
    {
        "id": 2,
        "pergunta": "pergunta 2",
        "opcoes": ["opcao 1", "opcao 2", "opcao 3"],
        "correta": "opcao 3"
    },
    {
        "id": 3,
        "pergunta": "pergunta 3",
        "opcoes": ["opcao 1", "opcao 2", "opcao 3"],
        "correta": "opcao 1"
    },
    {
        "id": 4,
        "pergunta": "pergunta 4",
        "opcoes": ["opcao 1", "opcao 2", "opcao 3"],
        "correta": "opcao 3"
    },
    {
        "id": 5,
        "pergunta": "pergunta 5",
        "opcoes": ["opcao 1", "opcao 2", "opcao 3"],
        "correta": "opcao 3"
    }
]

async def trivia(update: Update, context: ContextTypes.DEFAULT_TYPE):

    pergunta = random.choice(perguntas)
    keyboard = [[InlineKeyboardButton(opcao, callback_data=opcao)] for opcao in pergunta["opcoes"]] #ao percorrer as opções, cria um botão para cada opção
    reply_markup = InlineKeyboardMarkup(keyboard) #aglomera tudo em um teclado

    context.user_data['resposta_certa'] = pergunta["correta"] #apresenta pra função qial a resposat é a correta e armazena na memoria do usuario(user_data)

    await update.message.reply_text(pergunta["pergunta"], reply_markup=reply_markup)

async def buttonTrivia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query #absorve o objeto, enviado pelo telegram, ao clicar no botão 
    
    await query.answer() #otimiza o clique do botão
    
    resposta = query.data #resposta escolhida
    correta = context.user_data.get('resposta_certa') #se comunica com(context.user_data['resposta_certa'] = pergunta["correta"])
    ranking = acessar_db(ranking_db)

    user_id = str(query.from_user.id)
    user_nome = query.from_user.first_name

    if resposta == correta:

        # Pontos locais
        context.user_data['pontos'] = context.user_data.get('pontos', 0) + 1

        # Atualizar ranking global
        if user_id in ranking:
            ranking[user_id]["pontos"] += 1 #soma um ponto ao q o usuario aj possui
        else:
            ranking[user_id] = {"nome": user_nome, "pontos": 1} #adiciona o usuario no ranking

        salvar_ranking(ranking)

        await query.edit_message_text(text=f"✅ Acertou!")
    else:
        await query.edit_message_text(text=f"❌ Errou! A resposta correta era: {correta}")




#comando
async def ranking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ranking = acessar_db(ranking_db)
    texto = "🏆 Ranking trivia FURIA:\n\n"

    # Organiza do maior para o menor
    ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True) #verificar funcionalide

    for posicao, (user_id, dados) in enumerate(ranking_ordenado, start=1): #verificar funcionalide
        nome = dados["nome"]
        pontos = dados["pontos"]
        texto += f"{posicao}º | {nome}.{user_id} : {pontos} pontos\n"

    await update.message.reply_text(texto)


#funcoes
def acessar_db(db): #acessar oa rquivo
    if os.path.exists(db):
        with open(db, 'r') as f:
            try:
                data = f.read().strip()
                if not data:
                    return {}  # arquivo está vazio
                return json.loads(data)
            except json.JSONDecodeError:
                return {}  # arquivo está malformado
    return {}

def salvar_ranking(ranking): #
    with open(ranking_db, 'w') as f:
        json.dump(ranking, f)
