def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[float]:
    """
    Computes the BMI for each corresponding height and weight.
    BMI formula: weight / (height^2).

    :param height: list of heights (int or float)
    :param weight: list of weights (int or float)
    :return: list of BMI values
    :raises ValueError: if lists are not the same size or contain invalid types
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists "
                             + "must have the same length.")

        bmi_list = []
        for h, w in zip(height, weight):
            if not (isinstance(h, (int, float))
                    and isinstance(w, (int, float))):
                raise ValueError("All elements in height "
                                 + "and weight must be int or float.")
            if h <= 0:
                raise ValueError("Height cannot be equal or below zero.")
            if w <= 0:
                raise ValueError("Weight cannot be equal or below zero.")
            bmi_list.append(w / (h ** 2))
        return bmi_list
    except ValueError as e:
        print(f"ValueError: {e}")
        exit(1)


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """
    Checks each BMI value against the 'limit'
    to see if it's above (True) or not (False).

    :param bmi: list of BMI values (float)
    :param limit: integer threshold
    :return: list of booleans
    :raises ValueError: if bmi list has invalid types
    """
    try:
        result = []
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise ValueError("All elements in bmi must be numeric.")
            result.append(b > limit)
        return result
    except ValueError as e:
        print(f"ValueError: {e}")
        exit(1)
