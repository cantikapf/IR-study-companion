import asyncio
import edge_tts

TEXT = '''Pernahkah kamu bertanya, kenapa para pemimpin dunia sering terlihat begitu keras kepala dan curiga satu sama lain?
Sebagian orang mengira perdamaian dunia itu mudah dicapai jika semua orang berniat baik.
Namun Hans Morgenthau, bapak Realisme Klasik, punya jawaban yang jauh lebih dingin.
Bagi kaum realis, politik internasional bukan panggung moral, melainkan arena perjuangan kekuasaan yang berakar dari sifat dasar manusia.
Di bawah sistem anarki dunia tanpa polisi global, setiap negara dipaksa berdiri di atas kaki sendiri.
Kepentingan nasional selalu dihitung dengan satu mata uang utama, yaitu kekuasaan.
Memahami realisme bukan berarti kita mencintai perang, melainkan cara kita melihat dunia apa adanya, bukan sebagaimana yang kita inginkan.'''

# Sentences with rough timestamp allocation for 44.6 seconds
# 1: 00:00 - 00:06 (6s)
# 2: 00:06 - 00:12 (6s)
# 3: 00:12 - 00:18 (6s)
# 4: 00:18 - 00:26 (8s)
# 5: 00:26 - 00:32 (6s)
# 6: 00:32 - 00:38 (6s)
# 7: 00:38 - 00:44 (6s)

srt_content = '''1
00:00:00,500 --> 00:00:06,000
Pernahkah kamu bertanya, kenapa para pemimpin dunia
sering terlihat begitu curiga satu sama lain?

2
00:00:06,000 --> 00:00:12,000
Sebagian orang mengira perdamaian dunia itu mudah,
jika semua pihak berniat baik.

3
00:00:12,000 --> 00:00:18,500
Namun Hans Morgenthau, bapak Realisme Klasik,
punya jawaban yang jauh lebih dingin.

4
00:00:18,500 --> 00:00:26,500
Politik internasional bukan panggung moral,
melainkan arena perjuangan kekuasaan manusia.

5
00:00:26,500 --> 00:00:32,500
Di bawah anarki global tanpa polisi dunia,
setiap negara dipaksa berdiri sendiri (Self-Help).

6
00:00:32,500 --> 00:00:38,500
Kepentingan nasional selalu dihitung dengan
satu mata uang utama: KEKUASAAN (Power).

7
00:00:38,500 --> 00:00:44,500
Realisme bukan mencintai perang, melainkan
melihat dunia apa adanya, bukan yang kita inginkan.
'''

with open('simulation/assets/subtitles.srt', 'w', encoding='utf-8') as f:
    f.write(srt_content)
print('SRT created successfully!')
