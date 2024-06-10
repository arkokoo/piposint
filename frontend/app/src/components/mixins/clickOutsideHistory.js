export default {
  mounted(el, binding) {
    el.clickOutsideEvent = function (event) {
      console.log(event.target);
      if (!(el === event.target || el.contains(event.target))) {
          if (!event.target.classList.contains('history-button') && !event.target.parentElement.classList.contains('history-button')) {
            binding.value();
        }
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent);
  },
  unmounted(el) {
    document.body.removeEventListener('click', el.clickOutsideEvent);
  },
};