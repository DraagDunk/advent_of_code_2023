import re
from utils import Assignment, load_list_of_strings

RED = "red"
GREEN = "green"
BLUE = "blue"

class SecondAssignment(Assignment):
    number = 2

    @property
    def second_path(self):
        return self.first_path

    def get_game_result(self, game_line):
        res_dict = {RED: 0, GREEN: 0, BLUE: 0}
        results = game_line.split(",")
        for result in results:
            result = result.strip()
            matches = re.match(r'^(\d*) (red|green|blue)$', result)
            if matches:
                res_dict[matches.group(2)] = int(matches.group(1))
            else:
                raise Exception(f"No match found in game result '{result}'")
        return res_dict


    def get_draws(self, game_info):
        games = game_info.split(';')
        return [self.get_game_result(line) for line in games]

    def decode_game(self, line):
        match_line = re.match(r'^Game (\d*): (.*)$', line)
        game_num = match_line.group(1)
        game_info = match_line.group(2)

        return int(game_num), self.get_draws(game_info)

    def check_possible(self, game_draws, conf):
        for draw in game_draws:
            for color, num in draw.items():
                if num > conf[color]:
                    # Impossible game! Return False
                    return False
        # Made it to the end! Game possible!
        return True

    def lowest_possible(self, game_draws):
        lowest_conf = {RED: 0, GREEN: 0, BLUE: 0}
        for draw in game_draws:
            for color, num in draw.items():
                lowest_conf[color] = max(num, lowest_conf[color])
        return lowest_conf

    def cube_power(self, conf):
        return conf[RED] * conf[GREEN] * conf[BLUE]

    def main1(self, path):
        configuration = {
            RED: 12,
            GREEN: 13,
            BLUE: 14
        }
        lst = load_list_of_strings(path)
        accumulated_result = 0
        for line in lst:
            game_num, draws = self.decode_game(line)
            if self.check_possible(draws, configuration):
                accumulated_result += game_num
        return accumulated_result

    def main2(self, path):
        lst = load_list_of_strings(path)
        results = [self.decode_game(line)[1] for line in lst]
        cube_powers = []
        for result in results:
            cube_powers.append(self.cube_power(self.lowest_possible(result)))
        return sum(cube_powers)
        

assignment = SecondAssignment()
assignment.second()