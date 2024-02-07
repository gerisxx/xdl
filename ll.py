import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)
mailkey_role_id = 1189019273113391206
key_role_id = 1187581734599004170
keys = {}
mailkeys = {}
available_keys = [
    "premium-AB11111aAAA", "premium-CD22222bBBB", "premium-EF33333cCCC", "premium-GH44444dDDD",
    "premium-IJ55555eEEE", "premium-KL66666fFFF", "premium-MN77777gGGG", "premium-OP88888hHHH",
    "premium-QR99999iIII", "premium-ST00000jJJJ", "premium-UV11111kKKK", "premium-WX22222lLLL",
    "premium-YZ33333mMMM", "premium-AB44444nNNN", "premium-CD55555oOOO", "premium-EF66666pPPP",
    "premium-GH77777qQQQ", "premium-IJ88888rRRR", "premium-KL99999sSSS", "premium-MN00000tTTT",
    "premium-OP11111uUUU", "premium-QR22222vVVV", "premium-ST33333wWWW", "premium-UV44444xXXX",
    "premium-WX55555yYYY", "premium-YZ66666zZZZ", "premium-AB77777aAAA", "premium-CD88888bBBB",
    "premium-EF99999cCCC", "premium-GH00000dDDD", "premium-IJ11111eEEE", "premium-KL22222fFFF",
    "premium-MN33333gGGG", "premium-OP44444hHHH", "premium-QR55555iIII", "premium-ST66666jJJJ",
    "premium-UV77777kKKK", "premium-WX88888lLLL", "premium-YZ99999mMMM", "premium-AB00000nNNN",
    "premium-CD11111oOOO", "premium-EF22222pPPP", "premium-GH33333qQQQ", "premium-IJ44444rRRR",
    "premium-KL55555sSSS", "premium-MN66666tTTT", "premium-OP77777uUUU", "premium-QR88888vVVV",
    "premium-ST99999wWWW", "premium-UV00000xXXX", "premium-WX11111yYYY", "premium-YZ22222zZZZ",
    "premium-AB33333aAAA", "premium-CD44444bBBB", "premium-EF55555cCCC", "premium-GH66666dDDD",
    "premium-IJ77777eEEE", "premium-KL88888fFFF", "premium-MN99999gGGG", "premium-OP00000hHHH",
    "premium-QR11111iIII", "premium-ST22222jJJJ", "premium-UV33333kKKK", "premium-WX44444lLLL",
    "premium-YZ55555mMMM", "premium-AB66666nNNN", "premium-CD77777oOOO", "premium-EF88888pPPP",
    "premium-GH99999qQQQ", "premium-IJ00000rRRR", "premium-KL11111sSSS", "premium-MN22222tTTT",
    "premium-OP33333uUUU", "premium-QR44444vVVV", "premium-ST55555wWWW", "premium-UV66666xXXX",
    "premium-WX77777yYYY", "premium-YZ88888zZZZ", "premium-AB99999aAAA", "premium-CD00000bBBB",
    "premium-EF11111cCCC", "premium-GH22222dDDD", "premium-IJ33333eEEE", "premium-KL44444fFFF",
    "premium-MN55555gGGG", "premium-OP66666hHHH", "premium-QR77777iIII", "premium-ST88888jJJJ",
    "premium-UV99999kKKK", "premium-WX12345lLLL", "premium-YZ23456mMMM", "premium-AB34567nNNN",
    "premium-CD45678oOOO", "premium-EF56789pPPP", "premium-GH67890qQQQ", "premium-IJ78901rRRR",
    "premium-KL89012sSSS", "premium-MN90123tTTT", "premium-OP01234uUUU", "premium-QR12345vVVV",
    "premium-ST23456wWWW", "premium-UV34567xXXX", "premium-WX45678yYYY", "premium-YZ56789zZZZ",
    "premium-AB67890aAAA", "premium-CD78901bBBB", "premium-EF89012cCCC", "premium-GH90123dDDD",
    "premium-IJ01234eEEE", "premium-KL12345fFFF", "premium-MN23456gGGG", "premium-OP34567hHHH",
    "premium-QR45678iIII", "premium-ST56789jJJJ", "premium-UV67890kKKK", "premium-WX78901lLLL",
    "premium-YZ89012mMMM", "premium-AB90123nNNN", "premium-CD01234oOOO", "premium-EF12345pPPP",
    "premium-GH23456qQQQ", "premium-IJ34567rRRR", "premium-KL45678sSSS", "premium-MN56789tTTT",
    "premium-OP67890uUUU", "premium-QR78901vVVV", "premium-ST89012wWWW", "premium-UV90123xXXX",
    "premium-WX01234yYYY", "premium-YZ12345zZZZ", "premium-AB23456aAAA", "premium-CD34567bBBB",
    "premium-EF45678cCCC", "premium-GH56789dDDD", "premium-IJ67890eEEE", "premium-KL78901fFFF",
    "premium-MN89012gGGG", "premium-OP90123hHHH", "premium-QR01234iIII", "premium-ST12345jJJJ",
    "premium-UV23456kKKK", "premium-WX34567lLLL", "premium-YZ45678mMMM", "premium-AB56789nNNN",
    "premium-CD67890oOOO", "premium-EF78901pPPP", "premium-GH89012qQQQ", "premium-IJ90123rRRR",
    "premium-KL01234sSSS", "premium-MN12345tTTT", "premium-OP23456uUUU", "premium-QR34567vVVV",
    "premium-ST45678wWWW", "premium-UV56789xXXX", "premium-WX67890yYYY", "premium-YZ78901zZZZ",
    "premium-AB90123aAAA", "premium-CD01234bBBB", "premium-EF12345cCCC", "premium-GH23456dDDD",
    "premium-IJ34567eEEE", "premium-KL45678fFFF", "premium-MN56789gGGG", "premium-OP67890hHHH",
    "premium-QR78901iIII", "premium-ST89012jJJJ", "premium-UV90123kKKK", "premium-WX01234lLLL",
    "premium-YZ12345mMMM", "premium-AB23456nNNN", "premium-CD34567oOOO", "premium-EF45678pPPP",
    "premium-GH56789qQQQ", "premium-IJ67890rRRR", "premium-KL78901sSSS", "premium-MN89012tTTT",
    "premium-OP90123uUUU", "premium-QR01234vVVV", "premium-ST12345wWWW", "premium-UV23456xXXX",
    "premium-WX34567yYYY", "premium-YZ45678zZZZ", "premium-AB56789aAAA", "premium-CD67890bBBB",
    "premium-EF78901cCCC", "premium-GH89012dDDD", "premium-IJ90123eEEE", "premium-KL01234fFFF",
    "premium-MN12345gGGG", "premium-OP23456hHHH", "premium-QR34567iIII", "premium-ST45678jJJJ",
    "premium-UV56789kKKK", "premium-WX67890lLLL", "premium-YZ78901mMMM", "premium-AB90123nNNN",
    "premium-CD01234oOOO", "premium-EF12345pPPP", "premium-GH23456qQQQ", "premium-IJ34567rRRR",
    "premium-KL45678sSSS", "premium-MN56789tTTT", "premium-OP67890uUUU", "premium-QR78901vVVV",
    "premium-ST89012wWWW", "premium-UV90123xXXX", "premium-WX01234yYYY", "premium-YZ12345zZZZ",
    "premium-AB23456aAAA", "premium-CD34567bBBB", "premium-EF45678cCCC", "premium-GH56789dDDD",
    "premium-IJ67890eEEE", "premium-KL78901fFFF", "premium-MN89012gGGG", "premium-OP90123hHHH",
    "premium-QR01234iIII", "premium-ST12345jJJJ", "premium-UV23456kKKK", "premium-WX34567lLLL",
    "premium-YZ45678mMMM", "premium-AB56789nNNN", "premium-CD67890oOOO", "premium-EF78901pPPP",
    "premium-GH89012qQQQ", "premium-IJ90123rRRR", "premium-KL01234sSSS", "premium-MN12345tTTT",
    "premium-OP23456uUUU", "premium-QR34567vVVV", "premium-ST45678wWWW", "premium-UV56789xXXX",
    "premium-WX67890yYYY", "premium-YZ78901zZZZ", "premium-AB90123aAAA", "premium-CD01234bBBB",
    "premium-EF12345cCCC", "premium-GH23456dDDD", "premium-IJ34567eEEE", "premium-KL45678fFFF",
    "premium-MN56789gGGG", "premium-OP67890hHHH", "premium-QR78901iIII", "premium-ST89012jJJJ",
    "premium-UV90123kKKK", "premium-WX01234lLLL", "premium-YZ12345mMMM", "premium-AB23456nNNN",
    "premium-CD34567oOOO", "premium-EF45678pPPP", "premium-GH56789qQQQ", "premium-IJ67890rRRR",
    "premium-KL78901sSSS", "premium-MN89012tTTT", "premium-OP90123uUUU", "premium-QR01234vVVV",
    "premium-ST12345wWWW", "premium-UV23456xXXX", "premium-WX34567yYYY", "premium-YZ45678zZZZ",
    "premium-AB56789aAAA", "premium-CD67890bBBB", "premium-EF78901cCCC", "premium-GH89012dDDD",
    "premium-IJ90123eEEE", "premium-KL01234fFFF", "premium-MN12345gGGG", "premium-OP23456hHHH",
    "premium-QR34567iIII", "premium-ST45678jJJJ", "premium-UV56789kKKK", "premium-WX67890lLLL",
    "premium-YZ78901mMMM", "premium-AB90123nNNN", "premium-CD01234oOOO", "premium-EF12345pPPP",
    "premium-GH23456qQQQ", "premium-IJ34567rRRR", "premium-KL45678sSSS", "premium-MN56789tTTT",
    "premium-OP67890uUUU", "premium-QR78901vVVV", "premium-ST89012wWWW", "premium-UV90123xXXX",
    "premium-WX01234yYYY", "premium-YZ12345zZZZ", "premium-AB23456aAAA", "premium-CD34567bBBB",
    "premium-EF45678cCCC", "premium-GH56789dDDD", "premium-IJ67890eEEE"
]

mailavailable_keys = [
    'Mailbox-av932j9SCni21', 'Mailbox-jk872hJFpwo54', 'Mailbox-op765nKJdwq87', 'Mailbox-bh873nMCzqp29',
    'Mailbox-cd901qPLzxc33', 'Mailbox-vb786mNKxzc22', 'Mailbox-rf635dMZpoi88', 'Mailbox-lm347bXLxpo09',
    'Mailbox-qn982pKLzxc56', 'Mailbox-az861qPWxco98', 'Mailbox-po753cJNxdq21', 'Mailbox-bv297xLKpio64',
    'Mailbox-oi873pPWdzc37', 'Mailbox-mn345bZKxcv09', 'Mailbox-uf753mKLzxc91', 'Mailbox-kj298qPLkmd34',
    'Mailbox-gh902bXLxvz67', 'Mailbox-qp764mNKxcv20', 'Mailbox-fd823pKWpoi45', 'Mailbox-nb328bXLxpo12',
    'Mailbox-xc987mKLzxc34', 'Mailbox-lo523qPLmnd67', 'Mailbox-ws294bXLxzc89', 'Mailbox-ht864mNKxcv23',
    'Mailbox-pq573pKWpoi76', 'Mailbox-zx298bXLxpo45', 'Mailbox-lk234mKLzxc78', 'Mailbox-oi837qPLmnd90',
    'Mailbox-bv239bXLxzc43', 'Mailbox-er753mNKxcv65', 'Mailbox-gh892pKWpoi34', 'Mailbox-jk762bXLxpo98',
    'Mailbox-cv342mKLzxc12', 'Mailbox-op732qPLmnd56', 'Mailbox-xz965bXLxzc78', 'Mailbox-lo762mNKxcv43',
    'Mailbox-ht973pKWpoi21', 'Mailbox-rf876bXLxpo65', 'Mailbox-mn324mKLzxc98', 'Mailbox-az761qPLmnd54',
    'Mailbox-fd293bXLxzc87', 'Mailbox-qp765mNKxcv32', 'Mailbox-ws987pKWpoi65', 'Mailbox-er642bXLxpo98',
    'Mailbox-nb237mKLzxc12', 'Mailbox-gh924qPLmnd35', 'Mailbox-zx762bXLxzc78', 'Mailbox-lk345mNKxcv21',
    'Mailbox-oi762pKWpoi98', 'Mailbox-bv328bXLxpo54', 'Mailbox-jk876mKLzxc32', 'Mailbox-cv236qPLmnd78',
    'Mailbox-op975bXLxzc65', 'Mailbox-xz765mNKxcv21', 'Mailbox-lo328pKWpoi54', 'Mailbox-ht762bXLxpo98',
    'Mailbox-rf452mKLzxc32', 'Mailbox-mn753qPLmnd65', 'Mailbox-az762bXLxzc98', 'Mailbox-fd328mNKxcv21',
    'Mailbox-qp765pKWpoi54', 'Mailbox-ws237bXLxpo89', 'Mailbox-er762mKLzxc34', 'Mailbox-nb328qPLmnd67',
    'Mailbox-gh976bXLxzc12', 'Mailbox-zx328mNKxcv45', 'Mailbox-lk762pKWpoi98', 'Mailbox-oi328bXLxpo76',
    'Mailbox-bv765mKLzxc43', 'Mailbox-jk328qPLmnd65', 'Mailbox-cv762bXLxzc98', 'Mailbox-op328mNKxcv54',
    'Mailbox-xz765pKWpoi32', 'Mailbox-lo328bXLxpo65', 'Mailbox-ht762mKLzxc98', 'Mailbox-rf328qPLmnd54',
    'Mailbox-mn765bXLxzc32', 'Mailbox-az328mNKxcv65', 'Mailbox-fd765pKWpoi98', 'Mailbox-qp328bXLxpo76',
    'Mailbox-ws762mKLzxc43', 'Mailbox-er328qPLmnd65', 'Mailbox-nb765bXLxzc98', 'Mailbox-gh328mNKxcv54',
    'Mailbox-zx765pKWpoi32', 'Mailbox-lk328bXLxpo65', 'Mailbox-oi762mKLzxc98', 'Mailbox-bv328qPLmnd54',
    'Mailbox-jk765bXLxzc32', 'Mailbox-cv328mNKxcv65', 'Mailbox-op762pKWpoi98', 'Mailbox-xz328bXLxpo76',
    'Mailbox-lo765mKLzxc43', 'Mailbox-ht328qPLmnd65', 'Mailbox-rf762bXLxzc98', 'Mailbox-mn328mNKxcv54',
    'Mailbox-az765pKWpoi32', 'Mailbox-fd328bXLxpo65', 'Mailbox-qp762mKLzxc98', 'Mailbox-ws328qPLmnd54'
]



@bot.command()
async def key(ctx, key_type):
    author = ctx.author

    if key_type == 'premium':
        role = discord.utils.get(ctx.guild.roles, id=key_role_id)
        available = available_keys
        user_keys = keys
        sent_message = "Your Key Has Been Sent In DMs"

    elif key_type == 'mailbox':
        role = discord.utils.get(ctx.guild.roles, id=mailkey_role_id)
        available = mailavailable_keys
        user_keys = mailkeys
        sent_message = "Your Mail Key Has Been Sent In DMs"

    else:
        await ctx.send("Invalid key type.")
        return

    if role in author.roles:
        if author.id in user_keys:
            key = user_keys[author.id]
            response_embed = discord.Embed(
                title="Check Your DMs",
                description=sent_message,
                color=139576
            )
            await ctx.send(embed=response_embed)

            try:
                embed = discord.Embed(
                    title="Save Your Key!",
                    description=f"```{key}```",
                    color=0x139576
                )
                await author.send(embed=embed)
            except discord.Forbidden:
                response_embed = discord.Embed(
                    title="Enable Your DMs Privacy!",
                    description="Please enable your DMs to receive the key.",
                    color=139576,
                    image="https://cdn.discordapp.com/attachments/1086494473846001694/1190084099008905377/image_15.png?ex=65a0832f&is=658e0e2f&hm=dc14e8e26285e13c6f5cf12544f84c0bdd1191fb2b7c0466b83ee1df1d67a9d6&"
                )
                await ctx.send(embed=response_embed)
        else:
            if available:
                key = available.pop()
                user_keys[author.id] = key
                try:
                    embed = discord.Embed(
                        title="Save Your Key!",
                        description=f"```{key}```",
                        color=0x139576
                    )
                    await author.send(embed=embed)
                    
                    response_embed = discord.Embed(
                        title="Check Your DMs",
                        description=sent_message,
                        color=139576
                    )
                    await ctx.send(embed=response_embed)
                except discord.Forbidden:
                    response_embed = discord.Embed(
                        title="Enable Your DMs Privacy!",
                        description="Please enable your DMs to receive the key.",
                        color=139576,
                        image="https://cdn.discordapp.com/attachments/1086494473846001694/1190084099008905377/image_15.png?ex=65a0832f&is=658e0e2f&hm=dc14e8e26285e13c6f5cf12544f84c0bdd1191fb2b7c0466b83ee1df1d67a9d6&"
                    )
                    await ctx.send(embed=response_embed)
            else:
                response_embed = discord.Embed(
                    title="No Keys Available",
                    description="Apologies, there are no keys available at the moment.",
                    color=139576
                )
                await ctx.send(embed=response_embed)
    else:
        response_embed = discord.Embed(
            title="Check Your DMs",
            description=sent_message,
            color=139576
        )
        await ctx.send(embed=response_embed)
bot.run('MTE4Nzk4Mjg5NTE2MDIzODA4MA.GRgw_K.U2L_sVobQc4IURG4jF_Hf48-RPuMRhrqKhYz9c')
