# Telegram 新闻消息抓取工具

这是一个用Python开发的Telegram群组消息抓取工具，可以自动获取指定群组的历史消息。

## 功能特点

- 支持加入Telegram群组
- 可配置消息获取时间窗口
- 异步处理，高效获取消息
- 支持环境变量配置

## 环境要求

- Python 3.7+
- Telethon
- python-dotenv

## 安装

1. 克隆仓库：
```bash
git clone https://github.com/changdaye/telegram-news-fetcher.git
cd telegram-news-fetcher
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

在项目根目录创建 `.env` 文件，添加以下配置：

```env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=your_phone_number
TELEGRAM_GROUP_ID=target_group_id
```

## 使用方法

运行主程序：

```bash
python telegram_client.py
```

## 许可证

MIT License