import os
import pathlib
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By

def file_uri(filename):
  return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebpageTests(unittest.TestCase):

  def test_increase(self):
      """Make sure header updates to 1 after one click on the increase button."""
      driver.get(file_uri("counter.html"))
      # Encontrar e clicar no botão de aumento
      increase_button = driver.find_element(By.ID, "increase")
      increase_button.click()
      # Obter o texto do cabeçalho e verificar o valor
      header_text = driver.find_element(By.TAG_NAME, "h1").text
      self.assertEqual(header_text, "1")

  def test_decrease(self):
      """Make sure header updates to -1 after one click on the decrease button."""
      driver.get(file_uri("counter.html"))
      # Encontrar e clicar no botão de diminuição
      decrease_button = driver.find_element(By.ID, "decrease")
      decrease_button.click()
      # Obter o texto do cabeçalho e verificar o valor
      header_text = driver.find_element(By.TAG_NAME, "h1").text
      self.assertEqual(header_text, "-1")

  def test_multiple_increase(self):
      """Make sure header updates to 3 after three clicks on the increase button."""
      driver.get(file_uri("counter.html"))
      # Encontrar o botão de aumento e clicar três vezes
      increase_button = driver.find_element(By.ID, "increase")
      for _ in range(3):
          increase_button.click()
      # Obter o texto do cabeçalho e verificar o valor
      header_text = driver.find_element(By.TAG_NAME, "h1").text
      self.assertEqual(header_text, "3")

if __name__ == "__main__":
  unittest.main()