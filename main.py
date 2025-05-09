import os
from datetime import datetime
from telegram_fetcher import fetch_telegram_messages
from llm_processor import NewsProcessor

async def generate_daily_report():
    """
    生成每日新闻简报的主流程
    
    返回:
        tuple: 包含简报和分析报告的元组
    """
    # 获取过去10小时的消息（20:00-次日6:00）
    messages = await fetch_telegram_messages(hours_window=10)
    
    # 消息分类处理
    categorized = NewsProcessor.categorize_messages(messages)
    
    # 生成简报
    briefing = NewsProcessor.generate_briefing(categorized)
    
    # 生成深度分析
    analysis = NewsProcessor.generate_analysis(briefing)
    
    # 保存报告
    timestamp = datetime.now().strftime('%Y%m%d%H%M')
    with open(f'reports/{timestamp}_report.md', 'w') as f:
        f.write(f'# 每日新闻简报\n\n{briefing}\n\n## 深度分析\n{analysis}')
    
    return briefing, analysis

if __name__ == '__main__':
    import asyncio
    asyncio.run(generate_daily_report())