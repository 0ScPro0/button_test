document.getElementById("main_button").addEventListener("click", async () => {
    // Отправляем POST-запрос на сервер
    const response = await fetch("http://localhost:8000/button_press", {
      method: "POST",
    });
    const result = await response.json(); // Читаем ответ {"status": "success"}
    console.log(result); // Выводим ответ в консоль браузера
  });