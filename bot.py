from pyrogram import Client, filters
import pyrogram 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import wget
import os
import configparser
import asyncio
import tgcrypto

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
    await message.reply_text(f"🙃User: {message.from_user.mention}\n🆔ID: {message.from_user.id}\n📛Username: @{message.from_user.username}\n\n🇬🇧Hi Human, I'm a **Uploader to Telegram bot**, i can upload files from some sites(Example: Uptodown.com, Malavida.com, etc..., just simple sites, in other actualizations will come the Clouds and Youtube), not at all, i can't upload from MEGA, Gdrive, OneDrive, etc...,Here you can see more info about my Creator😁👇\n\n\n🇪🇸Hola Humano, Soy un **Bot que suber archivos a Telegram**, puedo subir archivos directos desde varios sitios(Ejemplos: Uptodown.com, Malavida.com, etc..., solo sitios simples, en proximas actualizaciones podras descargar desde nubes y Youtube), no todos, no puedo subir desde MEGA, Gdrive, OneDrive, etc...,Aqui puedes ver mas info acerca de mi creador😁👇",
    
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
    await message.reply_text("🇬🇧Just send me a link and i will try to download it\n\nNote: If you want to upload some other things and the bot don't recongnize him, you can go to @DirectLinkGeneratorbot, @DirectLinkGen_bot or @MaxFile2LinkBot.\n\n🇪🇸Solo enviame un link y lo intentare descargar\n\n**Nota**: Si envias un enlace y el bot no lo reconoce, puedes enviar el enlace a @DirectLinkGeneratorbot, @DirectLinkGen_bot o @MaxFile2LinkBot.\n")

@UploaderBot.on_message(filters.regex(pattern=".*http.*") & ~filters.edited) #the filters and that stuffs
async def descargar(client, message: Message):
    msg = await message.reply_text(text="🔎Checking URL🔎", quote=True) #Check the URL before Download
    dwnlad = message.text #Link sended by the User
    photo = "https://telegra.ph/file/fad940fbefd120bd58200.png" #Photo of the archive, you can delet it if you don't want a photo in the archive, or just change it for other
    pal = f"✅✅Upload Success✅✅\nUploaded By @Uploader_Tbot\nRemember GigaChad Loves u😘\nThe file was requested by: {message.from_user.id}" #The text who will be at the side of the archive when this is uploaded
    try:
        await msg.edit(f"⬇️Trying to Download the file⬇️") #this will be edit "Checking URL" when he check the URL
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ **0%**")
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ **25%**")
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️ **50%**")
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️ **75%**")
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️ **100%**")
        await asyncio.sleep(.100)
        await msg.edit(f"⬇️Trying to Download the file⬇️\n\nPercentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️")
        await asyncio.sleep(.200)
        await msg.edit("**File Downloaded, the Upload we will start in a moment🙂**")
        await asyncio.sleep(.200)
        filename = wget.download(dwnlad)#Download the archive
        photo_file = wget.download(photo)#Download the photo who will be with the archive
        pak = "fad940fbefd120bd58200.png" #Name + extension of the photo 
        await msg.edit("⬆️Uploading file⬆️")#this will be edit "Trying to Download Archive" when the archive is downloaded
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n\n⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ **0%**")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n\n⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ **25%**")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n\n⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️ **50%**")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️ **75%**")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬜️⬜️ **100%**")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\nCompleted, Plz wait 🕛")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\nCompleted, Plz wait 🕒")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\nCompleted, Plz wait 🕕")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\nCompleted, Plz wait 🕘")
        await asyncio.sleep(.100)
        await msg.edit("⬆️Uploading file⬆️ Percentage:\n⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️\nCompleted, Plz wait 🕛")
        await msg.delete()
        await message.reply_document(filename, thumb=pak, caption=pal) #Here we upload the archive
        #Remove from server
        os.remove(filename)
        os.remove(photo_file)
    except Exception:
        await msg.edit("❌❌Link not supported❌❌")#This he will show if the link is invalid

print("Bot running")


if __name__ == '__main__':
    UploaderBot.run()
