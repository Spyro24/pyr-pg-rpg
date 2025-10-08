def interpolateVector(start: tuple[int, int], end: tuple[int, int], time: float)->tuple[int, int]:
    startX, startY = start
    endX, endY = end
    return startX + time * (endX - startX), startY + time * (endY - startY)
    