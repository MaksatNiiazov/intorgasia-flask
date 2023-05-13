  // Находим элементы услуг и их содержимое
  const services = document.getElementById("services");
  const serviceElems = services.querySelectorAll(".service");
  
  // Находим элементы для вывода итоговых результатов
  const totalElement = document.getElementById("total");
  const averageElement = document.getElementById("average");
  const countElement = document.getElementById("count");
  
  // Находим элементы кнопок увеличения и уменьшения количества услуг
  const decrementButtons = services.querySelectorAll(".decrement");
  const incrementButtons = services.querySelectorAll(".increment");
  
  let total = 0;
  let count = 0;
  
  function updateTotals() {
    totalElement.textContent = `Общая стоимость: ${total}р`;
    const average = count > 0 ? total / count : 0;
    averageElement.textContent = `Средняя стоимость: ${average}р`;
    countElement.textContent = `Общее количество услуг: ${count}`;
  }
  
  decrementButtons.forEach(button => {
    button.addEventListener("click", event => {
      const input = event.target.parentNode.querySelector("input");
      const value = parseInt(input.value);
      if (value > 0) {
        input.value = value - 1;
        const serviceElem = event.target.closest(".service");
        const price = parseInt(serviceElem.querySelector(".service-price").textContent);
        total -= price;
        count -= 1;
        updateTotals();
      }
    });
  });
  
  incrementButtons.forEach(button => {
    button.addEventListener("click", event => {
      const input = event.target.parentNode.querySelector("input");
      const value = parseInt(input.value);
      input.value = value + 1;
      const serviceElem = event.target.closest(".service");
      const price = parseInt(serviceElem.querySelector(".service-price").textContent);
      total += price;
      count += 1;
      updateTotals();
    });
  });
  
  serviceElems.forEach(serviceElem => {
    const input = serviceElem.querySelector("input");
    input.addEventListener("input", event => {
      const value = parseInt(input.value);
      if (value >= 0) {
        const price = parseInt(serviceElem.querySelector(".service-price").textContent);
        const prevValue = parseInt(input.getAttribute("data-prev-value"));
        total -= price * (prevValue || 0);
        total += price * value;
        count += value - (prevValue || 0);
        input.setAttribute("data-prev-value", value);
        updateTotals();
      } else {
        input.value = input.getAttribute("data-prev-value") || 0;
      }
    });
  });