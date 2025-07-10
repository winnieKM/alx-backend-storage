def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Args:
        method: The method whose history to display
    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__
    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for inp, out in zip(inputs, outputs):
        input_str = inp.decode("utf-8")
        output_str = out.decode("utf-8")
        print(f"{method_name}(*{input_str}) -> {output_str}")
