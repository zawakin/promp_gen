import json
import pandas as pd
from typing import List
import random
from util import _validate_all_inputs_are_strings_in_a_list_and_not_empty


class PromptGenerator():
    def __init__(self, styles: List[str] = None, perspectives: List[str] = None, vibes: List[str] = None,
                 boosters: List[str] = None, formats: List[str] = None,
                 characters: List[str] = None, scenarios: List[str] = None, locations: List[str] = None):
        """A prompt engine to help with your image prompt creation ideas for DALLE-2, MidJourney and other tools.

        Args:
            characters (List[str], optional): A list of characters. Defaults to None.
            scenarios (List[str], optional): A list of actions that your characters are doing. Defaults to None.
            vibes (List[str], optional): A list of words to give your prompts a specific vibe. Defaults to None.
            boosters (List[str], optional): A list of words to give your prompts boosts. Defaults to None.
            perspectives (List[str], optional): A list of perspectives that the image will be captured in. Defaults to None.
            locations (List[str], optional): A list of locations (these could include famous landmarks, countries etc.). Defaults to None.
            formats (List[str], optional): A list of art formats (i.e. oil painting, photo-realistic). Defaults to None.
            styles (List[str], optional): _description_. Defaults to None.
        """

        # Importing vibes/boosters, styles, perspectives and formats:
        self.prompt_generator_data = self.import_prompt_data()
        if styles is None:
            self.styles = self.prompt_generator_data['styles']
        else:
            self.styles = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                styles)

        if perspectives is None:
            self.perspectives = self.prompt_generator_data['perspectives']
        else:
            self.perspectives = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                perspectives)
        if vibes is None:
            self.vibes = self.prompt_generator_data['vibes']
        else:
            self.vibes = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                vibes)
        if boosters is None:
            self.boosters = self.prompt_generator_data['boosters']
        else:
            self.boosters = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                boosters)
        if formats is None:
            self.formats = self.prompt_generator_data['formats']
        else:
            self.formats = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                formats)
        if characters is None:
            with open('prompt_gen/character_data/characters.json') as f:
                self.characters = json.load(f)
        else:
            self.characters = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                characters)
        if scenarios is None:
            with open('prompt_gen/scenario_data/scenarios.json') as f:
                self.scenarios = json.load(f)
        else:
            self.scenarios = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                scenarios)
        if locations is None:
            with open('location_data/landmarks.json') as f:
                self.locations = json.load(f)
        else:
            self.locations = _validate_all_inputs_are_strings_in_a_list_and_not_empty(
                locations)

    def import_prompt_data(self):
        with open('prompt_gen/prompt-generator.json', 'r') as f:
            return json.load(f)

    @property
    def landmarks(self) -> List[str]:
        with open('prompt_gen/location_data/landmarks.json') as f:
            return json.load(f)

    @property
    def cities(self) -> List[str]:
        return pd.read_csv('prompt_gen/location_data/cities.csv')['city'].tolist()

    @property
    def backgrounds(self) -> List[str]:
        with open('prompt_gen/location_data/backgrounds.json') as f:
            return json.load(f)

    def get_random_index(self, list_to_choose_from: list) -> int:
        """
        Returns a random index from a list.
        """
        return int(len(list_to_choose_from) * (random.random()))

    # Add the get_random_style, get_random_perspective, get_random_vibe, get_random_booster, get_random_format methods here
    def get_random_style(self) -> str:
        return self.styles[self.get_random_index(self.styles)]

    def get_random_perspective(self) -> str:
        return self.perspectives[self.get_random_index(self.perspectives)]

    def get_random_vibe(self) -> str:
        return self.vibes[self.get_random_index(self.vibes)]

    def get_random_booster(self) -> str:
        return self.boosters[self.get_random_index(self.boosters)]

    def get_random_format(self) -> str:
        return self.formats[self.get_random_index(self.formats)]

    def get_random_city(self) -> str:
        return self.cities[self.get_random_index(self.cities)]

    def get_random_landmark(self) -> str:
        return self.landmarks[self.get_random_index(self.landmarks)]

    def get_random_character(self) -> str:
        with open('prompt_gen/character_data/characters.json') as f:
            characters = json.load(f)
        return random.choice(characters)

    def get_random_scenario(self) -> str:
        with open('prompt_gen/scenario_data/scenarios.json') as f:
            scenarios = json.load(f)
        return random.choice(scenarios)

    def get_random_location(self) -> str:
        return random.choice(self.backgrounds)

    def generate_single_prompt(self, vibe: str = None, booster: str = None, perspective: str = None,
                               location: str = None, character: str = None, scenario: str = None, format: str = None,
                               use_vibe: bool = False, use_perspective: bool = False, use_booster: bool = False) -> str:
        """Generates a prompt based on the prompts in the prompt-generator.json file. If you do not provide any of the formats, then by 
        default all of them will be included. However vibe, perspective, booster are optional and if you want to use them, then remember to set `True`
        for the use_vibe, use_perspective, use_booster arguments.

        Args:
            vibe (str, optional): A vibe to improve your image prompt. Defaults to None.
            booster (str, optional): A booster to improve your image prompt. Defaults to None.
            perspective (str, optional): A perspective such as 'From behind', often this is associated with a camera angle. Defaults to None.
            location (str, optional): A location such as 'Big Ben' . Defaults to None.
            character (str, optional): A character such as 'Donald Duck'. Defaults to None.
            scenario (str, optional): A scenario of what your character is doing, i.e. 'swimming' or 'dancing' . Defaults to None.
            format (str, optional): A format of the image prompt such as 'oil painting' or 'photo-realistic'. Defaults to None.
            use_vibe (bool, optional): A boolean to opt into adding a vibe to your image prompt. Defaults to False.
            use_perspective (bool, optional): A boolean to opt into adding a perspective to your image prompt. Defaults to False.
            use_booster (bool, optional): A boolean to opt into adding a booster to your image prompt. Defaults to False.

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            str: _description_
        """
        if character is None:
            raise ValueError(
                'Please provide a character to generate a prompt.')

        if scenario is None:
            raise ValueError(
                'Please provide a scenario to generate a prompt.')

        # Generating the initial prompt:
        prompt = f"{character} {scenario}"

        # Get a random location:
        location_functions = [
            self.get_random_location,
            self.get_random_city,
            self.get_random_landmark
        ]

        params = {'location': location, 'perspective': perspective, 'format': format,
                  'vibe': vibe, 'booster': booster, }
        for key, value in params.items():
            if value is not None:
                if key == 'location':
                    prompt += f" in {value}"
                elif key == 'perspective':
                    if use_perspective:
                        prompt += f" in a {value} perspective"
                elif key == 'format':
                    prompt += f" in the format of a {value}"
                elif key == 'vibe':
                    if use_vibe:
                        prompt += f" {value}"
                elif key == 'booster':
                    if use_booster:
                        prompt += f" {value}"
                else:
                    prompt += f" {value}"
            else:
                if key == 'location':
                    prompt += f" at {random.choice(location_functions)()}"
                elif key == 'vibe':
                    if use_vibe:
                        prompt += f" {self.get_random_vibe()}"
                elif key == 'booster':
                    if use_booster:
                        prompt += f" {self.get_random_booster()}"
                elif key == 'perspective':
                    if use_perspective:
                        prompt += f" in a {self.get_random_perspective()} perspective"
                elif key == 'format':
                    prompt += f" in the format of a {self.get_random_format()}"

        return prompt.lower().capitalize()

    def generate_random_prompts(self,
                                characters: List[str] = None,
                                scenarios: List[str] = None,
                                vibes: List[str] = None,
                                boosters: List[str] = None,
                                perspectives: List[str] = None,
                                locations: List[str] = None,
                                formats: List[str] = None,
                                number_of_prompts: int = 10) -> List[str]:
        """A function to generate a list of random prompts.

        Args:
            characters (List[str], optional): A list of characters. Defaults to None.
            scenarios (List[str], optional): A list of actions that your characters are doing. Defaults to None.
            vibes (List[str], optional): A list of words to give your prompts a specific vibe. Defaults to None.
            boosters (List[str], optional): A list of words to give your prompts boosts. Defaults to None.
            perspectives (List[str], optional): A list of perspectives that the image will be captured in. Defaults to None.
            locations (List[str], optional): A list of locations (these could include famous landmarks, countries etc.). Defaults to None.
            formats (List[str], optional): A list of art formats (i.e. oil painting, photo-realistic). Defaults to None.
            number_of_prompts (int, optional): How many prompts you want to generate, be aware that if you do too many it might take too long. Defaults to 10.

        Returns:
            List[str]: Returns a list of string prompts.
        """
        # Loop over all of the arguments and see if any are none then use the self.
        # If all are none, then use the self.
        if characters is None:
            characters = self.characters
        if scenarios is None:
            scenarios = self.scenarios
        if vibes is None:
            vibes = self.prompt_generator_data['vibes']
        if boosters is None:
            boosters = self.prompt_generator_data['boosters']
        if perspectives is None:
            perspectives = self.prompt_generator_data['perspectives']
        if locations is None:
            if self.locations is None:
                with open('location_data/landmarks.json') as f:
                    locations = json.load(f)
            else:
                locations = self.locations
        if formats is None:
            formats = self.prompt_generator_data['formats']

        # Generate X prompts, randomy using parameters:
        prompts = []
        for i in range(number_of_prompts):
            prompt = self.generate_single_prompt(
                character=random.choice(characters),
                scenario=random.choice(scenarios),
                vibe=random.choice(vibes),
                booster=random.choice(boosters),
                perspective=random.choice(perspectives),
                location=random.choice(locations),
                format=random.choice(formats)
            )
            prompts.append(prompt)
        return prompts
