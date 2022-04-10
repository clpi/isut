import nimpy
import pixie

proc pasteCursor*(imgPath: string, x1, y1, x2, y2: int): Image {.exportpy.} =
    var img: Image = readImage(imgPath)
    let cursor: Image = readImage("res/cursor_vistsm.png")
    img.draw(cursor,
        translate(vec2(100, 100)) *
        scale(vec2(0.2, 0.2)) *
        translate(vec2(-450, -450))
    )
    img.writeFile(imgPath)