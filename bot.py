import discord
from discord.ext import commands
from discord import Option
bot = commands.Bot()
roleid = 999284677246459974
try:
	n = open("token.txt", "r")
	token = n.readline()
except:
	token = input("what is the token for the bot \n")
	n = open("token.txt", "a")
	n.close()
	n = open("token.txt", "w")
	n.write(token)
	n.close()
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
		d = line +"		:		" + str(count(line)) + "\n"
		q = q + d
	lines.close()
	return "**"+q+"**"

def generate(name):
	if count(name) == "0" :
			return 0
	elif count(name) == "1":
		return 1
	else:
		return ok
def ho(name):
	f = open(f"accounts\\{name}.txt")
	b = f.readline()
	lines = f.readlines()
	f = open(f"accounts\\{name}.txt", "w")
	f.writelines(lines)
	return "**"+ b + "**"
def one(name):
	f = open(f"accounts\\{name}.txt")
	b = f.readline()
	f = open(f"accounts\\{name}.txt", "w")
	f.writelines("")
	return "**"+b+"**"
def compare(name):
	lines = open("names.txt","r")
	for line in lines:
		line = line.rstrip()
		line = line.strip()
		if name.lower() == line.lower():
			lines.close()
			return "available"
	lines.close()
	return "unavailable"


@bot.event
async def on_ready():
    print('Ready to generate')
a = []

@commands.has_permissions(administrator=True)
@bot.slash_command(description="lets you add more type of accounts (you need to have permissions for that)")

async def add(ctx,type: Option(str,"the type that you want to gen",required=True,default="netflix")):
	arg = type
	mention = ctx.author.mention
	if arg == None:
		embed=discord.Embed(title="ERROR", description=f"**{mention}you have to put what type you want to add**", color=0x9b1900)
		await ctx.respond(embed=embed, delete_after=5)
	else:
		x = open(f"accounts\\{arg}.txt","w")
		x.close()
		x = open("names.txt", "a")
		x.write(f"\n{arg}")
		embed=discord.Embed(title="SUCCES", description=f"**{arg.upper()} has successfully added on the name list**", color=0x9b1900)
		await ctx.respond(embed=embed, delete_after=5)
@add.error
async def add_error(ctx,error):
	if isinstance(error, commands.MissingPermissions):
		mention = ctx.author.mention
		embed=discord.Embed(title="ERROR", description=f"**Sorry {mention}, you do not have permissions to do that!**", color=0x9b1900)
		await ctx.respond(embed=embed, delete_after=5)
@commands.has_role(roleid)
@bot.slash_command(description="lets you see the stock of the generator")
async def stock(ctx):
	
	embed=discord.Embed(title="Stock", description=stocko(), color=0x9b1900)
	await ctx.respond(embed=embed, delete_after=100)
@commands.has_role(roleid)
@bot.slash_command(description="lets you generate any type of account")
async def gen(ctx,type: Option(str,"the type that you want to gen",required=True,default="netflix")):
	arg = type
	mention = ctx.author.mention
	if ctx.channel.type == discord.ChannelType.private:
		embed=discord.Embed(title="ERROR", description="**Sorry you have no right to generate in dm's**", color=0x9b1900)
		await ctx.respond(embed=embed)
	else:
		if arg == None:
			embed=discord.Embed(title=f"ERROR", description=f"**{mention}You need to specify the type of accounts you want to generate (EX: /gen netflix)**", color=0x9b1900)
			await ctx.respond(embed=embed, delete_after=5)
		else:
			if compare(arg) == "available":
				if count(arg) == "0":
					embed=discord.Embed(title=f"{arg.upper()} ACCOUNT:", description=f"**Sorry {mention}, there is actually no {arg} accounts for the moment**", color=0x9b1900)
					await ctx.respond(embed=embed, delete_after=5)

				elif count(arg) == "1":
					embed=discord.Embed(title=f"{arg.upper()} ACCOUNT:", description=one(arg), color=0x9b1900)
					await ctx.author.respond(embed=embed, delete_after=20)
					embed=discord.Embed(title=f"{arg.upper()} ACCOUNT:", description=f"**{mention}, your {arg} account has been sent to you in the dm's**", color=0x9b1900)
					await ctx.respond(embed=embed, delete_after=5)


				else:
					embed=discord.Embed(title=f"{arg.upper()} ACCOUNT:", description=ho(arg), color=0x9b1900)
					await ctx.author.respond(embed=embed, delete_after=20)
					embed=discord.Embed(title=f"{arg.upper()} ACCOUNT:", description=f"**{mention}, your {arg} account has been sent to you in the dm's**", color=0x9b1900)
					await ctx.respond(embed=embed, delete_after=5)
			elif compare(arg) == "unavailable":
				embed=discord.Embed(title="error", description=f"Sorry {mention}, the type of accounts that you want to generate does not exist. Use /stock to see what is available", color=0x9b1900)
				await ctx.respond(embed=embed, delete_after=5)
			else:
				print("error")
@commands.has_role(roleid)
@bot.slash_command(description="Help")
async def help(ctx):
	embed=discord.Embed(title="HELP", description=f"**/gen [account type] (EX: /gen netflix)\n/stock**", color=0x9b1900)
	await ctx.respond(embed=embed, delete_after=5)
bot.run(token)
