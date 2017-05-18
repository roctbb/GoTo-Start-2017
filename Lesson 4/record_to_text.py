import pyaudio, wave, speechkit

FORMAT = pyaudio.paInt16  # глубина звука = 16 бит = 2 байта
CHANNELS = 1  # моно
RATE = 16000  # частота дискретизации - кол-во фреймов в секунду
CHUNK = 4000  # кол-во фреймов за один "запрос" к микрофону - тк читаем по кусочкам
RECORD_SECONDS = 5  # длительность записи

def record():
    audio = pyaudio.PyAudio()

    # открываем поток для чтения данных с устройства записи по умолчанию
    # и задаем параметры
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    result = b''  # список байтовых строк

    # для каждого "запроса"
    for i in range(0, RATE // CHUNK * RECORD_SECONDS):  # RATE // CHUNK - кол-во запросов в секунду
        data = stream.read(CHUNK)  # читаем строку из байт длиной CHUNK * FORMAT = 4000*2 байт
        result += data  # добавляем строку в список

    print("end recording")
    return result

def play(data):
    audio = pyaudio.PyAudio()

    # открываем поток для записи на устройство вывода - динамик - с такими же параметрами
    out_stream = audio.open(format=FORMAT, channels=CHANNELS,
                            rate=RATE, output=True)
    out_stream.write(data)
    out_stream.close()

data = record()

print(speechkit.record_to_text(data))


