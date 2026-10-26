def nearest_point(points, target):
    x0, y0 = target

    best_point = points[0]
    bx, by = best_point
    best_dist_sq = (bx - x0) ** 2 + (by - y0) ** 2

    for point in points[1:]:
        x, y = point
        dist_sq = (x - x0) ** 2 + (y - y0) ** 2

        if dist_sq < best_dist_sq:
            best_dist_sq = dist_sq
            best_point = point

    return best_point, best_dist_sq ** 0.5

# пример
points = [(0, 0), (5, 5), (2, 2), (1, 1)]
print(nearest_point(points, (3, 3))) 