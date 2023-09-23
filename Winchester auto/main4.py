from pyautogui import locateOnScreen, center, click, hotkey
from time import sleep
from configparser import ConfigParser

# Default values
delay_between_tries = 0.2
delay_after_succeding = 1
wait_after_click = 5  # Beklenecek süre (saniye) Ctrl+W'ye basıldıktan sonra
wait_before_next_loop = 3  # Bir sonraki döngüye geçmeden önce beklenecek süre (saniye)
max_retry_attempts = 5  # Maksimum yeniden deneme sayısı

# If the config has values, use those instead
config = ConfigParser()
config.read('settings.ini')

if config.has_option("SETTINGS", "delay_between_tries"):
    delay_between_tries = float(config["SETTINGS"]["delay_between_tries"])

if config.has_option("SETTINGS", "delay_after_succeding"):
    delay_after_succeding = float(config["SETTINGS"]["delay_after_succeding"])

while True:
    retry_attempts = 0

    while retry_attempts < max_retry_attempts:
        sleep(delay_between_tries)

        download_location2 = locateOnScreen("reference2.png")

        if download_location2 is not None:
            download_point_location2 = center(download_location2)
            click(download_point_location2.x, download_point_location2.y)

            sleep(delay_after_succeding)

            download_location = locateOnScreen("reference.png")

            if download_location is not None:
                download_point_location = center(download_location)
                click(download_point_location.x, download_point_location.y)

                # Bekleme süresi Ctrl+W'ye basıldıktan sonra
                sleep(wait_after_click)

                # Press Ctrl+W to close the current tab/window
                hotkey('ctrl', 'w')

                # Bekleme süresi bir sonraki döngüye geçmeden önce
                sleep(wait_before_next_loop)

                break  # Başarıyla işlem tamamlandı, döngüyü kır

        retry_attempts += 1

    # Tıklama yeri bulunamazsa kullanıcıya bilgi ver
    if retry_attempts >= max_retry_attempts:
        print("Tıklama yeri bulunamadı. Yeniden denemek için bekleniyor...")
        sleep(wait_before_next_loop)
