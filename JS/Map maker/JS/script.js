const screen = document.getElementById("screen")
const win = screen.getContext("2d")
const text_box = document.getElementById("text")
const button = document.getElementById("button")

screen.width = innerWidth
screen.height = innerHeight

win.fillStyle = "#000000"
win.fillRect(0, 0, screen.width, screen.height)