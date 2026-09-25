document.documentElement.classList.add("js-ready");
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.main-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => (nav.classList.toggle('open'), toggle.setAttribute('aria-expanded', nav.classList.contains('open'))));
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => nav.classList.remove('open')))
}
const revealEls = document.querySelectorAll('[data-reveal]');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target)
    }
  })
}, {
  threshold: .14,
  rootMargin: '0px 0px -60px 0px'
});
revealEls.forEach(el => observer.observe(el));
window.addEventListener('scroll', () => {
  document.documentElement.style.setProperty('--scroll', window.scrollY)
});
