from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from phones.models import Phone
from bot.gemini_service import ask_gemini

router = Router()


def get_phones_as_text() -> str:

    phones = Phone.objects.all()

    if not phones:
        return "Bazada hozircha telefon yo'q."

    lines = []
    for phone in phones:
        lines.append(
            f"- {phone.name} | Narxi: {phone.price:,} so'm | "
            f"RAM: {phone.ram} | Xotira: {phone.storage} | "
            f"Kamera: {phone.camera} | Batareya: {phone.battery}"
        )
    return "\n".join(lines)


@router.message(CommandStart())
async def start_command(message: Message):
    """
    /start buyrug'i - botni ishga tushirganda salomlashish.
    """
    welcome_text = (
        "Assalomu alekum! 👋\n\n"
        "Men telefon tavsiya qiluvchi botman. "
        "Menga qanday telefon kerakligini yozing, "
        "men sizga mos variantlarni tavsiya qilaman.\n\n"
        "Masalan:\n"
        "- Arzon telefon kerak, kamerasi yaxshi bo'lsin\n"
        "- 5 million so'mgacha bo'lgan telefon\n"
        "- iPhone bormi?\n"
    )
    await message.answer(welcome_text)


@router.message(F.text)
async def handle_message(message: Message):
    user_question = message.text

    await message.answer("Qidiryapman...")

    phones_data = get_phones_as_text()
    answer = ask_gemini(user_question, phones_data)

    await message.answer(answer)