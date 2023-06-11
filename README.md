# us-civics-quiz
Playground to generate quiz for the Civics portion of the US citizenship exam

## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)

## Description

This repo contains a couple of notebooks using LangChain and ChatGPT to simulate a full text interview to help study for the civics section of the US citizenship interview. It can help parse the pdf of questions in to well formatted data, and provide an interface for users to answer the questions in a natural language sentence structure and check if the answer is close to the provided answers.

## Features

The code here has 2 parts:
1. Data collection: Located in [this](Parse%20civics%20quesion.ipynb) notebook. The code here parse the provide pdf and uses chatGPT to generate the formatted question/answer pairs in data.json
2. Quiz: Contains both a [notebook](Civics%20question%20quiz.ipynb) and a [script](main_quiz.py). It will ask the user one of the question from data.json at random (without repeating questions), and uses ChatGPT to judge if the answer is close enough to the provided answer. 


## Installation

Written in python 3.11

Install dependencies with

```
pip install -r requirements.txt
```

## Usage

Get an [OpenAI token](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) 

You can run the quiz in the notebook after setting the token in your environement variable

```
export OPENAI_API_KEY=<token>
```

Alternatively, run the script provided:

```
OPENAI_API_KEY=<token> python main_quiz.py
```


## Contributing

Thank you for considering contributing to this project! Contributions are welcome and appreciated. To contribute, please follow these guidelines:

1. Fork the repository and create your branch from `main`.
2. Make your changes, documenting any necessary information or updates.
3. Ensure that your code adheres to the project's coding conventions and style guidelines.
4. Test your changes thoroughly.
5. Submit a pull request, clearly describing the changes you have made.

By contributing to this project, you agree to license your contributions under the [MIT License](https://opensource.org/licenses/MIT).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

You are free to use, modify, and distribute this software for any purpose. Please refer to the [LICENSE](LICENSE) file for more details.

## Contact

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/your-username/your-repo-name/issues) on the issue tracker.
