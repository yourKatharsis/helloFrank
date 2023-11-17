class TxtCard:
    name: str
    count: int

    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count

    def __init__(self, row: str):
        card_array = row.split(' ', 1)
        try:
            self.name = card_array[1]
            self.count = int(card_array[0])
        except ValueError as err:
            if len(card_array) > 2:
                print(f"{err=}: Could not find count and name in string.")
            else:
                print(f"{err=}: Could not convert data to an integer.")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise
