from __future__ import annotations
import logging
from aiogram import Bot, Dispatcher


class Telegram:
    """
    A simple configurable Telegram bot, wrapped Aiogram.
    """
    __bot_token: str
    _bot: Bot
    _dp: Dispatcher

    def __init__(self, bot_token: str):
        self.__bot_token = bot_token
        self.set_logging()
        self._initiate_bot()
        self._initiate_dp()
        

    def set_logging(self, level: int = logging.INFO):
        """
        Set the logging.
        """
        logging.basicConfig(level=level)
        logging.debug("Initiated logging.")

    def _initiate_bot(self):
        self._bot = Bot(token=self.__bot_token)
        logging.debug("Initiated Telegram bot.")

    def _initiate_dp(self):
        self._dp = Dispatcher(self._bot)
        logging.debug("Initiated the dispatcher of Telegram bot.")

    def get_bot(self) -> Bot:
        """
        Get the instanced bot.
        """
        return self._bot

    def get_dp(self) -> Dispatcher:
        """
        Get the dispatcher of the instanced bot.
        """
        return self._dp

    async def start_polling(self):
        """
        Start polling. Returns the created task.
        """
        logging.info("MCDRTelegram: Start polling.")
        await self._dp.start_polling()  # type: ignore

    def stop_polling(self) -> None:
        """
        Stop polling.
        """
        logging.info("MCDRTelegram: Stop polling.")
        self._dp.stop_polling()  # type: ignore
    
    async def stop_bot(self) -> None:
        """
        Stop Bot.
        """
        logging.info("MCDRTelegram: Closed.")
        await self._bot.close()