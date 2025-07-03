# FUNKCJA – nie jest związana z żadnym obiektem
def greet(name: str) -> str:
    return f"Cześć, {name}!"

# KLASA z METODĄ – metoda „widzi” atrybuty instancji przez parametr self
class Counter:
    def __init__(self) -> None:
        self.value = 0          # atrybut obiektu

    def add(self, amount: int = 1) -> int:  # METODA
        """Zwiększa licznik o 'amount' i zwraca nową wartość."""
        self.value += amount
        return self.value


# --- Użycie ---
print(greet("Ania"))   # wywołanie funkcji

cnt = Counter()        # tworzymy obiekt
print(cnt.add())       # metoda: wywołanie przez obiekt (self przekazywane automatycznie)
print(Counter.add(cnt, 4))  # to samo, ale jawnie podajemy self
