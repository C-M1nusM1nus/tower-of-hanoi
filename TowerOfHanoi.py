def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record():
        moves.append(" ".join(str(rod) for rod in rods))

    def move_disks(count, source, target, auxiliary):
        if count == 0:
            return

        move_disks(count - 1, source, auxiliary, target)

        disk = rods[source].pop()
        rods[target].append(disk)
        record()

        move_disks(count - 1, auxiliary, target, source)

    # Record the starting arrangement
    record()

    # Move all disks from rod 0 to rod 2
    move_disks(n, 0, 2, 1)

    return "\n".join(moves)
