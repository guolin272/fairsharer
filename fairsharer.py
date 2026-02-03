def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neighbor of the rightmost field.

    Args:
        values (list): 1D array of values.
        num_iterations (int): Integer to set the number of iterations.
        share (float): Fraction to share with neighbors. Default is 0.1.

    Returns:
        list: The updated values after iterations.
    """
    # Kopieren uns die vorgegeben Daten
    values_new = list(values)
    
    for _ in range(num_iterations):
        # Als erstes Suchen wir den höchsten Wert
        max_val = max(values_new)
        
        # Dann suchen wir den Index von dem höchsten Wert
        max_idx = values_new.index(max_val)
        
        # Berechnen wie viel wir abgeben vom höchsten Wert
        share_amount = max_val * share
        
        # Dem aktuellen Index abziehen
        values_new[max_idx] -= 2 * share_amount
        
        # Nachbarn berechnen
        left_idx = (max_idx - 1) % len(values_new)
        right_idx = (max_idx + 1) % len(values_new)
        
        # Den Nachbarn die Werte addieren
        values_new[left_idx] += share_amount
        values_new[right_idx] += share_amount
        
    return values_new

if __name__ == "__main__":
    test_values = [0, 1000, 800, 0]
    result = fair_sharer(test_values, 1)
    print(f"Nach 1 Iteration: {result}") 
    
    result2 = fair_sharer(result, 1)
    print(f"Nach 2 Iterationen: {result2}")