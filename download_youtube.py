import yt_dlp

def download_youtube_video(url, resolution='best'):
    ydl_opts = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': '%(title)s.%(ext)s',  # ชื่อไฟล์ที่ต้องการดาวน์โหลด
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        print("ดาวน์โหลดวิดีโอสำเร็จ!")

if __name__ == "__main__":
    url = input("กรุณากรอก URL ของวิดีโอ YouTube: ")
    resolution = input("กรุณากรอกความละเอียดที่ต้องการ (เช่น 720, 1080): ")
    download_youtube_video(url, resolution)