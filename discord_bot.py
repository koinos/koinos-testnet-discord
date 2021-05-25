import requests
import yaml
import argparse
import urllib.parse

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
config = None

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That's not a command I know!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("An address is required.")

@bot.command()
async def faucet(ctx, address):
    print(f"Faucet request from {ctx.author}.")
    try:
        url = urllib.parse.urljoin(config["faucet_url"], "request_koin")
        r = requests.post(url, json={"id": f"{ctx.author.id}", "address": address})
    except Exception as e:
        print(e)
    await ctx.send(f'{r.json()["message"]}')

def main():
    parser = argparse.ArgumentParser(description='Koinos testnet faucet server.')
    parser.add_argument('--config', '-c', type=str, default="config.yaml", help="configuration yaml file")
    args = parser.parse_args()

    # Load the config
    with open(args.config, "r") as f:
        global config
        config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    
    bot.run(config["bot_token"])

if __name__ == "__main__":
    main()
