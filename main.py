import asyncio
from aiogram import Bot,Dispatcher,F

from app.handlers import router
     


async def main():
    bot= Bot(token='7812729463:AAE4uVGLl1SR20GO9Wge6XHXwMXD18m338U')
    dp=Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')