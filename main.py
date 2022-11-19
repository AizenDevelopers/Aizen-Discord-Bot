import nextcord
import nextcord.utils
import config 
import random
from nextcord.ext import commands, tasks
import os
import youtube_dl


intent = nextcord.Intents.default()
intent.members = True
intent.typing = True
intent.presences = True
intent.message_content = True
intent.bans = True

bot = commands.Bot(command_prefix=config.Prefix, intents=intent)

@bot.event #Memberi tahu jika bot Online
async def on_ready():
    print('Aizen online !')
    await bot.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Mobile Legends"))

@bot.command(
    name="hallo",
    pass_context = True
)
async def hi(ctx):
    await ctx.send(
        f'Hallo {ctx.author.mention}, Selamat datang di server AutoFarm!'
    )

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(1042626769506807808)
  await channel.send(
    f'Sayonara {member.mention}'
  )

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(1042626769506807808)
  await channel.send(
    f'{member.mention} Selamat datang di server AutoFarm!'
  )

@bot.command(name="psatir")
async def psatir(ctx, *, question):
  emoji = bot.get_emoji(1042430327525756970)
  response = [
    "Afah iyah?",
    "Yang bener..",
    "Keknya salah",
    "Menurutku begitu..",
    "Semoga aja ga begitu",
    "Ya Ndak Tau Kok Tanya Saya...",
    "Mungkin... saja",
    "Iya",
    "Enggak juga",
    "Kayak gitu-gitu"
  ]
  await ctx.send(f'{emoji} Pertanyaan: {question}\n{emoji} Jawaban: {random.choice(response)}')


@bot.event
async def on_member_ban(guild, user):
  await bot.send(f'Wahh {user} kena ban!!')

@bot.event
async def on_member_unban(guild, user):
  await bot.send(f'Wahh {user} di unban dari {guild.name} ini!')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: nextcord.Member = None, *, reason=None):
    if user == None:
        await ctx.send("Please enter a user!")
        return

    await user.kick(reason=reason)
    await ctx.send(f'Menendang {user.name} dengan alasan {reason}')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: nextcord.Member =None, *, reason=None):
  if user == None:
    await ctx.send("Tolong masukkan username!")
    return
  embed = nextcord.Embed(title="Sucess", description=f'Membanned {user.name} dengan alasan {reason}')
  await user.ban(reason=reason)
  await ctx.send(embed)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user: nextcord.User=None, reason=None):
  if user == None:
    await ctx.send("Tolong masukkan username!")
    return
  
  guild = ctx.guild
  embed = nextcord.Embed(title="Sucess", description=f'{user} has been unbanned')

  await ctx.send(embed = embed)
  await guild.unban(user = user)

@bot.command(name="random_kursi")
async def random_kursi(ctx, *, user=None):
  if user == None:
    await ctx.send("Tolong masukkan nama!")
    return
  
  teman_kelas = [
    'Andaru, 7',
    'Grace, 18',
    'Gerryn, 27'
    'Nicho, 29',
    'Dimas, 10',
    'Tatag, 21',
    'Gasa, 31',
    'Audrey, 2',
    'Gisel, 17',
    'Kartika, 23',
    'Serafina, 33',
    'Axel, 15',
    'Sasya, 32',
    'Tasya, 8',
    'Tara, 3',
    'Kayla, 9',
    'Brian, 4',
    'Tesa, 16',
    'Nuel, 20',
    'Jojo, 30',
    'Bryan, 5',
    'Felicya, 11',
    'Rimang, 19',
    'Maria, 26',
    'Aurel. 28',
    'Krisna, 12',
    "Bintar, 6",
    'Aldo, 1',
    'Kanes, 13'
    'Myisha, 25'
  ]
  embed_kursi = nextcord.Embed(title="Random Kursi", description=f'{user} teman kursi yang kamu dapatkan adalah, {random.choice(teman_kelas)}', color=1752220 )
  await ctx.send(embed = embed_kursi)

@bot.command()
async def dor(ctx, user: nextcord.Member=None, *, reason=None):
  if user == None:
    await ctx.send("Tolong masukkan id / mention usernya")
    return

  embed_dor = nextcord.Embed(title="Tembak!\n", description=f"{ctx.author.mention}, kamu berhasil menembak, {user}\nDengan alasan: {reason}", color=15548997)
  await ctx.send(embed = embed_dor)
  await user.send(f'Hallo, {user},\n{ctx.author.mention} menembakkmu dengan alasan: {reason}')


bot.run(config.TOKEN)