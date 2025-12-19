import os
import yt_dlp


def download_media(url, mode="video", cookie_path="cookies.txt", output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)

    opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "nocheckcertificate": True,
        "quiet": False,
        "no_warnings": False,
        "user_agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    }

    if cookie_path and os.path.isfile(cookie_path):
        opts["cookiefile"] = cookie_path
        print("使用 cookie：", cookie_path)
    else:
        print("未找到 cookie，按未登录方式处理")

    if mode == "audio":
        print("模式：音频（mp3 192k）")
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
    else:
        print("模式：视频（尽量最高画质）")
        opts["format"] = "bestvideo*+bestaudio/best"

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            print("开始：", url)
            ydl.download([url])
            print("完成，保存到：", output_dir)
    except Exception as e:
        print("出错：", e)


if __name__ == "__main__":
    url = input("输入链接：").strip()
    if not url:
        print("链接不能为空")
        raise SystemExit

    x = input("选模式：1=视频  2=音频 > ").strip()
    mode = "audio" if x == "2" else "video"
    download_media(url, mode=mode)


