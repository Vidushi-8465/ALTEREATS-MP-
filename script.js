// JavaScript for any interactivity or animations can be added here
// For example, you can add event listeners or custom animations

// Example: Adding a hover effect to service cards
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseover', () => {
        card.style.transform = 'scale(1.05)';
        card.style.transition = 'transform 0.3s ease-in-out';
    });

    card.addEventListener('mouseout', () => {
        card.style.transform = 'scale(1)';
    });
});