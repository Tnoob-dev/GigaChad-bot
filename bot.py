#Modules
import os
from pyrogram import Client, filters
import pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio
import tgcrypto
import yt_dlp
from yarl import URL
import pyshorteners
import qrcode
from config import Config
import speedtest

from config import Config

#Client
GigaChad = Client(
    "GigaChad",
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    bot_token = Config.BOT_TOKEN
)


@GigaChad.on_message(filters.command("start") & ~filters.edited)
async def Start(filters, message):
    print(f"🤖The Bot was started by: {message.from_user.id}\n{message.from_user.username}\n") #In Spanish: "El bot ha sido comenzado por: "
    await message.reply_photo("https://telegra.ph/file/90aa09730e63d35357221.png")
    await message.reply_text(f"🙃User: {message.from_user.mention}\n🆔ID: {message.from_user.id}\n📛Username: @{message.from_user.username}\n\nHola Humano, Soy un **Bot que sube archivos a Telegram, genera codigos QR y acorta enlaces**, puedo subir archivos directos desde varios sitios(Ejemplos: Uptodown.com, Malavida.com, Youtube.com, facebook.com,etc..., en proximas actualizaciones podras descargar desde MEGA, y vendran mas cosas increibles), Aqui puedes ver mas info acerca de mi creador😁👇",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("👾Github👾", url="https://www.github.com/Tnoob-dev"),
        InlineKeyboardButton("🔝Repo🔝", url="https://github.com/Tnoob-dev/GigaChad-bot"),
        InlineKeyboardButton("🐦Twitter🐦", url="https://twitter.com/TitiLM30")
    ],
    [InlineKeyboardButton("⌨️Canal interesante⌨️", url="https://t.me/s3softwareyprogramacion"),

     InlineKeyboardButton("💻Grupo adjunto💻", url="https://t.me/S3SPGrupo")
    ],
    [InlineKeyboardButton("🇬🇧Text in English🇬🇧", callback_data='ingles_start')]
    ]
    
    )
    )
    await message.reply_text("**🇬🇧Note: Send /help to know what i can do\n\n🇪🇸Nota: Envia /help para conocer que puedo hacer**")

@GigaChad.on_callback_query(filters.regex('ingles_start'))
async def start_query(client, callback_query):
    await callback_query.answer()
    await callback_query.message.edit_text("Hi Human, I'm a **Uploader to Telegram bot, i can generate QR Codes too, and short URLs**, i can upload files from some sites(Example: Uptodown.com, Malavida.com, Youtube.com, facebook.com,etc..., in other actualizations will come MEGA, and other amazing things), Here you can see more info about my Creator😁👇")



@GigaChad.on_message(filters.command("help") & ~filters.edited)
async def ayuda(filters, message):
    await message.reply_photo("https://telegra.ph/file/86a8426af71ef4f7eeec8.png")
    await message.reply_text("Envia /download y luego el link de descarga, lo descargare y luego te enviare el archivo\n\nEnvia /qr y luego un texto, y te generare un codigo QR con el texto dentro\n\nEnvia /short y luego un link y te enviare un link acortado con el link que enviaste\n\nEnvia /speedtest para hacer un pequeño Test de rapidez y ver la velocidad de Bajada/subida\n\n**Nota**: Si envias un enlace y el bot no lo reconoce, puedes enviar el enlace a @DirectLinkGeneratorbot, @DirectLinkGen_bot o @MaxFile2LinkBot.", 
    
    reply_markup= InlineKeyboardMarkup([[

        InlineKeyboardButton("🇬🇧Text in English🇬🇧", callback_data='ingles_help'),
    ]]
    )
    )

@GigaChad.on_callback_query(filters.regex('ingles_help'))
async def help_query(client, callback_query):
    await callback_query.answer()
    await callback_query.message.edit_text("Send /download and later send me the link, i will Download it and send you the file\n\nSend /qr and later a text and i will generate you a QR Code with the text\n\nSend \speedtest to do a quickly speedtest and watch the speed of Download/Upload\n\nSend /short and later send a link and i will short it\n\nNote: If you want to upload some other things and the bot don't recongnize him, you can go to @DirectLinkGeneratorbot, @DirectLinkGen_bot or @MaxFile2LinkBot.")


@GigaChad.on_callback_query(filters.regex('close'))
async def help_query(client, callback_query):
    await callback_query.answer()
    await callback_query.message.delete()


Conversation_state = {} 


@GigaChad.on_message() #the filters and that stuffs
async def msg_handler(client, message: Message):
    dwnlad = message.text #message sended by the User
    pal = f"✅✅Upload Success✅✅\nUploaded By @Uploader_Tbot\nRemember GigaChad Loves u😘\nThe file was requested by: {message.from_user.id}" #The text who will be at the side of the archive when this is uploaded
    pal_qr = f"✅✅QR Generated✅✅\nUploaded By @Uploader_Tbot\nRemember GigaChad Loves u😘\nThe QR was requested by: {message.from_user.id}"
    who = message.from_user.id
    state = Conversation_state.get(who)
    chatid = message.chat.id
    
    DOWNLOAD_LINK = 0

    if state is None and message.text == "/download":
        await message.reply_text("🙃Give me a link to download🙃")
        Conversation_state[who] = DOWNLOAD_LINK
        
        return

    if state == DOWNLOAD_LINK and URL(dwnlad).scheme and URL(dwnlad).host :
        del Conversation_state[who]
        
        m = await message.reply_text("⬇️**Downloading the file**⬇️")
        try:
            loop = asyncio.get_running_loop()

            ytdownload = yt_dlp.YoutubeDL({"logger": YT_DLP_LOGGER()})
            fdata = await loop.run_in_executor(None, ytdownload.extract_info, dwnlad)
            fname = ytdownload.prepare_filename(fdata)
            await asyncio.sleep(2)
            await GigaChad.send_chat_action(chat_id = chatid,action="upload_document")
            await m.edit("**⬆️Uploading the archive⬆️**")
            await asyncio.sleep(5)
            await m.delete()
            await message.reply_document(fname, caption=pal)
        except Exception:
            await m.edit("❌Not a link supported❌")

        return

    QR = 1
    if state is None and message.text == "/qr":
        await message.reply_text("✍️Send me the text to generate QR✍️")
        Conversation_state[who] = QR

    if state == QR and dwnlad:
        del Conversation_state[who]
        filename = "qr" + ".png"

        img = qrcode.make(dwnlad)
        img.save(filename)

        await GigaChad.send_chat_action(chat_id=chatid, action="upload_photo")
        await message.reply_photo(filename, caption=pal_qr)

        os.remove(filename)
        return

    SHORT = 2
    if state is None and message.text == "/short":
        await message.reply_text("✍️Send me a link to short it✍️")
        Conversation_state[who] = SHORT

    if state == SHORT and dwnlad:
        del Conversation_state[who]
        
        s = pyshorteners.Shortener()

        short_clckru = s.clckru.short(dwnlad)
        short_dagd = s.dagd.short(dwnlad)
        short_osdb = s.osdb.short(dwnlad)

        await GigaChad.send_chat_action(chat_id=chatid, action="typing")
        await message.reply_text("✅✅Here you have your link shorted:\n\n😆From Clck.ru: \n\n" + short_clckru + "\n\n🙃From Da.gd: \n\n" + short_dagd + "\n\n😁From Os.db: \n\n" + short_osdb + "\n\n\nThanks for use @Uploader_Tbot😊", disable_web_page_preview=True)

    test = speedtest.Speedtest()
    if message.text == "/speedtest":
        a = await message.reply_text("**Generating speedTest...please wait this can take a moment**")
        
        
        up_res = test.upload()
        down_res = test.download()
        ping_res = test.results.ping
        await a.edit(f"```Subida: {up_res / 1024 / 1024 / 8:.2f} Mb/s\nBajada: {down_res / 1024 / 1024 / 8:.2f} Mb/s\nPing: {ping_res} ms```\n\n__Bot Hosted in:__ **Heroku❤️**")

    return
class YT_DLP_LOGGER(object):
    def debug(self, msg):
            pass
    def error(self, msg):
            pass
    def warning(self, msg):
            pass

#Start the bot :)
print("Bot running")

if __name__ == '__main__':
    GigaChad.run()
