const slider = document.querySelector('.slider');
const sliderContainer = document.querySelector('.slider-container');
const sliderItems = document.querySelectorAll('.slider-item');

let firstItemWidth = 0;
let currentPosition = 0;
let newItem;

for (let i = 0; i < sliderItems.length; i++) {
  if (i === 0) {
    firstItemWidth = sliderItems[i].offsetWidth;
  }
  newItem = sliderItems[i].cloneNode(true);
  sliderContainer.appendChild(newItem);
}

sliderContainer.style.width = `${sliderItems.length * firstItemWidth}px`;

setInterval(() => {
  currentPosition -=
