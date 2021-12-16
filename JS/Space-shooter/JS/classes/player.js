import {Bullet} from "./bullet.js"
import {Hibox} from "./hitbox.js"

export class Player {
    constructor(win, pos, width, height){
        this.hitbox = new Hibox(pos.x, pos.y, width, height)
        this.bullet = new Bullet(this.win, "up")
        this.shooting = false
        this.stng = 0
    }
    draw(){
        console.log("drawing")
        this.win.fillStyle = "#0000FF"
        this.win.fillRect(this.hitbox.x, this.hitbox.y, this.hitbox.w, this.hitbox.h)

        this.win.fillStyle = "#009900"
        let w = this.hitbox.w / 5
        this.win.fillRect(this.hitbox.x + (this.hitbox.w / 2) - w / 2, this.hitbox.y - this.hitbox.h + 1, w, this.hitbox.h)
    }
    move(right, speed){
        if(right){
            if (!(this.hitbox.x + this.hitbox.w + speed > innerWidth)){
                this.hitbox.x += speed
            }
        } else {
            if (!(this.hitbox.x - speed < 0)){
                this.hitbox.x -= speed
            }
        }
    }
    shoot(playing){
        if (playing && !(this.shooting)){
            this.shooting = true
            this.bullet.newBullet({x: this.hitbox.x + (this.hitbox.w / 2) - this.hitbox.w / 5 / 2, y: this.hitbox.y - this.hitbox.h + 1})

            this.stng = setInterval(() => {
                this.bullet.newBullet({x: this.hitbox.x + (this.hitbox.w / 2) - this.hitbox.w / 5 / 2, y: this.hitbox.y - this.hitbox.h + 1})
            }, 500)
            
        } else if (this.shooting && !(playing)) {
            this.shooting = false
            clearInterval(this.stng)
        }
    }
}