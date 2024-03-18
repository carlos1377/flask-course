import time


def duration_time(function):
    def wrapper():
        init = time.time()
        function()
        final = time.time()

        print(
            f'O tempo total da função {
                function.__name__} foi de {str(final-init)}'
        )

    return wrapper


@duration_time
def main():
    for i in range(1, 10000):
        pass


main()
