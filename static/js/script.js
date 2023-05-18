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