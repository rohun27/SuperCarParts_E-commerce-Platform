// Add smooth scrolling for navigation links
document.querySelectorAll('nav a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add event listener to the "Explore Specs" button
document.querySelector('.hero button').addEventListener('click', function() {
    document.querySelector('#car-Parts').scrollIntoView({
        behavior: 'smooth'
    });
});

// Add hover effect to car cards
const carCards = document.querySelectorAll('.car-card');
carCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05)';
    });
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
});