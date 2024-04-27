document.addEventListener("DOMContentLoaded", function() {
    // Get the current URL path
    var path = window.location.pathname;
    // Get the navigation links
    var navItems = document.querySelectorAll('.nav-item');

    // Loop through each navigation link
    navItems.forEach(function(item) {
        // Check if the link's href matches the current URL path
        if ("/"+item.getAttribute('id') === path) {
            // Add the active class to the matched link
            item.classList.add('active');
        }
    });
});