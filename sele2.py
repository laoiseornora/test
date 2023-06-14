sele2

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# DANE TESTOWE
imie = "Paulina"
email = "psujka14@gmail.com"
invalid_password = "tydsghsghfiejfi"

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        # Otworzyć stronę zalando.pl
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.zalando.pl/")
        # Zamknij okno cookies
        try:
            cookies_btn = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-testid="uc-banner-accept-button"]'))
            )
            cookies_btn.click()
        except:
            pass
        self.driver.implicitly_wait(10)

    def testNoCapitalLetterInPassword(self):
        # 1. Kliknij "Zaloguj się"
        zaloguj_btn = self.driver.find_element(By.XPATH, '//a[@data-testid="z-navicat-header-login-link"]')
        zaloguj_btn.click()
        # 2. Kliknij "Załóż konto"
        zaloz_konto_btn = self.driver.find_element(By.XPATH, '//button[@data-testid="signup-button"]')
        zaloz_konto_btn.click()
        imie_input = self.driver.find_element(By.XPATH, '//input[@data-testid="register-username"]')
        imie_input.send_keys(imie)
        email_input = self.driver.find_element(By.XPATH, '//input[@data-testid="register-email"]')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.XPATH, '//input[@data-testid="register-password"]')
        password_input.send_keys(invalid_password)

        # OCZEKIWANY REZULTAT
        # Użytkownik otrzymuje informację "Hasło musi zawierać co najmniej jedną wielką literę."
        
        # 1. Szukam komunikatu o błędzie
        error_message = self.driver.find_element(By.XPATH, '//div[@data-testid="register-passwordError"]')
        # 2. Sprawdzam treść i widoczność komunikatu "Hasło musi zawierać co najmniej jedną wielką literę."
        self.assertEqual("Hasło musi zawierać co najmniej jedną wielką literę.", error_message.text)
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
