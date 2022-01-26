import position_traps_to_geojson as ptg


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = ptg.add_offset(augend, addend)
    assert expected == obtained
