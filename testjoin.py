import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

import os

# Carica le variabili d'ambiente dal file .env
load_dotenv()
meet_link = os.getenv('MEET_LINK')
# Inserisci qui le tue credenziali Google
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


# Configurazione undetected Chrome Driver
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Avvia il browser
driver = uc.Chrome(options=options)

# 1. Naviga alla pagina di login Google
driver.get("https://accounts.google.com/")

# 2. Inserisci l'email
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys(email)
email_field.send_keys(Keys.RETURN)
sleep(2)  # Aspetta il caricamento della pagina

# 3. Inserisci la password
password_field = driver.find_element(By.NAME, "Passwd")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
sleep(2)  # Attendi il caricamento dell'account

# 4. Vai al link di Google Meet
driver.get(meet_link)
sleep(5)  # Attendi il caricamento della pagina di Meet

# 5. Trova e clicca su "Continua senza microfono e videocamera"
try:
    # Attempt to find the button in Italian first
    no_camera_mic_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Continua senza microfono e videocamera')]")
    no_camera_mic_button.click()
except:
    try:
        # Fallback to English if the Italian button is not found
        no_camera_mic_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Continue without microphone and camera')]")
        no_camera_mic_button.click()
    except:
        print("Non trovato il bottone per continuare senza microfono e videocamera.")

sleep(2)  # Attendi un attimo

# 6. Clicca su "Chiedi di partecipare"
try:
    # Attempt to find the button in Italian first
    ask_to_join_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Chiedi di partecipare')]")
    ask_to_join_button.click()
except:
    try:
        # Fallback to English if the Italian button is not found
        ask_to_join_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Ask to join')]")
        ask_to_join_button.click()
    except:
        print("Non trovato il bottone 'Chiedi di partecipare'.")

# Mantieni la finestra aperta
input("Premi Enter per chiudere il browser...")
driver.quit()

