# ChatVivo

一个基于vivo GPT API的智能聊天机器人Web应用。

## 功能特点

- 简洁美观的聊天界面
- 支持实时对话
- 自动滚动到最新消息
- 支持回车发送消息
- 输入框自动调整高度

## 技术栈

- 后端：Python Flask
- 前端：HTML, CSS, JavaScript
- API：vivo GPT API

## 安装步骤

1. 克隆项目
```bash
git clone https://github.com/your-username/chatVivo.git
cd chatVivo
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置API密钥
在`app.py`中配置您的vivo GPT API密钥：
```python
APP_ID = 'your_app_id'
APP_KEY = 'your_app_key'
```

4. 运行应用
```bash
python app.py
```

5. 访问应用
打开浏览器访问：`http://localhost:5000`

## 项目结构

```
chatVivo/
├── app.py              # 主应用文件
├── auth_util.py        # 认证工具
├── requirements.txt    # 依赖文件
├── static/
│   ├── css/
│   │   └── style.css  # 样式文件
│   └── js/
│       └── script.js  # 前端脚本
└── templates/
    └── index.html     # 主页面模板
```

## 注意事项

- 请确保您有有效的vivo GPT API密钥
- 建议在开发环境中使用，生产环境需要添加适当的安全措施
- 请遵守vivo GPT API的使用条款和限制

## 许可证

MIT License 