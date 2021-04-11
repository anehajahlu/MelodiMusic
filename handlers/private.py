from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("AAMCBQADGQEAAQlEyGBzdiUGDPFCJMnfvxV6M7ry3_O8AAJaAgACBjGpVsrLEMler1z4-4b_cHQAAwEAB20AAzYDAAIeBA")
    await message.reply_text(
        f"""**Yuhuuuu Guys {bn} 🎵

Saya bisa memutar musik di panggilan suara grup Anda. Dikembangkan Oleh [Toni](https://t.me/BluueBlueSky).

Tambahkan saya ke grup Anda dengan cara salin username saya lalu invite. jangan lupa invite @MelodiAssistantBot dan nikmati musik dengan bebas!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Klik Disini Untuk Penjelasan Printah", url="https://telegra.ph/text-04-11-2")
                  ],[
                    InlineKeyboardButton(
                        "🐝 Pemilik", url="https://t.me/BluueBlueSky"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CandaAnda"
                    )
                 ],[ 
                    InlineKeyboardButton(
                        "⚡Tambahkan Ke Grup Anda⚡", url="https://t.me/MelodiMusic?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Melodi Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/CandaAnda")
                ]
            ]
        )
   )


