import pygame

# ---------- pygame 窗口初始化 ----------
pygame.init()
CELL = 50                      # 每格像素大小
SCREEN_W, SCREEN_H = 800, 600  # 窗口大小
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("NAS1.0")
screen.fill((255, 255, 255))
pygame.display.flip()

def _check_quit():
    """点窗口关闭按钮后退出程序"""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

def draw(node, x, y, sx, sy):
    """在 pygame 窗口画图：draw("box", 横坐标, 纵坐标, 宽格数, 高格数)"""
    _check_quit()
    if node == "box":
        left, top = x * CELL, y * CELL
        width, height = sx * CELL, sy * CELL
        pygame.draw.rect(screen, (0, 0, 0), (left, top, width, height), 3)
        pygame.display.flip()  # 刷新窗口显示

def clear():
    """清空画布"""
    _check_quit()
    screen.fill((255, 255, 255))
    pygame.display.flip()

# ---------- 代码执行器（原逻辑不变） ----------
b = ""
while True:
    a = input()
    if a == "end":
        exec(b)
        _check_quit()
        print("---------------------------------------------")
        b = ""
    else:
        b = b + a + "\n"
