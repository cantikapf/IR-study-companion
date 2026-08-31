import asyncio
import edge_tts

TEXT = '''Pernahkah kamu bertanya, kenapa para pemimpin dunia sering terlihat begitu keras kepala dan curiga satu sama lain?
Sebagian orang mengira perdamaian dunia itu mudah dicapai jika semua orang berniat baik.
Namun Hans Morgenthau, bapak Realisme Klasik, punya jawaban yang jauh lebih dingin.
Bagi kaum realis, politik internasional bukan panggung moral, melainkan arena perjuangan kekuasaan yang berakar dari sifat dasar manusia.
Di bawah sistem anarki dunia tanpa polisi global, setiap negara dipaksa berdiri di atas kaki sendiri.
Kepentingan nasional selalu dihitung dengan satu mata uang utama, yaitu kekuasaan.
Memahami realisme bukan berarti kita mencintai perang, melainkan cara kita melihat dunia apa adanya, bukan sebagaimana yang kita inginkan.'''

async def main():
    communicate = edge_tts.Communicate(TEXT, 'id-ID-ArdiNeural', rate='+0%')
    sub_maker = edge_tts.SubMaker()
    
    with open('simulation/assets/narration.mp3', 'wb') as f:
        async for chunk in communicate.stream():
            if chunk['type'] == 'audio':
                f.write(chunk['data'])
            elif chunk['type'] == 'WordBoundary':
                sub_maker.feed(chunk)
                
    with open('simulation/assets/subtitles.srt', 'w', encoding='utf-8') as f:
        f.write(sub_maker.get_srt())
        
    print('TTS and SRT successfully created!')

asyncio.run(main())
