import os
import yt_dlp


def download_youtube_audio(url, output_path="./downloads", cookie_path="cookies.txt"):
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
        "quiet": False,
        "no_warnings": False,
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    }

    # 可选：如果 cookies.txt 存在就加载（用于你有权限访问的内容）
    if cookie_path and os.path.isfile(cookie_path):
        ydl_opts["cookiefile"] = cookie_path
        print(f"已加载 Cookie：{cookie_path}")
    else:
        print("未找到 Cookie 文件，按无登录方式下载（如需登录请放置 cookies.txt）。")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"正在准备下载: {url}")
            ydl.download([url])
            print("\n下载并转换成功！")
    except Exception as e:
        print(f"\n下载失败，错误信息: {e}")
        print("提示：可尝试更新：pip install -U yt-dlp")


if __name__ == "__main__":
    video_url = input("请输入视频链接: ").strip()
    if not video_url:
        print("链接不能为空。")
    else:
        download_youtube_audio(video_url)
