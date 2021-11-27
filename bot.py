from pyrogram import Client, filters
import pyrogram 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import configparser
import asyncio
import tgcrypto
import yt_dlp
from yarl import URL

config = configparser.ConfigParser()
config.read("config.ini")

UploaderBot = Client(
    "Uploaderbot",
    api_id = config.get('pyrogram', 'api_id'), #API_ID it's on the config.ini file
    api_hash = config.get('pyrogram', 'api_hash'), #API_HASh it's on the config.ini file
    bot_token = config.get('pyrogram', 'bot_token') #BOT_TOKEN it's on the config.ini file
)




@UploaderBot.on_message(filters.command("start") & ~filters.edited)
async def Start(filters, message):
    print(f"🤖The Bot was started by: {message.from_user.id}\n{message.from_user.username}\n") #In Spanish: "El bot ha sido comenzado por: "
    await message.reply_photo("https://telegra.ph/file/fad940fbefd120bd58200.png")
    await message.reply_text(f"🙃User: {message.from_user.mention}\n🆔ID: {message.from_user.id}\n📛Username: @{message.from_user.username}\n\n🇬🇧Hi Human, I'm a **Uploader to Telegram bot**, i can upload files from some sites(Example: Uptodown.com, Malavida.com, Youtube.com, etc..., just simple sites, in other actualizations will come the Clouds and Youtube), not at all, i can't upload from MEGA, Gdrive, OneDrive, etc...,Here you can see more info about my Creator😁👇\n\n\n🇪🇸Hola Humano, Soy un **Bot que suber archivos a Telegram**, puedo subir archivos directos desde varios sitios(Ejemplos: Uptodown.com, Malavida.com, Youtube.com, etc..., solo sitios simples, en proximas actualizaciones podras descargar desde nubes y Youtube), no todos, no puedo subir desde MEGA, Gdrive, OneDrive, etc...,Aqui puedes ver mas info acerca de mi creador😁👇",
    
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("👾Github👾", url="https://www.github.com/Tnoob-dev"),
        InlineKeyboardButton("🐦Twitter🐦", url="https://twitter.com/TitiLM30")
    ],
    [InlineKeyboardButton("📱User Telegram📱", url="https://t.me/TitiLM30")]
    ]
    
    )
    )


@UploaderBot.on_message(filters.command("help") & ~filters.edited)
async def ayuda(filters, message):
    await message.reply_photo("https://telegra.ph/file/a09ec751bdfd44711504a.png")
    await message.reply_text("🇬🇧Just send me a link and i will try to download it\n\n🇪🇸Solo enviame un link y lo intentare descargar")

@UploaderBot.on_message(filters.command("help") & ~filters.edited)
async def ayuda(filters, message):
    await message.reply_photo("https://telegra.ph/file/a09ec751bdfd44711504a.png")
    await message.reply_text("🇬🇧Just send /download, later send me a link and i will download it\n\nNote: If you want to upload some other things and the bot don't recongnize him, you can go to @DirectLinkGeneratorbot, @DirectLinkGen_bot or @MaxFile2LinkBot.\n\n🇪🇸Solo enviame /download, luego enviame un link y lo descargare\n\n**Nota**: Si envias un enlace y el bot no lo reconoce, puedes enviar el enlace a @DirectLinkGeneratorbot, @DirectLinkGen_bot o @MaxFile2LinkBot.\n")


Conversation_state = {} 


@UploaderBot.on_message() #the filters and that stuffs
async def descargar(client, message: Message):
    dwnlad = message.text #Link sended by the User
    pal = f"✅✅Upload Success✅✅\nUploaded By @Uploader_Tbot\nRemember GigaChad Loves u😘\nThe file was requested by: {message.from_user.id}" #The text who will be at the side of the archive when this is uploaded
    
    who = message.from_user.id
    state = Conversation_state.get(who)
    
    DOWNLOAD_LINK = True

    if state is None and message.text == "/download":
        await message.reply_text("🙃Give me a link to download🙃")
        Conversation_state[who] = DOWNLOAD_LINK
        
        return

    if state == DOWNLOAD_LINK and URL(dwnlad).scheme and URL(dwnlad).host :
        del Conversation_state[who]
        try:
            loop = asyncio.get_running_loop()

            ytdownload = yt_dlp.YoutubeDL({"logger": YT_DLP_LOGGER()})
            fdata = await loop.run_in_executor(None, ytdownload.extract_info, dwnlad)
            fname = ytdownload.prepare_filename(fdata)

            await message.reply_document(fname, caption=pal)
        except Exception:
            await message.reply_text("Not a link supported")

class YT_DLP_LOGGER(object):
    def debug(self, msg):
            pass
    def error(self, msg):
            pass
    def warning(self, msg):
            pass

print("Bot running")


if __name__ == '__main__':
    UploaderBot.run()
