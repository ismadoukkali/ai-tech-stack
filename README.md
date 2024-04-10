# AI Technology Extractor from Job Descriptions

This Python utility extracts technology names from job descriptions, specifically focusing on identifying the applications and tools mentioned. This can be particularly useful for understanding the tech stack a company uses based on their job postings.

## Prerequisites

Before you can use this script, you need to have an OpenAI API key. This key should be stored in an `.env` file with the key name `OPENAI_API_KEY`. This is crucial for the script to authenticate and make requests to the OpenAI API.

## Setup

1. Ensure you have Python installed on your machine.
2. Install the required packages, if not already installed:
    - `openai`
    - `dotenv` (for loading the `.env` file)
    - `json` (should be included with Python)

3. Create an `.env` file in the root directory of this project, and add your OpenAI API key as follows:
    ```env
    OPENAI_API_KEY=your_api_key_here
    ```

4. You might need to install other dependencies related to handling HTTP requests or environmental variables based on your setup or modifications to this script.

## How It Works

The `extract_technologies` function in the script takes a job description as input and uses a predefined OpenAI model to analyze and extract technologies mentioned within the text. The process involves sending the job description to the model, which is then interpreted to identify mentions of applications or technologies.

### Key Functionality

- **Extracting Application Companies**: Identifies companies or tools mentioned within a job description that are part of the company's tech stack.
- The function utilizes a structured prompt sent to the OpenAI API, expecting a list of technologies as the output.

### Example Usage

You can call the `extract_technologies` function with a string containing a job description. Here's an example:

```python
job_description = """Insert the job description here"""
technologies = extract_technologies(job_description)
print("Technologies used at company:", technologies)

```

Replace """Insert the job description here""" with the actual job description you want to analyze.

### Important Notes
The accuracy of the technology extraction is highly dependent on the quality of the input text and the current capabilities of the OpenAI model being used.

This tool is designed for informational purposes and should be used as a guide rather than an absolute source of truth.

### Contribution
Your contributions are welcome! If you have suggestions for improvement or have found bugs, please open an issue or pull request.


