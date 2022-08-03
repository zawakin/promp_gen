import pytest
from prompt_gen import PromptGenerator


@pytest.fixture
def get_prompt_model():
    return PromptGenerator()


def test_class_init_with_args(get_prompt_model):
    assert isinstance(get_prompt_model, PromptGenerator)
    assert isinstance(get_prompt_model.styles, list)
    assert isinstance(get_prompt_model.perspectives, list)
    assert isinstance(get_prompt_model.vibes, list)
    assert isinstance(get_prompt_model.boosters, list)
    assert isinstance(get_prompt_model.formats, list)
    assert isinstance(get_prompt_model.characters, list)
    assert isinstance(get_prompt_model.scenarios, list)
    assert isinstance(get_prompt_model.locations, list)
    assert len(get_prompt_model.styles) > 0
    assert len(get_prompt_model.perspectives) > 0
    assert len(get_prompt_model.vibes) > 0
    assert len(get_prompt_model.boosters) > 0
    assert len(get_prompt_model.formats) > 0
    assert len(get_prompt_model.characters) > 0
    assert len(get_prompt_model.scenarios) > 0
    assert len(get_prompt_model.locations) > 0
