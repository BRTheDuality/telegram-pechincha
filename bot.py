from telegram import Bot
import schedule
import time
import random

# === CONFIGURAÇÕES ===
BOT_TOKEN = '8193359138:AAFkq61zpov1xygX7Q-iCuhsjEhe9axWHYE'
CHAT_ID = -1002727668932

# Lista de links de afiliado da Shopee (você pode adicionar mais)
LINKS_AFILIADOS = [
    "https://s.shopee.com.br/gF8pkKlOP"
]

bot = Bot(token=BOT_TOKEN)

def postar_oferta():
    link = random.choice(LINKS_AFILIADOS)
    titulo = "🔥 OFERTA IMPERDÍVEL NA SHOPEE!"
    msg = f"{titulo}\n\n🛒 Use o cupom e aproveite agora:\n👉 {link}"
    bot.send_message(chat_id=CHAT_ID, text=msg)

# Agendamento automático
schedule.every(1).hours.do(postar_oferta)

# Loop para manter o bot funcionando
while True:
    schedule.run_pending()
    time.sleep(1)
