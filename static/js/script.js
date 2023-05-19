document.addEventListener("DOMContentLoaded", function() {
    document.body.classList.add("loaded");
  });

  window.addEventListener('scroll', function() {
    var anchor = document.getElementById('anchor');
    var scrollPercent = (document.documentElement.scrollTop + document.body.scrollTop) / (document.documentElement.scrollHeight - document.documentElement.clientHeight) * 100;

    if (scrollPercent >= 10) {
      anchor.style.display = 'block';
    } else {
      anchor.style.display = 'none';
    }
  });

  document.getElementById('anchor').addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  var openBtn = document.getElementById('open-btn');
  var anchor = document.getElementById('anchor');
  var popup = document.getElementById('popup');
  var icons = document.querySelectorAll('.icon');

  openBtn.addEventListener('click', function() {
    popup.style.display = (popup.style.display === 'block') ? 'none' : 'block';
  });

  anchor.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  for (var i = 0; i < icons.length; i++) {
    icons[i].addEventListener('click', function() {
      // Действия при клике на иконку
      // Например, переход на соответствующую страницу
    });
  }