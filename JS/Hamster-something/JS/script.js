import {Button, Image} from "./classes/import.js"

let screen = document.getElementById("screen")
let win = screen.getContext("2d")

let scene = "lobby"

screen.width = innerWidth
screen.height = innerHeight

let textures = {
    "GBU": new Image("/assets/buttons/GBU.jpg"),
    "GBD": new Image("/assets/buttons/GBD.jpg"),
    "PBU": new Image("/assets/buttons/PBU.jpg"),
    "PBD": new Image("/assets/buttons/PBD.jpg"),
    "RBU": new Image("/assets/buttons/RBU.jpg"),
    "RBD": new Image("/assets/buttons/RBD.jpg")
}

let buttons = {
    "play": new Button(win, "Play", {x: (innerWidth / 2) - ((innerWidth / 4) / 2), y: innerHeight / 2}, innerWidth / 4, innerHeight / 5, textures.GBU, textures.GBD, "gameChoosing", "lobby"),

    "settings": new Button(win, "Settings", {x: (innerWidth / 2) - ((innerWidth / 4) / 2), y: (innerHeight / 4) * 3}, innerWidth / 4, innerHeight / 5, textures.PBU, textures.PBD, "settings", "lobby"),

    "ofline": new Button(win, "Ofline", {x: innerWidth / 20, y: innerHeight / 2}, innerWidth / 6, innerHeight / 6, textures.RBU, textures.RBD, "gameCHOfl", "gameChoosing"),

    "backS": new Button(win, "Back", {x: innerWidth / 20, y: innerHeight - (innerHeight / 6) - (innerHeight / 20)}, innerWidth / 6, innerHeight / 6, textures.RBU, textures.RBD, "lobby", "settings"),

    "backP": new Button(win, "Back", {x: innerWidth / 20, y: innerHeight - (innerHeight / 6) - (innerHeight / 20)}, innerWidth / 6, innerHeight / 6, textures.RBU, textures.RBD, "lobby", "gameChoosing")
}

let mousePos = {"x": 0, "y": 0}

document.addEventListener("mousemove", (event) => {
	mousePos = {"x": event.clientX, "y": event.clientY}
    for (let button in buttons){
        if (buttons[button].ITM(mousePos)){
            buttons[button].expantion = buttons[button].w / 10
        } else {
            buttons[button].expantion = 0
        }
    }
})
document.addEventListener("click", (event) => {
    for (let button in buttons){
        if (buttons[button].ITM(mousePos)){
            buttons[button].pressed = true
            setTimeout(() => {scene = buttons[button].STSO}, 300)
        }
    }
})

function animate(){
    let animation = requestAnimationFrame(animate)
    

    update()
    draw()
}

function draw(){
    win.clearRect(0, 0, innerWidth, innerHeight)
    for (let button in buttons){
        buttons[button].draw()
    }
}

function update(){
    for (let button in buttons){
        if (scene != buttons[button].vis){
            buttons[button].hidden = true
            buttons[button].pressed = false
        } else {
            buttons[button].hidden = false
        }
    }
}



animate()