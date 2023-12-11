def load_list_of_strings(path):
    file = open(path, 'r')
    return file.read().split("\n")

class Assignment:
    number = 0
    
    @property
    def str_num(self):
        return str(self.number).rjust(2, '0')

    @property
    def root_path(self):
        return f"data/{self.str_num}/"

    @property
    def test_path(self):
        return f"{self.root_path}/test.txt"

    @property
    def first_path(self):
        return f"{self.root_path}/input1.txt"

    @property
    def second_path(self):
        return f"{self.root_path}/input2.txt"

    def main(self, path):
        print("NOT IMPLEMENTED")

    def main1(self, path):
        self.main(path)

    def main2(self, path):
        self.main(path)

    def test(self):
        result = self.main(self.test_path)
        print(f"Test result:   {result}")

    def first(self):
        result = self.main1(self.first_path)
        print(f"First result:  {result}")

    def second(self):
        result = self.main2(self.second_path)
        print(f"Second result: {result}")

    def run_all(self):
        self.test()
        self.first()
        self.second()