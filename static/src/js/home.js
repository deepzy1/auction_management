odoo.define('auction_management.main', function (require) {
    "use strict";

    console.log('JavaScript for Auction Management Loaded!');

    // Initialize WebSocket connection (replace `localhost` with your server if needed)
    const socket = new WebSocket('ws://localhost:8080/');

    socket.onopen = function () {
        console.log('WebSocket connection established');
    };

    socket.onmessage = function (event) {
        console.log('Message received from server:', event.data);
        // Update auction data dynamically
    };

    socket.onclose = function () {
        console.log('WebSocket connection closed');
    };
});
