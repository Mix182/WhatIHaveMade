import {Bullet} from "./bullet.js"
import {Hibox} from "./hitbox.js"

export class Enemy {
    constructor(win){
        this.win = win
        this.enemies = []
        this.color = "#FF0000"
        this.bullet = Bullet(this.win, "down")
    }
    newEnemy(){

    }
}