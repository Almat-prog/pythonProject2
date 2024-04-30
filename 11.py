import librosa
import soundfile as sf

# Загрузка аудиофайла
def load_audio(file_path):
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    return audio_data, sample_rate

# Получение основной информации об аудиофайле
def get_audio_info(audio_data, sample_rate):
    duration = librosa.get_duration(y=audio_data, sr=sample_rate)
    return duration, sample_rate

# Изменение громкости аудиофайла
def change_volume(audio_data, volume_factor):
    return audio_data * volume_factor

# Сохранение измененного аудиофайла
def save_audio(file_path, audio_data, sample_rate):
    sf.write(file_path, audio_data, sample_rate)

# Основной код приложения
if __name__ == "__main__":
    # Загрузка аудиофайла
    audio_file_path = r"C:\Users\Asus\Desktop\Xcho - Мир На Двоих.mp3"
    audio_data, sample_rate = load_audio(audio_file_path)

    # Получение информации об аудиофайле
    duration, sample_rate = get_audio_info(audio_data, sample_rate)
    print(f"Длительность аудиофайла: {duration} секунд")
    print(f"Частота дискретизации: {sample_rate} Гц")

    # Применение эффекта изменения громкости
    volume_factor = 0.5  # Уменьшение громкости вдвое
    modified_audio_data = change_volume(audio_data, volume_factor)

    # Сохранение измененного аудиофайла
    modified_audio_file_path = "modified_audio.wav"
    save_audio(modified_audio_file_path, modified_audio_data, sample_rate)
