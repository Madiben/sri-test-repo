document.addEventListener('DOMContentLoaded', (event) => {
    const header = document.querySelector('header');

    if (header) {
        header.addEventListener('mouseover', () => {
            alert('HI, I see you');
        });
    }
});