import discord
import requests

discord_token = ""#とーくん

client = discord.Client()

@client.event
async def on_ready():
    print('Done')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if client.user in message.mentions:
        url = 'https://api.mcsrvstat.us/2/example.com:19132'#じぶんのさばのipに変えてね
        response = requests.get(url)
        jsonData = response.json()

        if jsonData["online"]==False:
            embed = discord.Embed(title="さばの状態", description="オフライン", color=0xff0000)
            await message.channel.send(embed=embed)
            return

        plyrs=""
        for i in jsonData["players"]["list"]:
         plyrs=plyrs+i+"\n"

        embed = discord.Embed(title="さばめい", description="オンライン", color=0x00ff00, url="example.com")
        embed.set_author(name="たいとる", url="example.com", icon_url="example.com/sample.png")
        embed.add_field(name="IP:PORT", value=jsonData['hostname']+":"+str(jsonData['port']))
        embed.add_field(name="人数", value=str(jsonData['players']['online'])+"/"+str(jsonData["players"]["max"]))
        embed.add_field(name="サーバー内にいる人", value=plyrs, inline=False)
        await message.channel.send(embed=embed)
        return


client.run(discord_token)