# -*- coding: utf-8 -*-
# Copyright (c) 2026 Shensist Art Intelligence Studio (AIS)
# License: GNU AGPLv3
# Project: MelodyLight AI: 山海寻宝大乐园

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="MelodyLight AI - Hardened Edition")

# 物理路径定位 (工业级动态解析)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(BASE_DIR, "assets")

# 核心：确保 /assets/ 路径被正确映射，供 HTML 相对路径使用
app.mount("/assets", StaticFiles(directory=ASSETS_PATH), name="assets")

@app.get("/")
async def read_index():
    # 根路径直接返回 index.html
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

# 备用：强制背景图路由（如果 CSS 动态加载出现路径偏移，此路由可保底）
@app.get("/assets/beijing2.webp")
async def get_bg():
    return FileResponse(os.path.join(ASSETS_PATH, "beijing2.webp"))

# 保留 /interface/ 以向下兼容旧链接
@app.get("/interface/")
async def read_interface():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
