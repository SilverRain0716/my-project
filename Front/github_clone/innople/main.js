const slider = document.querySelector('.slider');
const sliderContainer = document.querySelector('.slider-container');
const sliderItems = document.querySelectorAll('.slider-item');
const slideCount = sliderItems.length;
const slideWidth = slider.clientWidth;
const slideMargin = 10; // Changed slide margin to 10 pixels

sliderContainer.style.width = slideCount * (slideWidth + slideMargin) + "px";

sliderItems.forEach((item) => {
  item.style.width = slideWidth + "px";
});

// Clone the first slider item and append it to the end of the slider
const firstSlideClone = sliderItems[0].cloneNode(true);
sliderContainer.appendChild(firstSlideClone);

let currentSlide = 0;
function transitionSlide() {
  const slideOffset = currentSlide * (slideWidth + slideMargin);
  sliderContainer.style.transform = `translateX(-${slideOffset}px)`;
  
  currentSlide++;
  if (currentSlide >= slideCount) {
    // Reset to the first slide
    currentSlide = 0;
    sliderContainer.style.transform = `translateX(0)`;
  }
}

var slideInterval = 4000;
setInterval(transitionSlide, slideInterval);
