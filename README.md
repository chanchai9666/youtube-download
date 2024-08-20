# youtube-download
download video youtube from url

<p class="has-line-data" data-line-start="0" data-line-end="3">ครั้งแรกให้ติดตั้ง<br>
pip install yt-dlp<br>
brew install ffmpeg (mac os)</p>
https://ffmpeg.org/download.html (windows)
<p class="has-line-data" data-line-start="5" data-line-end="9">run คำสั่ง<br>
python download_youtube.py<br>
-&gt;ใส่ url ของ youtube ที่ต้องการ<br>
-&gt;ใส่รายความละเอียด video ที่ต้องการ เช่น 720 , 1080</p>
<p class="has-line-data" data-line-start="10" data-line-end="13">กรณีไฟล์ไม่เป็น mp4 สามารถ แปลงไฟล์ได้<br>
ใช้คำสั่ง<br>
ffmpeg -i ชื่อไฟล์เก่า.webm -c:v libx264 -c:a aac ชื่อไฟล์ใหม่.mp4</p>