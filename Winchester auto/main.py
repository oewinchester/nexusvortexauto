from pyautogui import locateOnScreen, center, click, hotkey
from time import sleep
from configparser import ConfigParser

# Default values
delay_between_tries = 0.2
delay_after_reference2 = 1  # reference2'ye tıkladıktan sonra beklenecek süre (saniye)
wait_after_click = 5  # Ctrl+W'ye basıldıktan sonra beklenecek süre (saniye)
max_retry_attempts = 3  # Maksimum yeniden deneme sayısı

# If the config has values, use those instead
config = ConfigParser()
config.read('settings.ini')

if config.has_option("SETTINGS", "delay_between_tries"):
    delay_between_tries = float(config["SETTINGS"]["delay_between_tries"])

while True:
    # reference2'yi ara ve tıkla
    download_location2 = locateOnScreen("reference2.png")
    if download_location2 is not None:
        download_point_location2 = center(download_location2)
        click(download_point_location2.x, download_point_location2.y)
        sleep(delay_after_reference2)
    else:
        # reference2 bulunamazsa reference'ı ara ve tıkla
        download_location = locateOnScreen("reference.png")
        if download_location is not None:
            download_point_location = center(download_location)
            click(download_point_location.x, download_point_location.y)
            sleep(wait_after_click)
            hotkey('ctrl', 'w')
            continue  # Döngüyü başa al

    # Eğer reference2 ve reference bulunamazsa, tekrar döngüyü başlat
    retry_attempts = 0
    while retry_attempts < max_retry_attempts:
        sleep(delay_between_tries)
        download_location2 = locateOnScreen("reference2.png")
        if download_location2 is not None:
            download_point_location2 = center(download_location2)
            click(download_point_location2.x, download_point_location2.y)
            sleep(delay_after_reference2)
            break
        download_location = locateOnScreen("reference.png")
        if download_location is not None:
            download_point_location = center(download_location)
            click(download_point_location.x, download_point_location.y)
            sleep(wait_after_click)
            hotkey('ctrl', 'w')
            break
        retry_attempts += 1
