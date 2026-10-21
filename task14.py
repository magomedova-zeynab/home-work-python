from contextlib import contextmanager


@contextmanager
def log_operation(filename, operation):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"START: {operation}\n")
    try:
        yield
    except Exception:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"ERROR: {operation}\n")
        raise  # исключение продолжает распространяться
    else:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"END: {operation}\n")