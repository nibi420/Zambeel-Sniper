from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


absolute_path = os.path.dirname(__file__)
path_string = absolute_path + "\\chromedriver.exe"

PATH = path_string

def call_chrome(id,pswd):
    driver = webdriver.Chrome(PATH)

    driver.get("https://zambeel.lums.edu.pk/psc/ps/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?")

    driver.maximize_window()

    User_ID = driver.find_element("id","userid")
    User_ID.send_keys(id)

    Password = driver.find_element("id","pwd")
    Password.send_keys(pswd)

    Sign_In = driver.find_element("name","Submit")
    Sign_In.click()




    ##PLanner Click
    try:
        
        Planner = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "win0divPTNUI_LAND_REC_GROUPLET$12"))
        )
        Planner.click()

    
    except:
        print("Enrollment wasn't Found")
        driver.quit()




    ##Switch to main frame
    try:
        
        main_frame = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "main_target_win0"))
        )
        driver.switch_to.frame("main_target_win0")

    
    except:
        print("Iframe wasn't Found")
        driver.quit()


    ##Shopping Cart Click
    try:
        
        Shopping_Cart = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(.,'Shopping Cart')]"))
        )
        Shopping_Cart.click()

    
    except:
        print("Shopping Cart wasn't Found")
        driver.quit()
        
    


    ##CheckBox
    try:
        
        check_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "P_SELECT$0"))
        )
        check_box.click()

    
    except:
        print("Checkbox wasn't Found")
        driver.quit()

    #Enroll button
    try:
        
        Enroll = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "DERIVED_REGFRM1_LINK_ADD_ENRL$291$"))
        )
        Enroll.click()

    
    except:
        print("Enroll wasn't Found")
        driver.quit()


    t_end = time.time() + 60
    while time.time() < t_end:

        time.sleep(5)
        ##CheckBoxUnselect
        try:
            
            check_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "P_SELECT$0"))
            )
            check_box.click()


        except:
            print("Checkbox wasn't Found")
            driver.quit()

        time.sleep(5)

        ##CheckBox
        try:
            
            check_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "P_SELECT$0"))
            )
            check_box.click()

        
        except:
            print("Checkbox wasn't Found")
            driver.quit()



        #Enroll button
        try:
            
            Enroll = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "DERIVED_REGFRM1_LINK_ADD_ENRL$291$"))
            )
            Enroll.click()

        
        except:
            print("Enroll wasn't Found")
            driver.quit()

        time.sleep(10)

