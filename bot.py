from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import wget
import os

UploaderBot = Client(
    "Uploaderbot",
    bot_token= "TOKEN_FROM_BOTFATHER", #example: 1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ
    api_hash= "API Hash From my.telegram.org",
    api_id= "API ID from my.telegram.org" #int valor (example:(int(12345)))
)


@UploaderBot.on_message(filters.command("start") & ~filters.edited)
async def Start(filters, message):
    print(f"🤖The Bot was started by: {message.from_user.id}\n{message.from_user.username}\n") #In Spanish: "El bot ha sido comenzado por: "
    await message.reply_photo("https://telegra.ph/file/fad940fbefd120bd58200.png")
    await message.reply_text(f"🙃User: {message.from_user.mention}\n🆔ID: {message.from_user.id}\n📛Username: @{message.from_user.username}\n\n🇬🇧Hi Human, I'm a **Uploader to Telegram bot**, i can upload files from some sites(Example: Uptodown.com, Malavida.com, etc..., just simple sites, in other actualizations will come the Clouds and Youtube), not at all, i can't upload from MEGA, Gdrive, OneDrive, etc...,Here you can see more info about my Creator😁👇\n\n\n🇪🇸Hola Humano, Soy un **Bot que sube archivos a Telegram**, puedo subir archivos directos desde varios sitios(Ejemplos: Uptodown.com, Malavida.com, etc..., solo sitios simples, en proximas actualizaciones podras descargar desde nubes y Youtube), no todos, no puedo subir desde MEGA, Gdrive, OneDrive, etc...,Aqui puedes ver mas info acerca de mi creador😁👇",
    
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("👾Github👾", url="https://www.github.com/Tnoob-dev"),
        InlineKeyboardButton("🐦Twitter🐦", url="https://twitter.com/TitiLM30")
    ],
    [InlineKeyboardButton("📞User Telegram📞", url="https://t.me/TitiLM30")]
    ]
    
    )
    )
@UploaderBot.on_message(filters.command("help") & ~filters.edited)
async def ayuda(filters, message):
    await message.reply_photo("https://telegra.ph/file/a09ec751bdfd44711504a.png")
    await message.reply_text("🇬🇧Just send me a link and i will try to download it\n\n🇪🇸Solo enviame un link y lo intentare descargar")

@UploaderBot.on_message(filters.regex(pattern=".*http.*") & ~filters.edited) #the filters and that stuffs
async def descargar(client, message: Message):
    msg = await message.reply_text(text="🔎Checking URL🔎", quote=True) #Check the URL before Download
    dwnlad = message.text #Link of the User
    photo = "https://telegra.ph/file/fad940fbefd120bd58200.png" #Photo of the archive, you can delet it if you don't want a photo in the archive, or just change it for other
    pal = "😉Here you have😉" #The text who will be at the side of the archive when this is uploaded
    try:
        await msg.edit("⬇️Trying to Download the archive⬇️") #this will be edit "Checking URL" when he check the URL
        arch = wget.download(dwnlad)#Download the archive
        photo = wget.download(photo)#Download the photo wh will be with the archive
        pak = "fad940fbefd120bd58200.png" #Name + extension of the photo 
        await msg.edit("⬆️Uploading Archive⬆️")#this will be edit "Trying to Download Archive" when the archive is downloaded
        await message.reply_document(arch, thumb=pak, caption=pal) #Here we upload the archive
        await msg.delete()#Delete the message when Upload the archive
        #Remove from server
        os.remove(dwnlad)
        os.remove(photo)
    except Exception:
        await msg.edit("❌❌Link not supported❌❌")#This he will show if the link is invalid
        
print("Bot running")
UploaderBot.run()
