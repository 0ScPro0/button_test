from fastapi import FastAPI  # Импортируем FastAPI

# Создаём приложение
app = FastAPI()

# Этот код сработает, когда нажмут кнопку на сайте
@app.post("/button_press")  # POST-запрос по адресу /button_press
def button_press():
    print("pressed")  # Выводим "pressed" в консоль сервера
    return {"status": "success"}  # Отправляем JSON назад в браузер