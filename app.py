from loader import bot, AuthMiddleware


async def on_shutdown(dp):
    await bot.close()

    
if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    dp.middleware.setup(AuthMiddleware())
    executor.start_polling(dp,
                           on_shutdown=on_shutdown,
                           skip_updates=True)