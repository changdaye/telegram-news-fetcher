#!/bin/bash

# 进入项目目录
cd /Users/changdaye/TraeProjects/news

# 激活Python虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 执行主程序
python main.py

# 去激活虚拟环境
deactivate