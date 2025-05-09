import os
import openai
from typing import List, Dict

openai.api_key = os.getenv('OPENAI_API_KEY')

class NewsProcessor:
    """
    新闻处理类，用于对原始消息进行分类、摘要生成和深度解读
    """
    
    @staticmethod
    def categorize_messages(messages: List[str]) -> Dict[str, List[str]]:
        """
        对消息进行初步分类
        
        参数:
            messages: 原始消息列表
        
        返回:
            按类别分类的字典（财经/军事/其他）
        """
        categorized = {'finance': [], 'military': [], 'other': []}
        for msg in messages:
            if any(keyword in msg for keyword in ['股', '汇', '经济']):
                categorized['finance'].append(msg)
            elif any(keyword in msg for keyword in ['军演', '武器', '冲突']):
                categorized['military'].append(msg)
            else:
                categorized['other'].append(msg)
        return categorized

    @classmethod
    def generate_briefing(cls, categorized: Dict[str, List[str]]) -> str:
        """
        生成分类摘要简报
        
        参数:
            categorized: 分类后的消息字典
        
        返回:
            结构化摘要文本
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "将以下分类新闻生成结构化简报，包含重要事件和时间线"
            }, {
                "role": "user",
                "content": str(categorized)
            }]
        )
        return response.choices[0].message.content

    @classmethod
    def generate_analysis(cls, briefing: str) -> str:
        """
        生成深度分析报告
        
        参数:
            briefing: 摘要简报文本
        
        返回:
            包含趋势分析和影响评估的深度报告
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "对以下简报进行深度分析，指出潜在影响和发展趋势"
            }, {
                "role": "user",
                "content": briefing
            }]
        )
        return response.choices[0].message.content