import math
from PIL import Image, ImageDraw
import random


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):  # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def scale(self, v):
        self.x *= v
        self.y *= v


    @staticmethod
    def from_polar(r, theta):  # static methods belong to the type, not the instance
        px = r * math.cos(theta)
        py = r * math.sin(theta)
        return Point(px, py)

    def __str__(self):
        return f'{self.x},{self.y}'




class Mesh:

    def __init__(self, min_x, max_x, n_samples, equation, color=(255,255,255)):
        self.points = []
        for i in range(n_samples):
            # angle = i/(100-1)*2*math.pi
            # radius = 100
            # p = Point.from_polar(radius, angle)
            x = lerp(min_x, max_x, i / (n_samples - 1))
            y = equation(x)
            p = Point(x, y)
            self.points.append(p)
        self.color = color


    def draw(self, img):
        width, height = img.size
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]

            x1 = p1.x + width/2
            y1 = p1.y + height/2
            x2 = p2.x + width/2
            y2 = p2.y + height/2

            draw.line((x1, y1, x2, y2), fill=self.color, width=1)


def lerp(a, b, t):
    return (1-t)*a + t*b



meshes = []
for i in range(10):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    mesh = Mesh(random.randint(-250,-100), random.randint(100,250), 500, lambda x: random.randint(10,60) * math.sin(x), (red, green, blue))
    meshes.append(mesh)


width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for mesh in meshes:
    mesh.draw(img)

# mesh = Mesh(-250, 250, 500, lambda x: 100*math.sin(x), (255, 200, 200))
# mesh.draw(img)

img.show()


