# youtube-download
download video youtube from url

ครั้งแรกให้ติดตั้ง
  pip install yt-dlp
  brew install ffmpeg (mac os)
  

run คำสั่ง
python download_youtube.py
  ->ใส่ url ของ youtube ที่ต้องการ
  ->ใส่รายความละเอียด video ที่ต้องการ เช่น 720 , 1080
กรณีที่ 

กรณีไฟล์ไม่เป็น mp4 สามารถ แปลงไฟล์ได้
ใช้คำสั่ง
  ffmpeg -i ชื่อไฟล์เก่า.webm -c:v libx264 -c:a aac ชื่อไฟล์ใหม่.mp4
