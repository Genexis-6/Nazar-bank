// Handle form submissions
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        alert('Form submitted!');
        // Add actual form submission logic here
    });
});

// Handle navigation
document.querySelectorAll('nav ul li a').forEach(link => {
    link.addEventListener('click', function(event) {
        const target = event.target.getAttribute('href');
        if (target && target !== '#') {
            window.location.href = target;
        }
    });
});
