export class Hitbox{
    constructor(x, y, width, height){
        this.x = x
        this.y = y
        this.w = width
        this.h = height
        this.top = y
        this.bottom = y + height
        this.left = x
        this.right = x + width

    }
    colided(otherHitbox){
        let oH = otherHitbox
        if ((this.right > oH.left && thzis.left < oH.right) && (this.bottom > oH.top && this.top < oH.bottom)){
            return true
        } else {
            return false
        }
    }
}