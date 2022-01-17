/*
Write a function that takes a DOM element and smoothly animates it from its current position to distance pixels to the
right over duration milliseconds. Implement the following function, animate(el, milliseconds, distance)
*/


function animate(el, ms, distance) {
    // current distance should be saved to a data-attr in case animate will be run multiple times for the same element
    // if no distance specified, then initialize it to 0
    const currentDistance = el.dataset.distance ? +el.dataset.distance : 0;
    const newDistance = currentDistance + distance;

    // save new distance to data-attr
    el.dataset.distance = newDistance;

    // add transition for the transform (to make it smooth) and specify length of the transition
    el.style.transition = `transform ${ms}ms`;
    // do transition via translateX for a better performance
    el.style.transform = `translateX(${newDistance}px)`;

    // remove transition after animation, so default value for the transition will be applied
    setTimeout(() => {
        el.style.transition = ''
    }, ms)
}
