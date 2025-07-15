import discord
from discord.ext import commands
import asyncio
import random

class TaiXiu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="taixiu")
    @commands.cooldown(rate = 1, per = 8, type = commands.BucketType.user)
    
    async def taixiu(self, ctx, prize: int = None):
        if prize is None or prize <= 0:
            embed = discord.Embed(
                description="⚠️ Số tiền cược phải lớn hơn 0!",
                color=discord.Color.orange()
            )
            return await ctx.send(embed = embed)

        if prize > 250000:
            prize = 250000

        emojis = {"🔴": "tài", "🟢": "xỉu"}

        embed = discord.Embed(
            title="🎮 Tài Xỉu - Chọn lựa của bạn",
            description=(
                f"{ctx.author.mention} đã cược **{prize:,}đ**!\n\n"
                "Hãy chọn bằng cách react:\n"
                "🔴 = **Tài**\n"
                "🟢 = **Xỉu**"
            ),
            color=discord.Color.random()
        )
        message = await ctx.send(embed=embed)

        for emoji in emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            return (
                user == ctx.author and
                str(reaction.emoji) in emojis and
                reaction.message.id == message.id
            )

        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=30.0, check=check)
        except asyncio.TimeoutError:
            timeout_embed = discord.Embed(
                description = "⏰ Hết thời gian chọn! Vui lòng thử lại sau.",
                color = discord.Color.red()
            )
            return await ctx.send(embed=timeout_embed)

        choice = emojis[str(reaction.emoji)]
        
        '''
        dice = [random.randint(1, 6) for _ in range(3)]
        total = sum(dice)
        result = "tài" if 11 <= total <= 17 else "xỉu"
        win = (choice == result)
        '''
        
        win = random.random() < 0.4

        if win:
            result = choice
        else:
            result = "xỉu" if choice == "tài" else "tài"

        def generate_dice_for(result):
            while True:
                dice = [random.randint(1, 6) for _ in range(3)]
                total = sum(dice)
                current_result = "tài" if 11 <= total <= 17 else "xỉu"
                if current_result == result:
                    return dice

        dice = generate_dice_for(result)
        total = sum(dice)

        result_embed = discord.Embed(
            title = "🎲 Kết quả Tài Xỉu",
            color = discord.Color.green() if win else discord.Color.red()
        )
        result_embed.add_field(name = "🎲 Xúc xắc", value=f"`{' + '.join(map(str, dice))} = {total}`", inline = False)
        result_embed.add_field(name = "📢 Kết quả", value=f"**{result.upper()}**", inline=True)
        result_embed.add_field(name = "🧑‍💼 Người chơi", value=ctx.author.mention, inline=True)
        result_embed.add_field(
            name = "🎉 Trạng thái",
            value = "✅ Bạn **THẮNG**!" if win else "❌ Bạn **THUA**!",
            inline = False
        )

        await message.edit(embed=result_embed)
        
    @taixiu.error
    async def taixiu_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                description = f"⏳ Bạn cần chờ **{error.retry_after:.1f} giây** trước khi dùng lại lệnh này.",
                color = discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=5)


async def setup(bot):
    await bot.add_cog(TaiXiu(bot))
