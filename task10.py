# Было
class Player(PlayerATD):

    def __init__(self):
        self._inventory: list[str] = []
        self._remove_item_status = self.REMOVE_ITEM_NIL

    def get_inventory(self) -> list[str]:
        return self._inventory

    def add_item(self, item: str) -> None:
        self._inventory.append(item)

    def remove_item(self, item: str):
        item_index: int = -1
        for i, item_invenory in enumerate(self._inventory):
            if item_invenory == item:
                item_index = i
                break
        if item_index == -1:
            self._remove_item_status = self.REMOVE_ITEM_ERR_NOT_EXISTS
        if item_index != -1:
            del self._inventory[item_index]
            self._remove_item_status = self.REMOVE_ITEM_OK

    def clear(self) -> None:
        self._inventory = []

    def has_item(self, item: str) -> bool:
        return item in self._inventory

    def get_remove_item_status(self) -> int:
        return self._remove_item_status


# Стало
class Player(PlayerATD):

    def __init__(self, inventory):
        self._inventory: list[str] = inventory

    def get_inventory(self) -> list[str]:
        return self._inventory

    def add_item(self, item: str) -> Player:
        return Player(self._inventory + [item])

    def remove_item(self, item: str) -> Player:
        if item not in self._inventory:
            raise ValueError(f"Элемент '{item}' не найден")
        item_index = self._inventory.index(item)
        return Player(self._inventory[:item_index] + self._inventory[item_index + 1 :])

    def clear(self) -> Player:
        return Player([])

    def has_item(self, item: str) -> bool:
        return item in self._inventory
