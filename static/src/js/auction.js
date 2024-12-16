odoo.define('auction_management.place_bid', function (require) {
    "use strict";

    var ajax = require('web.ajax');  // Import AJAX functionality from Odoo

    // Place bid function
    window.placeBid = function (auctionId) {
        console.log("placeBid function called for auction ID:", auctionId);

        var bidAmount = document.getElementById('bid-' + auctionId).value;
        console.log("Bid input value:", bidAmount);

        if (bidAmount <= 0) {
            alert("Please enter a valid bid amount.");
            return;
        }

        // Send the bid to the server
        console.log("Sending AJAX request to place bid...");
        ajax.jsonRpc('/auction/place_bid', 'call', {
            'auction_id': auctionId,
            'bid_amount': bidAmount
        }).then(function (response) {
            console.log("AJAX response received:", response);
            if (response.success) {
                alert("Bid placed successfully!");
                document.getElementById('highest-bid-' + auctionId).innerText = "Highest Bid: $" + response.new_highest_bid;
            } else {
                alert(response.error_message || "Failed to place the bid. Please try again.");
            }
        });
    };

    console.log("auction.js loaded and placeBid function registered.");
});
