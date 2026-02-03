from fairsharer import fair_sharer

def test_fair_sharer():
    values_1 = [0, 1000, 800, 0]
    result_1 = fair_sharer(values_1, 1)
    assert result_1 == [100, 800, 900, 0], f"Fehler bei 1 Iteration! Erhalten: {result_1}"

    values_2 = [0, 1000, 800, 0]
    result_2 = fair_sharer(values_2, 2)
    assert result_2 == [100, 890, 720, 90], f"Fehler bei 2 Iterationen! Erhalten: {result_2}"