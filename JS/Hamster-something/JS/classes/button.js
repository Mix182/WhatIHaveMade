export class Button{
    constructor(win, text, pos, width, height, image, pressed_immage, sceneToSwitchOn, VIS, hidden = false, text_color = "#000000", font = "Arial") {
        this.win = win
        this.text = text
        this.pos = pos
        this.w = width
        this.h = height
        this.img = image
        this.pimg = pressed_immage
        this.clr = text_color
        this.font = font
        this.hidden = hidden
        this.expantion = 0
        this.pressed = false
        this.STSO = sceneToSwitchOn
        this.vis = VIS
    }
    draw() {
        if (this.hidden == false){
            if (this.pressed == false){
                this.win.drawImage(this.img.img, this.pos.x - this.expantion, this.pos.y - this.expantion, this.w + (this.expantion * 2), this.h + (this.expantion * 2))
            } else {
                this.win.drawImage(this.pimg.img, this.pos.x - this.expantion, this.pos.y - this.expantion, this.w + (this.expantion * 2), this.h + (this.expantion * 2))
            }
            this.win.fillStyle = this.clr
            this.win.font = (((this.h + this.expantion) / 6) * 5) + "px " + this.font
            this.win.textAlign = "center";
            this.win.fillText(this.text, this.pos.x + this.w / 2, this.pos.y + (this.h / 4) * 3, ((this.w + this.expantion) / 6) * 5)
        }
    }
    ITM(mousePos) { // Is Touching Mouse
        if((this.hidden == false) && (mousePos.x > this.pos.x && mousePos.x < this.pos.x + this.w) && (mousePos.y > this.pos.y && mousePos.y < this.pos.y + this.h)){
            return true
        } else {
            return false
        }
    }
}


