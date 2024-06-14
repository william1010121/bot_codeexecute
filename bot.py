import discord
from discord.ext import commands
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

import random
import string
def randomName() :
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def python(ctx, *, code: str):
    # 創建一個子進程來執行代碼
    code = code.replace('```', '')
    try:
        result = subprocess.run(
            ["python", "-c", code],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout if result.stdout else result.stderr
    except subprocess.TimeoutExpired:
        output = "Execution timed out."
    except Exception as e:
        output = str(e)

    await ctx.send(f"```\n{output}\n```")

@bot.command()
async def cpp(ctx, *, code: str):
    code = code.replace('```', '')
    name = randomName()
    with open(f"cpp/{name}.cpp", "w") as f:
        f.write(code)
    try:
        result = subprocess.run(
            ["g++", f"cpp/{name}.cpp", "-o", f"cpp/{name}", "-std=c++17"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            raise Exception(result.stderr)
        result = subprocess.run(
            [f"./cpp/{name}"],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout if result.stdout else result.stderr
    except subprocess.TimeoutExpired:
        output = "Execution timed out."
    except Exception as e:
        output = str(e)
    # remove the name.cpp 
    await ctx.send(f"```\n{output}\n```")

bot.run(os.getenv("DISCORD_TOKEN"))