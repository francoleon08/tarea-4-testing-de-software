from selenium.webdriver.common.by import By

# Test para verificar el inicio de sesión exitoso
def test_login_successful(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('dumbridge')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('tomriddle')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    current_url = driver.execute_script("return window.location.href")

    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/inicio.html', \
        f"URL actual ({current_url}) no coincide con la esperada"


# Test para verificar el inicio de sesión fallido con contraseña incorrecta
def test_incorrect_password(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('dumbridge')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('1234')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    current_url = driver.execute_script("return window.location.href")

    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html', \
        f"URL actual ({current_url}) no coincide con la esperada"


# Test para verificar el inicio de sesión fallido sin contraseña
def test_empty_password(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('dumbridge')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()
    
    message = driver.find_element(By.ID, 'estado').text
    current_url = driver.execute_script("return window.location.href")
    
    assert message == 'Atención: El password no puede estar vació', \
        f"Mensaje de error incorrecto ({message})"
    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html', \
        f"URL actual ({current_url}) no coincide con la esperada"


# Test para verificar el inicio con un usuario incorrecto
def test_incorrect_username(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys('123')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('tomriddle')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    message = driver.find_element(By.ID, 'estado').text
    current_url = driver.execute_script("return window.location.href")

    assert message == 'Atención: El usuario ingresado no existe', \
        f"Mensaje de error incorrecto ({message})"
    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html', \
        f"URL actual ({current_url}) no coincide con la esperada"
      
        
# Test para verificar el inicio sin ingresar un usuario
def test_empty_username(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('tomriddle')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    message = driver.find_element(By.ID, 'estado').text
    current_url = driver.execute_script("return window.location.href")

    assert message == 'Atención: Debe ingresar un nombre de usuario', \
        f"Mensaje de error incorrecto ({message})"
    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html', \
        f"URL actual ({current_url}) no coincide con la esperada"
        
        
# Test para verificar el inicio con campos vacíos
def test_empty_fields(setup_teardown):
    driver = setup_teardown

    driver.get('https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html')

    button = driver.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    message = driver.find_element(By.ID, 'estado').text
    current_url = driver.execute_script("return window.location.href")

    assert message == 'Atención: Debe ingresar un nombre de usuario', \
        f"Mensaje de error incorrecto ({message})"
    assert current_url == 'https://cs.uns.edu.ar/~mll/temp/testing/examen/login.html', \
        f"URL actual ({current_url}) no coincide con la esperada"