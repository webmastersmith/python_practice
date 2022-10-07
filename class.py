class Robot:
    def __init__(self, id_="0", name="default") -> None:
        self.id = id
        self.name = name

    def __str__(self):
        return f"{str(self.__class__)} {str(self.__dict__)}"

    def introduce_self(self):
        print(f"My name is {self.name}")


r1 = Robot(101, "Bryon")


print(r1)
