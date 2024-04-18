# Real Estate Research Automation

This Python application automates the research process for identifying promising real estate investment opportunities in Sydney, Australia. It leverages the `crewai` framework to deploy agents with specialized roles in property analysis and reporting.

## Description

The script defines two main roles:
1. **Senior Property Researcher**: This agent is responsible for finding detailed information on potential investment properties in specified areas.
2. **Senior Property Analyst**: This agent summarizes the detailed property information into concise reports suitable for investors.

The agents perform tasks using the `Ollama` language model from the `langchain_community.llms` and tools from `crewai_tools` to enhance their research capabilities.

## Configuration

Used my own API key from serper.dev to use the SerperDevTool. 

## Output

The agents' activities are logged in detail, and the outputs of their tasks are saved to text files:

task1_output.txt: Detailed property data for investment analysis.
task2_output.txt: Summarized property reports for quick review.
Contributing

Feel free to fork this repository and submit pull requests to enhance the functionality or add new features.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Disclaimer

This tool is for educational and research purposes only. Always verify your data with official sources.

---

Author : Sudarshan Krishnan
