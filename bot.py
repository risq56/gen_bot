import discord
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
token = input("what is the token for the bot")
bot = ComponentsBot('/', help_command=None)
def count(name):
	lines = open(f"accounts\\{name}.txt", 'r')
	x = 0
	for line in lines :
		if line.rstrip() == "":
			x += 0
		elif line.rstrip() != "":
			x += 1
	return str(x)

def stocko():
	lines = open ("names.txt","r")
	q = ""
	for line in lines:
		line = line.rstrip()
		line = line.strip()
		d = line +" : " + str(count(line)) + "\n"
		q = q + d
	return q

def generate(name):
	if count(name) == "0" :
			return 0
	elif count(name) == "1":
		return 1
	else:
		return ok
def ho(name):
	print("option A")
	f = open(f"accounts\\{name}.txt")
	b = f.readline()
	lines = f.readlines()
	f = open(f"accounts\\{name}.txt", "w")
	f.writelines(lines)
	return(b)
def one(name):
	print("option b")
	f = open(f"accounts\\{name}.txt")
	b = f.readline()
	f = open(f"accounts\\{name}.txt", "w")
	f.writelines("")
	return(b)
def compare(name):
	lines = open("names.txt","r")
	for line in lines:
		line = line.rstrip()
		line = line.strip()
		if name.lower() == line.lower():
			return "available"
	return "unavailable"


@bot.event
async def on_ready():
    print('Ready to support ✅')
a = []



@bot.command()
async def stock(ctx):
    embed=discord.Embed(title="Stock", description=stocko(), color=0x9b1900)
    await ctx.send(embed=embed)
@bot.command()
async def gen(ctx,arg):
	if compare(arg) == "available":
		if count(arg) == "0":
			embed=discord.Embed(title=f"{arg.upper()}", description=f"there is actually no {arg} accounts for the moment", color=0x9b1900)
			await ctx.author.send(embed=embed)

		elif count(arg) == "1":
			embed=discord.Embed(title=f"{arg.upper()}", description=one(arg), color=0x9b1900)
			await ctx.author.send(embed=embed)

		else:
			embed=discord.Embed(title=f"{arg.upper()}", description=ho(arg), color=0x9b1900)
			await ctx.author.send(embed=embed)
	elif compare(arg) == "unavailable":
		embed=discord.Embed(title="error", description="the account that you want to generate does not exist. Use /stock to see what is available", color=0x9b1900)
		await ctx.send(embed=embed)
	else:
		print("error")


bot.run(token)
