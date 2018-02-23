// let ECS = {}; //instantiate the Entity Component System

class Entity {
    constructor() {
        this.id = Math.floor(Math.random() * Math.floor(10000));  //generate unique id
        this.components = [];

    function addComponent( component ) {
        //add a new component to entity
        this.components.push(component);

        }

}
}

class