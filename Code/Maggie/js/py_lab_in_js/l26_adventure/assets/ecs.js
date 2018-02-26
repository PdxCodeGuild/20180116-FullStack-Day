//js entity component system that allows modular additions of components to default entities
//follows tutorial found at http://vasir.net/blog/game-development/how-to-build-entity-component-system-in-javascript
//using es5 class syntax because it allows modular component additions/avoids hierarchical inheritance order limitations of super

let ECS = {}; //instantiate the Entity Component System

//entity will have random ID and empty component array
ECS.Entity = function Entity() {
    //uses date object and random to create a 'random' ID
     this.id = (+new Date()).toString(16) +
        (Math.random() * 100000000 | 0).toString(16) +
        ECS.Entity.prototype._count;

    // incrementing a counter
    ECS.Entity.prototype._count++;

    return this;
};
//prototype counter to keep track of entities
ECS.Entity.prototype._count = 0;

//the addComponent allows modular addition of components to entities by its constructor prototype reference
ECS.Entity.prototype.addComponent = function addComponent ( component ){
    //add component **by its 'name' property** to the entity component array
    this.components[component.name] = component;
    return this;
};

//the remove component references an entities constructor to access the component array and deletes the name so it can no longer be referenced
ECS.Entity.prototype.removeComponent = function removeComponent ( componentName ) {
    let name = componentName;  //so we can pass in strings to reference the object property
    if(typeof  componentName === 'function'){
        //first check type to make sure that it is a valid reference
        name = componentName.prototype.name; //variable now references constructor data
    }
    //delete the name from the component list and return the updated object
    delete this.components[name];
    return this;
};

// a logger for the entity specifics
ECS.Entity.prototype.log_Info = function log_Info () {
    // log information about the entity
    console.log(JSON.stringify(this, null, 4));
    return this;
};
