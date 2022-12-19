import turtle

width = 1200
height = 600

def main():
    screen= turtle.Screen()
    screen.setup(width, height, 0, 0)
    t = turtle. Turtle()
    def draw_koch_segment(t, ln):
        if ln > 6:
            ln3 = ln // 3
            draw_koch_segment(t, ln3)
            t.left(60)
            draw_koch_segment(t, ln3)
            t.right(120)
            draw_koch_segment(t, ln3)
            t.left(60)
            draw_koch_segment(t, ln3)
        else:
            t.fd(ln*10)
            t.left(60)
            t.fd(ln*10)
            t.right(120)
            t.fd(ln*10)
            t.left(60)
            t.fd(ln*10)

    t.speed(100)

    draw_koch_segment(t, 7)

    turtle.done()

if __name__ == "__main__":
    main()
