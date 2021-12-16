const screen = document.getElementById("screen")
const win = screen.getContext("2d")

screen.width = innerWidth - 5
screen.height = innerHeight - 6

import {Player, Enemy, Bullet} from "./classes/import.js"

let width = innerWidth / 15
let height = innerHeight / 20

const player = new Player(win , {
    x: (innerWidth / 2) - (width / 2), 
    y: innerHeight - (innerHeight / 10) - height}, width, height)

let right = false
let left = false
let speed = innerWidth / 40

function animate(){
    requestAnimationFrame(animate)

    player.bullet.update()

    draw()

    if (right){
        player.move(true, speed)
    } else if (left){
        player.move(false, speed)
    }
}

function draw(){
    win.clearRect(0, 0, innerWidth, innerHeight)
    player.draw()
    player.bullet.draw()
}

addEventListener("keydown", (key) => {
    if (key.keyCode == 65){
        left = true
    } else if (key.keyCode == 68){
        right = true
    } else if (key.keyCode == 32){
        player.shoot(true)
    }
})

addEventListener("keyup", (key) => {
    if (key.keyCode == 65){
        left = false
    } else if (key.keyCode == 68){
        right = false
    } else if (key.keyCode == 32){
        player.shoot(false)
    }
})

animate()