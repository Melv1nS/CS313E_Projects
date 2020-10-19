import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

def read_input(coords):

  point_list = []

  for coord in coords:
    point_list.append(Point(coord[0], coord[1]))

  return point_list

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):

  row1 = [1, p.x, p.y]
  row2 = [1, q.x, q.y]
  row3 = [1, r.x, r.y]

  val = row1[0] * det_2x2(row2[1:], row3[1:]) \
        - row1[1] * det_2x2([row2[0], row2[2]], [row3[0], row3[2]]) \
        + row1[2] * det_2x2(row2[:2], row3[:2])

  return val

#takes two lists representing the first and second rows of the determinant
def det_2x2(p1, p2):

  det = (p1[0] * p2[1]) - (p1[1] * p2[0])
  return det


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):

  #create an empty list upper_hull
  upper_hull = []

  #append first two poins to upper_hull
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])

  #loop for I from range 3 -> end of list
  for i in range(2, len(sorted_points)):

    #append points to upper_hull
    upper_hull.append(sorted_points[i])

    #while upper_hull has 3 or more points and the last 3 points in upper_hull make a right turn
    while len(upper_hull) >= 3 and det(upper_hull[-1], upper_hull[-2], upper_hull[-3]) < 0:

      #remove the middle of the last three points
      del upper_hull[-2]

    i += 1

  lower_hull = []

  sorted_reverse = sorted_points.copy()
  sorted_reverse.reverse()

  lower_hull.append(sorted_reverse[0])
  lower_hull.append(sorted_reverse[1])

  # loop for I from range 3 -> end of list
  for i in range(2, len(sorted_reverse)):

    # append points to lower_hull
    lower_hull.append(sorted_reverse[i])

    # while lower_hull has 3 or more points and the last 3 points in lower_hull make a right turn
    while len(lower_hull) >= 3 and det(lower_hull[-1], lower_hull[-2], lower_hull[-3]) < 0:
      # remove the middle of the last three points
      del lower_hull[-2]

    i += 1

  #remove first and last points to avoid duplication with upper_hull
  del lower_hull[0]
  del lower_hull[len(lower_hull) - 1]

  #append lower_hull to upper_hull and call it convex_hull
  convex_hull = upper_hull

  for val in lower_hull:
    convex_hull.append(val)

  return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):

  convex_poly = convex_poly.copy()
  convex_poly.reverse()

  area = 0
  i = 0
  j = 1
  while i < len(convex_poly):

    area += det_2x2([convex_poly[i].x, convex_poly[j].x],
                    [convex_poly[i].y, convex_poly[j].y])

    i += 1
    j += 1

    if j == len(convex_poly):
      area += det_2x2([convex_poly[i].x, convex_poly[0].x],
                      [convex_poly[i].y, convex_poly[0].y])
      break

  area *= .5

  return area


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  return "all test cases passed"

def get_coords():

  num_coords = int(input())
  coords = []

  for i in range(num_coords):
    line = input().split()
    coords.append((int(line[0]), int(line[1])))
    line.clear()

  return coords

def main(coords):

  # create an empty list of Point objects

  # read data from standard input

  # read line by line, create Point objects and store in a list

  point_list = read_input(coords)

  # sort the list according to x-coordinates

  sorted_points = sorted(point_list)

  # get the convex hull

  convex = convex_hull(sorted_points)

  # run your test cases

  # print your results to standard output

  # print the convex hull

  # get the area of the convex hull
  area = area_poly(convex)

  print(area)

  # print the area of the convex hull

  return convex

if __name__ == "__main__":
  coords = get_coords()
  main(coords)