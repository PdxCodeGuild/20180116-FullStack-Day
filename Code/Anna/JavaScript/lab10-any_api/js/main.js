// determine if it's night or day
let now = new Date();
let dayOrNight = "day";
if (now.getHours() > 18 || now.getHours() < 7 ) {
    dayOrNight = "night";
}


// the main Vue app
let app = new Vue({
    el: '#app',
    mounted: function() {
        console.log("Ready!");
        $('select').material_select();
        if (dayOrNight === "day") {
            $('body').addClass('dayMode');
            this.greeting = "Good day!";
        } else {
            $('body').addClass('nightMode');
            this.greeting = "Good night!";
        }
        },
    data: {
        greeting: '',
        title: "How's the weather in your neck of the woods?",
        city: 'your city',
        time: dayOrNight,
        selectedWeather: '',
        celsius: "Wait, what is this Celsius bullshit?!?",
        murica: "Show me some 'Murican units!",
        options: [
            { value: 1,
            text: "really nice outside."},
            { value: 2,
            text: "sunny and perfect 😊"},
            { value: 3,
            text: "kinda grey..."},
            { value: 4,
            text: "raining and miserable"},
            { value: 5,
            text: "raining, but I like it."},
            { value: 6,
            text: "snowing! WTF?!?"},
            { value: 7,
            text: "snowing, wheeee!"},
            { value: 8,
            text: "what's this 'outside' you speak of?"},
        ],
        resultMain: "",
        resultDesc: "",
        weatherResults: {
            main: '',
            description: '',
            icon: '',
            iconSrc: '',
            temp: '',
            clouds: ''
        }
    },
    watch: {    // not using this ATM
        displaySelected: function (selectedWeather) {
            if (selectedWeather.value === 1 || selectedWeather.value === 2) {
                console.log("That's awesome!");
            } else if (selectedWeather.value === 3) {
                console.log("Maybe it'll brighten up later, let's see...");
            } else if (selectedWeather.value === 4) {
                console.log("That sucks 😔");
            } else if (selectedWeather.value === 5) {
                console.log("That's the spirit!");
            } else if (selectedWeather.value === 6) {
                console.log("I know, right?");
            } else if (selectedWeather.value === 7) {
                console.log("Let's build a snowman! ☃️");
            } else if (selectedWeather.value === 8) {
                console.log("Get off your computer, there's a big world out there!");
            }
        }
    },
    methods: {
        getWeather: function() {
            console.log("Getting weather for " + this.city);
            let url = 'https://api.openweathermap.org/data/2.5/weather?q=' + this.city + '&appid=0a4a01ff35467b0ba44767fcc74a1ad2';
            this.$http.get(url).then((response) => {
                console.log(response);
                // response = JSON.parse(response);
                // console.log(response);
                response = response.body;
                this.weatherResults.main = response.weather[0].main.toLowerCase();
                this.weatherResults.description = response.weather[0].description.toLowerCase();
                this.weatherResults.icon = response.weather[0].icon;
                this.weatherResults.iconSrc = response.weather[0].id;
                this.weatherResults.temp = response.main.temp;
                this.weatherResults.clouds = response.clouds.all;
                if (this.weatherResults.main === 'clouds') {
                    this.weatherResults.main = 'cloudy';
                } else if (this.weatherResults.main === 'rain') {
                    this.weatherResults.main = 'raining';
                } else if (this.weatherResults.main === 'snow') {
                    this.weatherResults.main = 'snowing';
                } else if (this.weatherResults.main === 'haze') {
                    this.weatherResults.main = 'hazy';
                }
            });
            console.log("It is " + dayOrNight);
            setTimeout(this.showWeather, 2000);
        },
        showWeather: function() {
            $('#introDiv').addClass('hidden');
            $('#resultDiv').removeClass('hidden');
            $('body').removeClass();
            console.log("Weather code: "+ this.weatherResults.iconSrc);
            if (this.weatherResults.iconSrc === 800) {
                $('body').addClass('clearSkies');
            } else if (this.weatherResults.iconSrc > 800 && this.weatherResults.iconSrc < 803) {
                $('body').addClass('mixedSkies');
            } else if (this.weatherResults.iconSrc === 803 || this.weatherResults.iconSrc === 804 || (this.weatherResults.iconSrc > 700 && this.weatherResults.iconSrc < 800)) {
                $('body').addClass('greySkies');
            } else if (this.weatherResults.iconSrc >= 200 && this.weatherResults.iconSrc < 600) {
                $('body').addClass('rainSkies');
            } else if (this.weatherResults.iconSrc >= 600 && this.weatherResults.iconSrc < 700) {
                $('body').addClass('snowSkies');
            } else if (this.weatherResults.iconSrc >= 900) {
                $('body').addClass('extremeSkies');
            } else {
                $('body').addClass('mixedSkies');
            }
            let owfClass = 'owf-'+ this.weatherResults.iconSrc;
            $('#weatherIcon').addClass(owfClass);
            this.resultMain = "Right now, it is " + this.weatherResults.main + " in " + this.city + ".";
            this.resultDesc = "The weather is " + this.weatherResults.description + ", the temperature is "
                + Math.round(this.weatherResults.temp - 273.15) + "°C, with " + this.weatherResults.clouds + "% cloud cover."
        },
        goAgain: function(){
            $('#resultDiv').addClass('hidden');
            $('#introDiv').removeClass('hidden');
            $('body').removeClass();
            if (dayOrNight === "day") {
                $('body').addClass('dayMode');
                this.greeting = "Good day!";
            } else {
                $('body').addClass('nightMode');
                this.greeting = "Good night!";
            }
            this.celsius = "Wait, what is this Celsius bullshit?!?";
            this.murica = "Show me some 'Murican units!";
        },
        goFYourTemp: function() {
            this.resultDesc = "The weather is " + this.weatherResults.description + ", the temperature is "
                + Math.round((this.weatherResults.temp * (9/5)) - 459.67) + "°F, with " + this.weatherResults.clouds + "% cloud cover.";
            this.murica = "Happy now?";
            this.celsius = '';
            $('body').removeClass();
            $('body').addClass('muricaMode');
        }
    }
});



