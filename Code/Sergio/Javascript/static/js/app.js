//const CRYPTOCOMPARE_API_URI = "https://www.cryptocompare.com";
//crypto compare api has changed and hence changing its base url to the latest version
const CRYPTOCOMPARE_API_URI = "https://min-api.cryptocompare.com";
const CRYPTOCOMPARE_BASE_IMAGE_URI = "https://www.cryptocompare.com";
const COINMARKETCAP_API_URI = "https://api.coinmarketcap.com";
const UPDATE_INTERVAL = 60 * 1000;

let app = new Vue({
  el: "#app",
  data: {
    coins: [],
    coinData: {}
  },

  methods: {
    getCoinData: function() {
      let self = this;
      //changing api end point to its latest end (cryptocompare api has changed) ..
      axios.get(CRYPTOCOMPARE_API_URI + "/data/all/coinlist")
        .then((res) => {
            this.coinData = res.data.Data;
            //console.log(JSON.stringify("getting coin data."));
            //console.log(JSON.stringify(res));
            this.getCoins();
          })
        .catch((err) => {
          this.getCoins();
          console.error(err);
        });
    },
    getCoins: function() {
      let self = this;

      axios.get(COINMARKETCAP_API_URI + "/v1/ticker/?limit=10")
      .then((res) => {
        this.coins = res.data;
      //console.log(JSON.stringify("getting coin."));
      })
      .catch((err) => {
        console.error(err);
      });
    },
    getCoinImage: function(symbol) {
      //console.log(JSON.stringify(symbol));
      //console.log(JSON.stringify(this.coinData));
      symbol = (symbol === "MIOTA" ? "IOT" : symbol);
      symbol = (symbol === "VERI" ? "VRM" : symbol);
     // console.log(JSON.stringify("getting coin Image."));
      return CRYPTOCOMPARE_BASE_IMAGE_URI + this.coinData[symbol].ImageUrl;
    },
    getColor: (num) => {
//      console.log(JSON.stringify("getting coin color."));
      return num > 0 ? "color:green;" : "color:red;";
    },
  },
  created: function() {
  this.getCoinData();
  }
});

setInterval(() => {
  app.getCoins();
}, UPDATE_INTERVAL);
