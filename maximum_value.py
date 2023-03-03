from typing import List


def maximum_value(orders: List[dict], maximum_weight: int) -> int:
    """
    Retrieves the maximum value from a list of orders with a limited maximum weight
    Args:
        orders (List[dict]): list containing dictionaries with the weight and value of each package
        maximum_weight (int): maximum capacity of the cargo robot
    Returns:
        int:
            maximum value that the cargo robot can handle from the list of orders
    """

    def maximum_value_helper(_orders: List[dict], _maximum_weight: int, max_value: int, current_value: int) -> int:
        """
        Helper function that iterates over the orders recursively to get the best possible package combination
        Args:
            _orders (List[dict]): list containing dictionaries with the weight and value of each package
            _maximum_weight (int): maximum capacity of the cargo robot in the current state of the iteration
            max_value (int): maximum current best value found
            current_value (int): current value during the best combination search
        Returns:
            int: maximum value that the cargo robot can handle from the list of orders
        """
        for index, order in enumerate(_orders):
            value = order["value"]
            weight = order["weight"]
            if weight <= _maximum_weight:
                current_value += value
                if current_value > max_value:
                    max_value = current_value
                # recursive call moving index and updating current maximum weight
                max_value = maximum_value_helper(
                    _orders[index + 1:], _maximum_weight - weight, max_value, current_value
                )
                current_value -= value
        return max_value

    return maximum_value_helper(
        orders,
        maximum_weight,
        0,  # max_value found set to 0 in case no combination found
        0,  # current_value set to 0 in case no combination found
    )
