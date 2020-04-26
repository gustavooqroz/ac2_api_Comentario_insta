from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import random 

class InstagramBoot:
    def __init__(self,username, password):
        self.username = username 
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
   
    def login(self):
        driver= self.driver
        driver.get("https://www.instagram.com")  
        time.sleep(3)
        campo_usuario= driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha= driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_nas_fotos_hashtag('maromba')
    
  
  
    @staticmethod
    def Digite_iguaL_um_homosapiens(frase, onde_digitar):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("vai começar a digitar a mensagem na área de texto de compartilhamento de mensagens")
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5) / 10)
  
  
  
  
  
    def comente_nas_fotos_hashtag(self, hashtag):
        driver=self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag + "/")
        time.sleep(3)


        for i in range (1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
       
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                comentarios=['E que todas as dores virem músculos!','Não trate como whey protein quem te trata como albumina.','Beijinho no ombro, pra gordura passar longe'
                ,'O peso mais difícil é levantar da cama','Desista de desistir!','Chega de mimimi e bora malhar!','Siga os seus sonhos, não o que as pessoas dizem',
                'O que não te desafia não faz você mudar','Transforme a motivação em hábito.','Treine pesado ou fique em casa.','Quem treina por gosto não cansa.','Você pode ter resultados ou desculpas.']
                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario= driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(2, 5))
                self.Digite_iguaL_um_homosapiens(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(30,35))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(2)




gustavoBot= InstagramBoot('VamosDominarOword','muitofacilmesmo123')
gustavoBot.login()