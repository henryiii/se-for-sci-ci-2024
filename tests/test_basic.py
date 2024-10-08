import example


def test_compare():
    a = example.Vector(1, 2)
    b = example.Vector(1, 2)

    assert a.x == b.x
    assert a.y == b.y
    assert a == b
    assert repr(a) == "Vector(x=1, y=2)"
    assert a != example.Vector(2, 2)
