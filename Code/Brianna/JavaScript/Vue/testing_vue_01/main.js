let  card = new Vue({
    el: "#card",
    data: {
        title: "Dinosaurs",
        items: [
            {text: "Velociraptor"},
            {text: "Triceratops"},
            {text: "Stegasaurus"}
        ]
    },
    methods: {
        addItem: function() {
            let input = document.getElementById('itemForm');
            if (input.value !== ''){
                this.items.push({
                    text: input.value
                })
                input.value = '';
            }
        },
        deleteItem: function (index) {
            this.items.splice(index, 1);
        }
    }
})