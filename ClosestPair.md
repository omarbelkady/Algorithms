function ClosestPair(points):
    if length(points) <= 3:
        return bruteForceClosestPair(points)
    mid = length(points) // 2
    left = points[0:mid]
    right = points[mid:]
    dLeft = ClosestPair(left)
    dRight = ClosestPair(right)
    d = min(dLeft, dRight)
    strip = [p for p in points if abs(p.x - points[mid].x) < d]
    return min(d, closestInStrip(strip, d))