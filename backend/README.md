# Backend

个人网站中 A 股分位观测站模块的后端服务和定时爬虫。

## 目录

- `common/`：环境变量和 MySQL 连接配置。
- `web/`：FastAPI 只读接口，不请求外部数据，也不写入估值数据。
- `crawler/`：独立的丹卷基金数据抓取和 MySQL 写入程序。
- `init.sql`：数据库初始化脚本。

## 本地启动 API

在 `backend` 目录创建 `.env`，填写对应数据库配置。程序会自动读取该文件；生产环境不要把真实密码提交到 Git。然后执行：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PYTHONPATH = (Get-Location).Path
.\.venv\Scripts\python.exe -m uvicorn web.main:app --host 127.0.0.1 --port 8000 --reload
```

API 文档地址：`http://127.0.0.1:8000/docs`。

## 爬虫

只校验接口、不写数据库：

```powershell
$env:PYTHONPATH = (Get-Location).Path
.\.venv\Scripts\python.exe -m crawler.fetch_val --dry-run
```

正式写入：

```powershell
.\.venv\Scripts\python.exe -m crawler.fetch_val
```

生产环境应将数据库密码放在项目目录之外的受限环境变量文件中，并分别为 Web 服务和爬虫配置只读、读写数据库账号。
