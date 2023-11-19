class TxtCard:
    name: str
    count: int

    def __init__(self, name, count) -> None:
        self.name = name
        self.count = count

    @classmethod
    def from_string(cls, row: str):
        card_array = row.split(' ', 1)
        try:
            name = card_array[1]
            count = int(card_array[0])
            return TxtCard(name=name, count=count)
        except (ValueError, IndexError) as err:
            print(f"{type(err)=}: {err=}\nrow=[{row}]")
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}\nrow=[{row}]")
            raise
