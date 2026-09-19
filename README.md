# Telegram News Fetcher & LLM Daily Digest

基于 **Telethon** 与 **OpenAI API** 的 Telegram 群组/频道资讯异步抓取、智能分类与每日简报生成工具。

项目支持设置自定义监控时间窗口，定时从 Telegram 订阅源提取未读消息，利用大模型自动按领域归类并生成包含深度分析的 Markdown 晨报。

---

## ✨ 核心特性

- **异步高效抓取**：基于 Telethon MTProto 协议直接与 Telegram API 通信，支持指定历史时间跨度（默认抓取最近 10 小时消息）。
- **智能领域分流**：根据关键词与语义将海量消息自动归入**财经市场**、**地缘军事**与**综合资讯**等板块。
- **大模型简报与洞察**：调用 OpenAI 模型对分流消息进行智能摘要，并输出次日关键观察点与深度影响分析。
- **自动归档落地**：生成的完整日报自动输出为结构化 Markdown 文档，归档保存在 `reports/` 目录下（如 `202605090600_report.md`）。
- **定时任务就绪**：内置 `cronjob.sh` 脚本，方便配置在服务器或本地 Crontab 中无人值守运行。

---

## 📂 项目结构

```text
.
├── main.py              # 全流程入口：抓取 -> 分类 -> 大模型生成 -> 导出报告
├── telegram_fetcher.py  # 异步消息抓取核心模块（支持时间窗口筛选）
├── llm_processor.py     # OpenAI 分类器、简报与深度分析生成引擎
├── telegram_client.py   # 交互式 Telegram 会话客户端（用于初次登录认证）
├── cronjob.sh           # 定时任务执行脚本
├── requirements.txt     # Python 依赖清单
└── reports/             # 自动生成的 Markdown 日报归档目录
```

---

## 🚀 快速开始

### 1. 安装依赖

推荐在 Python 3.8+ 虚拟环境下运行：

```bash
git clone https://github.com/changdaye/telegram-news-fetcher.git
cd telegram-news-fetcher

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置环境变量

在根目录下创建 `.env` 文件：

```env
# Telegram API 配置（从 https://my.telegram.org 获取）
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash
TELEGRAM_PHONE=+8613800000000
TELEGRAM_GROUP_ID=-1001234567890

# OpenAI API 配置
OPENAI_API_KEY=sk-...
```

### 3. 首次认证与运行

首次运行需要验证 Telegram 登录凭据（控制台会提示输入验证码）：

```bash
# 首次登录认证与连通性测试
python telegram_client.py

# 执行一次全流程日报生成
python main.py
```

### 4. 配置定时任务（可选）

通过 Crontab 设置每天清晨 06:00 自动生成夜间资讯总结：

```bash
crontab -e
# 添加以下内容（按实际路径调整）：
0 6 * * * /bin/bash /path/to/telegram-news-fetcher/cronjob.sh
```

---

## 📄 开源许可

MIT License

