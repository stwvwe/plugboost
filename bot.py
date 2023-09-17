import discord,requests
from discord.ext import commands

bot = commands.Bot(command_prefix='+', help_command=None, intents=discord.Intents.all())

### -- EDIT THIS LINE -- ###
token = "MTEyNDYyMzIwNjIyNjA3NTY0OA.Gr7h3b.d65nwAD1YCcj_dPCaV-yR2VsT6UoD4IzbOg7vg"
yourid = 1149010158379343963
vouch_channel_id = 1124593049033519104
endpoint_url = "https://plugboost.vercel.app/"
api_key = "steve1745"
    
@bot.event
async def on_message(message):
    if message.channel.id == vouch_channel_id and message.author.id != bot.user.id and message.author.id != yourid:
        if len(message.content) > 250: # just cus looks better on site
            await message.author.send("Your message is too long, please keep it under 250 characters.")
            await message.delete()
            return
        r = requests.post(endpoint_url, json = {"discord_tag": message.author.name,"discord_id": message.author.id,"vouch_content": {"message_id": str(message.id),"content": message.content},"api_key": api_key})
        await message.reply("Thank you!")
    await bot.process_commands(message) # So that you can add regular commands as well

bot.run(token)
