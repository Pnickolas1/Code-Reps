
"""
Rectangle Intersection

Given a ton of rectangles on a X/Y graph, determine if there is an intersection,
if so, give the points of intersection (4)


"""

import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


# does not intersect
r1 = Rectangle(1, 2, 3, 4)
r2 = Rectangle(5, 3, 2, 4)

#intersect
r3 = Rectangle(1, 2, 3, 4)
r4 = Rectangle(1, 2, 3, 4)

#intersect
r4 = Rectangle(1, 1, 2, 5)
r5 = Rectangle(1, 2, 3, 1)

def intersect_rectangle(R1, R2):

    def is_intersect(R1, R2):

        return (R1.x <= R2.x + R2.width and
                R1.x + R1.width >= R2.x and
                R1.y <= R2.y + R2.height and
                R1.y + R1.height >= R2.y)

    if not is_intersect(R1, R2):
        return Rectangle(0, 0, -1, -1) # no intersection

    return Rectangle(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        min(R1.x + R1.width , R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
    )


print(intersect_rectangle(r1, r2))
print(intersect_rectangle(r3, r4))
print(intersect_rectangle(r4, r5))
