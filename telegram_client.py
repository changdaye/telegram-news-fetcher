import os
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest
from datetime import datetime, timedelta
from typing import List

class TelegramMessageFetcher:
    """Telegram消息获取器，使用用户账号获取群组消息"""
    
    def __init__(self):
        # 从环境变量获取API配置
        self.api_id = os.getenv('TELEGRAM_API_ID')
        self.api_hash = os.getenv('TELEGRAM_API_HASH')
        self.phone = os.getenv('TELEGRAM_PHONE')
        
        # 初始化客户端
        self.client = TelegramClient('news_session', self.api_id, self.api_hash)
    
    async def start(self):
        """启动Telegram客户端"""
        await self.client.start(phone=self.phone)
        print("Telegram客户端已启动")
    
    async def join_group(self, group_link: str):
        """加入指定的Telegram群组
        
        参数:
            group_link: 群组邀请链接或用户名
        """
        try:
            await self.client.join_chat(group_link)
            print(f"成功加入群组: {group_link}")
        except Exception as e:
            print(f"加入群组失败: {str(e)}")
    
    async def fetch_messages(self, chat_id: int, hours_window: int = 10) -> List[str]:
        """获取指定群组的历史消息
        
        参数:
            chat_id: 群组ID
            hours_window: 获取过去多少小时的消息
            
        返回:
            消息文本列表
        """
        messages = []
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=hours_window)
        
        try:
            # 获取群组实体
            chat = await self.client.get_entity(chat_id)
            
            # 获取消息历史
            async for message in self.client.iter_messages(
                chat,
                offset_date=end_time,
                reverse=True
            ):
                if message.date < start_time:
                    break
                if message.text:
                    messages.append(message.text)
                    
            return messages
        except Exception as e:
            print(f"获取消息失败: {str(e)}")
            return []
    
    async def stop(self):
        """停止Telegram客户端"""
        await self.client.disconnect()
        print("Telegram客户端已停止")

if __name__ == '__main__':
    import asyncio
    
    async def main():
        fetcher = TelegramMessageFetcher()
        await fetcher.start()
        
        # 示例：加入群组并获取消息
        group_id = int(os.getenv('TELEGRAM_GROUP_ID'))
        messages = await fetcher.fetch_messages(group_id)
        print(f"获取到 {len(messages)} 条消息")
        
        await fetcher.stop()
    
    asyncio.run(main())