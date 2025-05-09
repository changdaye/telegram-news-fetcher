import os
import datetime
from telegram import Bot

async def fetch_telegram_messages(hours_window=10):
    """
    获取指定时间窗口内的Telegram群组消息
    
    参数:
        hours_window (int): 需要抓取的小时数（默认抓取过去10小时）
    
    返回:
        list: 包含消息文本的列表
    """
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=hours_window)

    messages = []
    async with bot:
        async for message in bot.get_chat_history(chat_id=chat_id):
            if message.date < start_time.replace(tzinfo=None):
                break
            if message.text:
                messages.append(message.text)
    return messages

if __name__ == '__main__':
    import asyncio
    print(asyncio.run(fetch_telegram_messages()))