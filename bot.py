#Modules
import os
from pyrogram import Client, filters
import pyrogram
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio
import tgcrypto
import yt_dlp
from yt_dlp import YoutubeDL
from yarl import URL
import pyshorteners
import qrcode
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
    await message.reply_text(f"🙃User: {message.from_user.mention}\n🆔ID: {message.from_user.id}\n📛Username: @{message.from_user.username}\n\n🇬🇧Hi Human, I'm a **Uploader to Telegram bot, i can generate QR Codes too, and short URLs**, i can upload files from some sites(Example: Uptodown.com, Malavida.com, Youtube.com, facebook.com,etc..., in other actualizations will come MEGA, and other amazing things), Here you can see more info about my Creator😁👇\n\n\n🇪🇸Hola Humano, Soy un **Bot que sube archivos a Telegram, genera codigos QR y acorta enlaces**, puedo subir archivos directos desde varios sitios(Ejemplos: Uptodown.com, Malavida.com, Youtube.com, facebook.com,etc..., en proximas actualizaciones podras descargar desde MEGA, y vendran mas cosas increibles), Aqui puedes ver mas info acerca de mi creador😁👇",
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("👾Github👾", url="https://www.github.com/Tnoob-dev"),

        InlineKeyboardButton("🐦Twitter🐦", url="https://twitter.com/TitiLM30")
    ],
    [InlineKeyboardButton("⌨️Canal interesante⌨️", url="https://t.me/s3softwareyprogramacion"),

     InlineKeyboardButton("💻Grupo adjunto💻", url="https://t.me/S3SPGrupo")
    ]
    ]
    
    )
    )
    await message.reply_text("**🇬🇧Note: Send /help to know what i can do\n\n🇪🇸Nota: Envia /help para conocer que puedo hacer**")
@GigaChad.on_message(filters.command("help") & ~filters.edited)
async def ayuda(filters, message):
    await message.reply_photo("https://telegra.ph/file/86a8426af71ef4f7eeec8.png")
    await message.reply_text("🇬🇧Send /download and later send me the link, i will Download it and send you the file\n\nSend /qr and later a text and i will generate you a QR Code with the text\n\nSend /short and later send a link and i will short it\n\nNote: If you want to upload some other things and the bot don't recongnize him, you can go to @DirectLinkGeneratorbot, @DirectLinkGen_bot or @MaxFile2LinkBot.\n\n🇪🇸Envia /download y luego el link de descarga, lo descargare y luego te enviare el archivo\n\nEnvia /qr y luego un texto, y te generare un codigo QR con el texto dentro\n\nEnvia /short y luego un link y te enviare un link acortado con el link que enviaste\n\nEnvia /gdown e intentare descargar el enlace de GDrive\n\n**Nota**: Si envias un enlace y el bot no lo reconoce, puedes enviar el enlace a @DirectLinkGeneratorbot, @DirectLinkGen_bot o @MaxFile2LinkBot.\n")


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
            await message.reply_text("❌Not a link supported❌")

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

        return

    DOWNLOAD_LINK2 = 3
    if state is None and message.text == "/down_480":
        await message.reply_text(f"Hola {message.from_user.first_name}, Enviame el link a descargar UwU") 
        Conversation_state[who] = DOWNLOAD_LINK2

    if state == DOWNLOAD_LINK2 and dwnlad:

        capt = f"Aqui tienes tu video guapo ( ˘ ³˘)♥️\n\n𝕮𝖔𝖕𝖞𝖗𝖎𝖌𝖍𝖙 @𝕿𝖎𝖙𝖎𝕷𝕸30\n\nEl archivo ha sido requerido por @{message.from_user.username}"

        del Conversation_state[who]

        ydl_opts = {"format": "best[height<=480]"}

        ydl = yt_dlp.YoutubeDL(ydl_opts)

        info = ydl.extract_info(dwnlad)     
        msg_bot = await message.reply_text("⬇️**Downloading the file**⬇️")
        await asyncio.sleep(3)
        filen = ydl.prepare_filename(info)
        await GigaChad.send_chat_action(chat_id = chatid,action="upload_video")
        await msg_bot.edit("⬆️**Uploading the file**⬆️")
        await msg_bot.delete()
        await asyncio.sleep(5)

        await message.reply_document(filen, caption=capt)
        
        return


    DOWNLOAD_LINK3 = 4
    if state is None and message.text == "/down_360":
        await message.reply_text(f"Hola {message.from_user.first_name}, Enviame el link a descargar UwU") 
        Conversation_state[who] = DOWNLOAD_LINK3

    if state == DOWNLOAD_LINK3 and dwnlad:

        capt = f"Aqui tienes tu video guapo ( ˘ ³˘)♥️\n\n𝕮𝖔𝖕𝖞𝖗𝖎𝖌𝖍𝖙 @𝕿𝖎𝖙𝖎𝕷𝕸30\n\nEl archivo ha sido requerido por @{message.from_user.username}"

        del Conversation_state[who]

        ydl_opts = {"format": "best[height<=360]"}

        ydl = yt_dlp.YoutubeDL(ydl_opts)

        info = ydl.extract_info(dwnlad)     
        msg_bot = await message.reply_text("⬇️**Downloading the file**⬇️")
        await asyncio.sleep(3)
        filen = ydl.prepare_filename(info)
        await GigaChad.send_chat_action(chat_id = chatid,action="upload_video")
        await msg_bot.edit("⬆️**Uploading the file**⬆️")
        await msg_bot.delete()
        await asyncio.sleep(5)

        await message.reply_document(filen, caption=capt)

        return

    DOWNLOAD_LINK4 = 5
    if state is None and message.text == "/down_240":
        await message.reply_text(f"Hola {message.from_user.first_name}, Enviame el link a descargar UwU") 
        Conversation_state[who] = DOWNLOAD_LINK4
    if state == DOWNLOAD_LINK4 and dwnlad:

        capt = f"Aqui tienes tu video guapo ( ˘ ³˘)♥️\n\n𝕮𝖔𝖕𝖞𝖗𝖎𝖌𝖍𝖙 @𝕿𝖎𝖙𝖎𝕷𝕸30\n\nEl archivo ha sido requerido por @{message.from_user.username}"

        del Conversation_state[who]

        ydl_opts = {"format": "best[height<=240]"}

        ydl = yt_dlp.YoutubeDL(ydl_opts)

        info = ydl.extract_info(dwnlad)     
        msg_bot = await message.reply_text("⬇️**Downloading the file**⬇️")
        await asyncio.sleep(3)
        filen = ydl.prepare_filename(info)


        await GigaChad.send_chat_action(chat_id = chatid,action="upload_video")


        await msg_bot.edit("⬆️**Uploading the file**⬆️")
        await msg_bot.delete()
        await asyncio.sleep(5)

        await message.reply_document(filen, caption=capt)

        return

    DOWNLOAD_LINK5 = 6
    if state is None and message.text == "/down_144":
        await message.reply_text(f"Hola {message.from_user.first_name}, Enviame el link a descargar UwU") 
        Conversation_state[who] = DOWNLOAD_LINK5

    if state == DOWNLOAD_LINK5 and dwnlad:

        capt = f"Aqui tienes tu video guapo ( ˘ ³˘)♥️\n\n𝕮𝖔𝖕𝖞𝖗𝖎𝖌𝖍𝖙 @𝕿𝖎𝖙𝖎𝕷𝕸30\n\nEl archivo ha sido requerido por @{message.from_user.username}"

        del Conversation_state[who]

        ydl_opts = {"format": "best[height<=144]"}

        ydl = yt_dlp.YoutubeDL(ydl_opts)

        info = ydl.extract_info(dwnlad)     
        msg_bot = await message.reply_text("⬇️**Downloading the file**⬇️")
        await asyncio.sleep(3)
        filen = ydl.prepare_filename(info)
        await GigaChad.send_chat_action(chat_id = chatid,action="upload_video")

        await msg_bot.edit("⬆️**Uploading the file**⬆️")
        await msg_bot.delete()
        await asyncio.sleep(5)

        await message.reply_document(filen, caption=capt)

        return

    DOWNLOAD_LINK6 = 7
    if state is None and message.text == "/down_1080":
        await message.reply_text(f"Hola {message.from_user.first_name}, Enviame el link a descargar UwU") 
        Conversation_state[who] = DOWNLOAD_LINK6

    if state == DOWNLOAD_LINK6 and dwnlad:

        capt = f"Aqui tienes tu video guapo ( ˘ ³˘)♥️\n\n𝕮𝖔𝖕𝖞𝖗𝖎𝖌𝖍𝖙 @𝕿𝖎𝖙𝖎𝕷𝕸30\n\nEl archivo ha sido requerido por @{message.from_user.username}"

        del Conversation_state[who]

        ydl_opts = {"format": "best[height<=1080]"}

        ydl = yt_dlp.YoutubeDL(ydl_opts)

        info = ydl.extract_info(dwnlad)     
        msg_bot = await message.reply_text("⬇️**Downloading the file**⬇️")
        await asyncio.sleep(3)
        filen = ydl.prepare_filename(info)
        await GigaChad.send_chat_action(chat_id = chatid,action="upload_video")
        await msg_bot.edit("⬆️**Uploading the file**⬆️")
        await msg_bot.delete()
        await asyncio.sleep(5)

        await message.reply_document(filen, caption=capt)

        return
class YT_DLP_LOGGER(object):
    def debug(self, msg):
            pass
    def error(self, msg):
            pass
    def warning(self, msg):
            pass

print("Bot running")



if __name__ == '__main__':
    GigaChad.run()
