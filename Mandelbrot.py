P = 50                     # размер [2*P+1 x 2*P+1]
scale = P / 2          # масштабный коэффициент
view = (0, 0)            # координаты смещения угла обзора
n_iter = 100                # число итераций для проверки принадлежности к множеству Мандельброта

def main():
    for y in range(-P+view[1], P+view[1]):
        str_line = ""
        for x in range(-P+view[0], P+view[0]):
            trigger = False
            a = x / scale
            b = y / scale
            c = complex(a, b)
            z = complex(0)
            n = 0
            for n in range(n_iter):
                z = z**2 + c
                if abs(z) > 2:
                    break
            else:
                str_line += "#"
                trigger = True

            if not trigger: str_line += " "

        print(str_line)
    input()

if __name__ == "__main__":
    main()

