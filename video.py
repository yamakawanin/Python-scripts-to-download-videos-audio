import os
import yt_dlp


def download_video(url, cookie_path="cookies.txt", output_dir="downloads"):
    if not os.path.isfile(cookie_path):
        print(f"找不到 {cookie_path}，请把导出的 cookie 文件放到脚本同目录。")
        return

    os.makedirs(output_dir, exist_ok=True)

    opts = {
        "cookiefile": cookie_path,
        "format": "bestvideo+bestaudio/best",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "nocheckcertificate": True,
        "quiet": False,
        "no_warnings": False,
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            print("开始下载：", url)
            ydl.download([url])
            print("下载完成")
    except Exception as e:
        print("出错：", e)


if __name__ == "__main__":
    url = input("输入视频链接：").strip()
    if url:
        download_video(url)
    else:
        print("链接不能为空")

