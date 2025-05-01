#t.me/FuriaGiovanniBot
#Chave da API: 7272480776:AAHJ2QpwQWVIdaRGIO3-P4ixNrLc9fs_rwk
#pip install python-telegram-bot
#fontes: https://www.youtube.com/watch?v=vZtm1wuA2yc&t=848s, 
#enventual possivel hospedagem: https://www.youtube.com/watch?v=2TI-tCVhe9k

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ApplicationBuilder,CallbackQueryHandler

from commands import (
    start, lista, noticias, loja, agenda, curiosidades, trivia, buttonTrivia, ranking
)

botToken: Final = '7272480776:AAHJ2QpwQWVIdaRGIO3-P4ixNrLc9fs_rwk'
botUsername: Final = '@FuriaGiovanniBot'

ranking_db = 'db.json'

#----------------------------------------

#handlers

def handle_response(text: str) -> str:
    texto: str = text.lower()

    if 'oi' in texto:
        return 'oi'
    
    return 'resposta invalida'
 


async def handle_messge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type #informa se estamos me um grupo ou me um chat privado, ele tem diferentes cmportamentos nesses 2 casos
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')#recupera o id do usuario usando o chat, debug

    if message_type == 'group':
        if botUsername in text: #em grupos o bot so vai responder se o nome dlee estiver na menssagem
            newText: str = text.replace(botUsername, '').strip()
            response: str = handle_response(newText)
        else: 
            return
    else:
        response: str = handle_response(text)

    print('Bot', response) #resposta, debug
    await update.message.reply_text(response)

async def erro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caousou erro {context.error}')

if __name__ == '__main__':
    print('Bot iniciado!')
    app = Application.builder().token(botToken).build()

    #commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('lista', lista))
    app.add_handler(CommandHandler('noticias', noticias))
    app.add_handler(CommandHandler('loja', loja))
    app.add_handler(CommandHandler('agenda', agenda))
    app.add_handler(CommandHandler('curiosidades',curiosidades ))
    app.add_handler(CommandHandler('trivia', trivia))
    app.add_handler(CommandHandler('ranking', ranking))
    app.add_handler(CallbackQueryHandler(buttonTrivia))


    #menssagens
    app.add_handler(MessageHandler(filters.TEXT, handle_messge))

    #erros 
    app.add_error_handler(erro)

    #verificando se há novas menssagens
    #print('polling')
    app.run_polling(poll_interval=2)

    




