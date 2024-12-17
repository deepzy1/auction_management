odoo.define('auction_management.countdown', function (require) {
    "use strict";


    return {
        start: function () {
            let auctionCountdowns = document.querySelectorAll('.auction-countdown');

            for (let i = 0; i < auctionCountdowns.length; i++) {
                let countdownElement = auctionCountdowns[i];

                // Extract start date (adapt this to your HTML structure)
                let auctionStartDateStr = countdownElement.parentElement.previousElementSibling.previousElementSibling.previousElementSibling.previousElementSibling.textContent.trim().split(':')[1].trim(); 
                let auctionStartDate = new Date(auctionStartDateStr); 

                // Countdown logic
                function updateCountdown(index) {
                    let now = new Date();
                    let diff = auctionStartDate - now;

                    if (diff > 0) { 
                        let days = Math.floor(diff / (1000 * 60 * 60 * 24));
                        let hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                        let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                        let seconds = Math.floor((diff % (1000 * 60)) / 1000);

                        let timeString = `${days}d:${String(hours).padStart(2, '0')}h:${String(minutes).padStart(2, '0')}m:${String(seconds).padStart(2, '0')}s`;
                        countdownElement.innerHTML = timeString;
                    } else {
                        countdownElement.innerHTML = "Auction Started"; 
                    }
                }

                // Update the countdown every second
                let timerInterval = setInterval(() => updateCountdown(i), 1000);
            }
        }
    };
});