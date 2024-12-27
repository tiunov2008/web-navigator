
document.addEventListener('DOMContentLoaded', ()=>{
  const swiper = new Swiper('.swiper', {
      // Optional parameters
      loop: true,
      // If we need pagination
      pagination: {
        el: '.swiper-pagination',
      },
      // Navigation arrows
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    
    });
    let bg = document.querySelector('.hero-title');
    window.addEventListener('mousemove', function(e) {
    let x2 = e.clientX;
    let y2 = e.clientY;  
    let x1 = bg.getBoundingClientRect().left;
    let y1 = bg.getBoundingClientRect().top;
    
    let angleDeg = Math.abs(Math.round(Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI / 2));
    console.log(x2, y2, x1, y1);
    bg.style.background = 'linear-gradient(' + angleDeg + 'deg, #4287ff 10%, #0015d4 35%, #4966fc 100%)';
    bg.style.backgroundClip = 'text';
  });
})
