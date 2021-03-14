from solution import line

def show(grid):
    print('\n'.join(grid))
    return grid

Test.describe("Sample tests")

expected = True
Test.it("Good1")
grid = ["           ",
        "X---------X",
        "           ",
        "           "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Good2")
grid = ["     ",
        "  X  ",
        "  |  ",
        "  |  ",
        "  X  "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Good3")
grid = ["                    ",
        "     +--------+     ",
        "  X--+        +--+  ",
        "                 |  ",
        "                 X  ",
        "                    "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Good4")
grid = ["                     ",
        "    +-------------+  ",
        "    |             |  ",
        " X--+      X------+  ",
        "                     "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Good5")
grid = ["                      ",
        "   +-------+          ",
        "   |      +++---+     ",
        "X--+      +-+   X     "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")



expected = False
Test.it("Bad1")
grid = ["X-----|----X"]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Bad2")
grid = [" X  ",
        " |  ",
        " +  ",
        " X  "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Bad3")
grid = ["   |--------+    ",
        "X---        ---+ ",
        "               | ",
        "               X "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Bad4")
grid = ["              ",
        "   +------    ",
        "   |          ",
        "X--+      X   ",
        "              "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")


Test.it("Bad5")
grid = ["      +------+",
        "      |      |",
        "X-----+------+",
        "      |       ",
        "      X       "]
test.assert_equals(line(show(grid)), expected)
print("<COMPLETEDIN::>")
print("<COMPLETEDIN::>")
