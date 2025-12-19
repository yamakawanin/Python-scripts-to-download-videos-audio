# yt-dlp 简易下载脚本（视频 / 音频）

一个基于 **yt-dlp** 的 Python 下载脚本，支持  
-  **视频下载（尽量最高画质）**  
-  **音频下载（MP3，192kbps）**  
-  **Cookie 登录模式（适合需要登录的平台）**

适合个人学习、研究与非商业用途。

---

##  功能特性

- 支持视频 / 音频两种模式
- 自动调用 ffmpeg 转码音频
- 支持 cookies.txt 登录（绕过部分限制）
- 自动创建下载目录
- 命令行交互，使用简单

---

##  环境要求

- Python **3.9+**
- ffmpeg（需加入系统 PATH）
- yt-dlp

---

##  安装依赖

```bash
pip install -U yt-dlp
Windows
下载：https://ffmpeg.org/download.html
解压后将 bin 目录加入系统 PATH
```

## Cookie使用
- 某些网站（如 YouTube、Twitch 等）在未登录状态下会限制清晰度或下载。
- 获取 cookies.txt 方法
- 推荐使用浏览器插件：
- Chrome / Edge
- Get cookies.txt LOCALLY
- 导出后重命名为 cookies.txt，与脚本放在同一目录即可。
---
