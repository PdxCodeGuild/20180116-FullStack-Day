//components.js
//Modular components for entities

ECS.Components.Position = function ComponentPosition ( parameters ) {
    //has an x y position on the game board grid
    this.x = parameters.x;
    this.y = parameters.y;
    return this;
};
ECS.Components.Position.prototype.name = 'position';


ECS.Components.PlayerControl = function PlayerControl( parameters ) {
    //entity will be controlled by the player
    this.playercontrolled = true;
};
ECS.Components.PlayerControl.prototype.name = player_control;

ECS.Components.Ears = function() {}; //able to hear other entities if they make noise
ECS.Components.Legs = function() {}; //able to move single spaces
ECS.Components.Eyes = function () {}; //has a field of view
ECS.Components.Mouth = function (){}; //able to chat and relay messages
ECS.Components.Inventory = function() {}; // able to carry items
ECS.Components.Visible = function () {};  //graphically represented with an ascii character
ECS.Components.OccupySpace = function () {}; //keeps other entities from occupying same space
ECS.Components.Energy = function () {}; //has an energy reserve capacity
ECS.Components.Consumable = function () {}; //able to be consumed as an item


