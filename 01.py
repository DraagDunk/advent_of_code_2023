import re
from utils import Assignment, load_list_of_strings

class FirstAssignment(Assignment):
    number = 1

    @property
    def second_path(self):
        return self.first_path

    def get_calibration_val(self, string, with_num_strings=False):
        translation = {'1': 1, 'one': 1, '2': 2, 'two': 2, '3': 3, 'three': 3,
                       '4': 4, 'four': 4, '5': 5, 'five': 5, '6': 6, 'six': 6,
                       '7': 7, 'seven': 7, '8': 8, 'eight': 8, '9': 9, 'nine': 9}
        if with_num_strings:
            first_pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
            last_pattern = r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin'
        else:
            first_pattern = r'\d'
            last_pattern = r'\d'
        first_match = re.search(first_pattern, string)
        last_match = re.search(last_pattern, string[::-1])
        result = int(str(translation[first_match.group(0)]) + str(translation[last_match.group(0)[::-1]]))
        return result
        

    def main(self, path, with_num_strings=False):
        lst = load_list_of_strings(path)
        running_total = 0
        for line in lst:
            running_total += self.get_calibration_val(line, with_num_strings=with_num_strings)

        return running_total

    def main1(self, path):
        return self.main(path, with_num_strings=False)

    def main2(self, path):
        return self.main(path, with_num_strings=True)
            

assignment = FirstAssignment()
assignment.run_all()