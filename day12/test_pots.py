from pots import Pots
    
def test_1():
    initial = "#..#.#..##......###...###"
    rules = {}
    file = open("test.txt", "r")
    for line in file:
        rule = line[:5]
        state = line[9]
        rules.update({rule:state})
    
    pots = Pots(initial)
    pots.add_rules(rules)
    pots.apply_rules()
    pots.count_plants()
    result = pots.print_gen()
    assert result == "#...#....#.....#..#..#..#."

def test_2():
    initial = "#..#.#..##......###...###"
    rules = {}
    file = open("test.txt", "r")
    for line in file:
        rule = line[:5]
        state = line[9]
        rules.update({rule:state})
    
    pots = Pots(initial)
    pots.add_rules(rules)
    pots.apply_rules()
    pots.apply_rules()
    pots.count_plants()
    result = pots.print_gen()
    assert result == "##..##...##....#..#..#..##."

def test_3():
    initial = "#..#.#..##......###...###"
    rules = {}
    file = open("test.txt", "r")
    for line in file:
        rule = line[:5]
        state = line[9]
        rules.update({rule:state})
    
    pots = Pots(initial)
    pots.add_rules(rules)
    pots.apply_rules()
    pots.apply_rules()
    pots.apply_rules()
    pots.count_plants()
    result = pots.print_gen()
    assert result == "#.#...#..#.#....#..#..#...#."