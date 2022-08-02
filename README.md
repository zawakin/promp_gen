# Prompt Engineering

A python package for automating your Prommpt Engineering workflows.

## ⌛️ Installation

```bash
pip install prompt_gen
```

## 🎛 API

### <kbd>class</kbd> `PromptGenerator`

An instance of `PromptGenerator`, initialized with the default config. Useful as a quick
shortcut if you don't need to customize initialization.

```python
from prompt_gen import PromptGenerator
prompt_model = PromptGenerator()
```

| Argument       | Type      | Description                                                                                             | Default |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------- | ------- |
| `styles`       | List[str] | Styles such as fauvism, cubism or abstract                                                              | `False` |
| `perspectives` | List[str] | Perspectives about the image prompt such as the angle which the shot has been taken in `[from behind]`. | `False` |
| `vibes`        | List[str] | Vibes are a way to add a look/theme to your image prompts.                                              | `False` |
| `boosters`     | List[str] | Boosters are an alternative way to add a look/theme to your image prompts.                              | `False` |
| `formats`      | List[str] | Formats include `[oil painting`, `photo-realistic`, `cartoon drawing]` etc.                             | `False` |
| `characters`   | List[str] | Characters such as `['Mickey Mouse', 'Donald Duck']`                                                    | `False` |
| `scenarios`    | List[str] | Actions that your characters are taking such as `['Rowing', 'Swimming', 'Eating some food']`            | `False` |
| `locations`    | List[str] | A list of locations such as `['New York', 'Big Ben']`                                                   | `False` |
| **RETURNS**    | `Printer` | The initialized PromptGenerator.                                                                        | -       |

If you don't include any of the arguments above, then defaults will be included within your image prompts.

## Resources:

- Prompt Generator: https://docs.google.com/spreadsheets/d/1TWYoCaPVPllyoZyjOhnPeojfzgTbppMDhpK_r87-duM/edit
- Art Movements: https://artsandculture.google.com/category/art-movement?hl=en-GB
- Artists: https://artsandculture.google.com/category/artist?hl=en-GB

---

# Different parts of what makes a good prompt for AI:

## Locations:

- Cities
- Made up environments
- Important landmarks

---

## Characters:

- Animals
- Characters from Films (Star Wars, The Matrix)
- Characters from TV Shows (Friends, The Simpsons)
- Characters from Books (Harry Potter, The Lord of the Rings)
- Characters from Comics (Star Wars, The Matrix)

---

## Styles:

These include for example `abstract` or `cartoon` etc.

---

## Perspectives:

These include for example `from behind`, `from above`, `from the side` etc.

---

## Vibes/Boosters act as a style:

Vibes/Boosters are a different way to describe the style.
