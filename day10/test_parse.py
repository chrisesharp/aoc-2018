from sky import Sky

def test_1():
    input = "position=< 9,  1> velocity=< 0,  2>"
    sky = Sky()
    sky.add_point(input)
    print(sky.points)
    assert sky.get_point((9,1)) == '#'
    assert sky.get_point((9,3)) == '.'

def test_2():
    input = "position=< 9,  1> velocity=< 0,  2>"
    sky = Sky()
    sky.add_point(input)
    print(sky.points)
    sky.points = sky.tick()
    print(sky.points)
    assert sky.get_point((9,1)) == '.'
    assert sky.get_point((9,3)) == '#'

def test_3():
    sky = Sky()
    file = open("test.txt", "r")
    for line in file:
        sky.add_point(line)

    assert sky.left == -6
    assert sky.right == 15
    assert sky.top == -4
    assert sky.bottom == 11

def test_4():
    expected = r"""
........#.............
................#.....
.........#.#..#.......
......................
#..........#.#.......#
...............#......
....#.................
..#.#....#............
.......#..............
......#...............
...#...#.#...#........
....#..#..#.........#.
.......#..............
...........#..#.......
#...........#.........
...#.......#..........
"""
    sky = Sky()
    file = open("test.txt", "r")
    for line in file:
        sky.add_point(line)
    
    output = sky.render()
    print(output)
    assert output == expected

def test_5():
    expected = r"""
......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................
"""
    sky = Sky()
    file = open("test.txt", "r")
    for line in file:
        sky.add_point(line)
    sky.points = sky.tick()
    sky.points = sky.tick()
    sky.points = sky.tick()
    output = sky.render()
    print(output)
    assert output == expected
    
    