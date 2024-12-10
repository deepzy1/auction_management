document.addEventListener('DOMContentLoaded', function () {
    const auctionId = parseInt(document.querySelector('input[name="auction_id"]').value);
    const timerElement = document.getElementById('timer');
    const highestBidElement = document.getElementById('highest_bid');
    const bidForm = document.getElementById('bid_form');
    const placeBidButton = document.getElementById('place_bid');

    // Countdown Timer
    const endTime = new Date(document.querySelector('#timer').getAttribute('data-end-time')).getTime();

    function updateTimer() {
        const now = new Date().getTime();
        const distance = endTime - now;

        if (distance < 0) {
            timerElement.innerHTML = "Auction Ended";
            placeBidButton.disabled = true;
            return;
        }

        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        timerElement.innerHTML = `${hours}h ${minutes}m ${seconds}s`;
    }

    setInterval(updateTimer, 1000);

    // Place Bid
    placeBidButton.addEventListener('click', function () {
        const bidAmount = parseFloat(bidForm.querySelector('input[name="bid_amount"]').value);

        fetch('/auction/place_bid', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrf_token"]').value // Include CSRF token if needed
            },
            body: JSON.stringify({
                auction_id: auctionId,
                bid_amount: bidAmount
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    highestBidElement.textContent = data.highest_bid;
                } else {
                    alert(data.error);
                }
            })
            .catch(error => {
                console.error('Error placing bid:', error);
            });
    });

    // Real-Time Updates
    function fetchHighestBid() {
        fetch(`/auction/${auctionId}/highest_bid`)
            .then(response => response.json())
            .then(data => {
                if (data.highest_bid) {
                    highestBidElement.textContent = data.highest_bid;
                }
            })
            .catch(error => {
                console.error('Error fetching highest bid:', error);
            });
    }

    setInterval(fetchHighestBid, 5000); // Poll every 5 seconds
});
