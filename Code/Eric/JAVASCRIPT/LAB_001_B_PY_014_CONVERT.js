// pick 6 javascript conversion

let x = true;
// user wants gamble?
while (x) {
    if (confirm("hi this is pick 6- lets gamble")){
        alert("feeling lucky eh");
        game();
    }
    else{
        alert("wimp");
        x = false;
    }
               // user ticket function
    function pick6() {
        let ticket = [];

        let num;
        for (num = 0; num < 5; num++ ) {
            num = Math.floor(Math.random() * 99) + 1;
            ticket.push(num);
        }
        return (ticket);
    }

    // winning numbers function
    function winnings(ticket, winners) {
        let match = 0;
        for (let num = 0; num < 5; num++) {
            if (ticket[num] === winners[num]) {
                match++;
            }
        }
        let payout = [0, 4, 7, 100, 50000, 1000000, 25000000];
        return (payout[match]);
    }

    // play game function
    function game() {
        let winners = pick6();
        let earned = 0;
        let spent = 0;
        let games;
        let ticket;
        for (games = 0; games < 100000; games++) {
            ticket = pick6();
            spent = spent + 2;
            earned = earned + winnings(ticket, winners);
        }
        let bal = (earned - spent);
        let roi = (bal / spent);
        alert("total earnings: $" + earned + "\n" +
            "total spent: $" + spent + "\n" +
            "current bal: $" + bal + "\n" +
            "roi: $" + roi);
    }
}
