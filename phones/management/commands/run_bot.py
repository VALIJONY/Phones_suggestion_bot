import os
import asyncio

from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher

from bot.handlers import router


class Command(BaseCommand):
    help = "Telegram botni ishga tushiradi"

    def handle(self, *args, **kwargs):
        asyncio.run(self.run_bot())

    async def run_bot(self):
        token = os.getenv("TELEGRAM_BOT_TOKEN")

        if not token:
            self.stdout.write(
                self.style.ERROR(
                    "TELEGRAM_BOT_TOKEN topilmadi. .env faylini tekshiring."
                )
            )
            return

        bot = Bot(token=token)
        dp = Dispatcher()
        dp.include_router(router)

        self.stdout.write(self.style.SUCCESS("Bot ishga tushdi..."))

        await dp.start_polling(bot)