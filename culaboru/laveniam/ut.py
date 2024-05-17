def logger(num, data):
    """
    Logs the data to a file.

    Args:
        num (int): The number of the log entry.
        data (str): The data to log.
    """

    with open("log.txt", "a") as f:
        f.write(f"{num}: {data}\n")
