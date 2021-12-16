import {Hibox} from "./hitbox.js"

export class Bullet {
    constructor(win, direction){
        this.win = win
        this.bullets = []
        this.dir = direction
        if (this.dir == "up"){
            this.color = "#FFFF00"
            this.speed = innerHeight / 35
        } else if (this.dir == "down"){
            this.color = "#FF00FF"
            this.speed = innerHeight / 30
        }
    }
    newBullet(pos){
        this.bullets.push({width: innerWidth / 15 / 5,
        height: innerWidth / 20 / 2,
        x: pos.x,
        y: pos.y})
    }
    draw(){
        this.win.fillStyle = this.color
        this.bullets.forEach((bullet) => {
            this.win.fillRect(bullet.x, bullet.y, bullet.width, bullet.height)
        })
    }
    update(){
        if (this.dir == "up"){
            this.bullets.forEach((bullet, index) => {
                bullet.y -= this.speed
                if (bullet.y + bullet.height < 0){
                    this.bullets.splice(index, 1)
                }
            })
        } else if (this.dir == "down"){
            this.bullets.forEach((bullet, index) => {
                bullet.y += this.speed
                if (bullet.y > innerHeight){
                    this.bullets.splice(index, 1)
                }
            })
        }

    }
}