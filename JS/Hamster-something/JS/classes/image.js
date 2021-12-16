export class Image {
    constructor(link){
        this.img = document.createElement("img")
        this.img.src = link
        this.img.id = "button"
        document.getElementById("textures").appendChild(this.img)
    }
}