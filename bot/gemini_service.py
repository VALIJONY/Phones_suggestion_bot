import os
from google import genai

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-2.5-flash"

SYSTEM_PROMPT = """
Sen telefon do'konining yordamchi botisan. Foydalanuvchi savol beradi,
sen unga quyidagi bazadagi telefonlar ro'yxatidan mos variantlarni
tavsiya qilasan.

Qoidalar:
- Faqat berilgan baza ichidan telefon tavsiya qil, o'zingdan telefon o'ylab topma.
- Narxni so'm ko'rinishida, tushunarli formatda yoz (masalan: 5 500 000 so'm).
- Javobni o'zbek tilida, do'stona va qisqa yoz.
- Agar mos telefon topilmasa, buni halol ayt va yaqin variant taklif qil.
"""


def ask_gemini(user_question: str, phones_data: str) -> str:
    """
    Foydalanuvchi savolini va bazadagi telefonlar ro'yxatini Gemini'ga
    yuborib, tabiiy javob oladi.
    """
    prompt = f"""{SYSTEM_PROMPT}

Bazadagi telefonlar ro'yxati:
{phones_data}

Foydalanuvchi savoli: {user_question}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"Kechirasiz, xatolik yuz berdi. Qaytadan urinib ko'ring. ({e})"