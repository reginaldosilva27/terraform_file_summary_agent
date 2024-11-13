#!/usr/bin/env python
import sys
from terraform_file_summary_agent.crew import TerraformFileSummaryAgentCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'directory_path': '/Users/reginaldosilva/Documents/Datainaction/ExportDatabricks',
        'output_file_path': '/Users/reginaldosilva/Documents/Datainaction/terraform_file_summary_agent/'
    }
    result = TerraformFileSummaryAgentCrew().crew().kickoff(inputs=inputs)

    # Listar todas as propriedades do CrewOutput para entender o que está disponível
    print(">>>>>>>>>>>>>>>>>> Costs <<<<<<<<<<<<<<<<<")
    costs = 0.150 * (result.token_usage.prompt_tokens + result.token_usage.completion_tokens) / 1_000_000
    print(f"Total costs: ${costs:.4f}")
    print(result.token_usage)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'directory_path': 'sample_value',
        'output_file_path': 'sample_value'
    }
    try:
        TerraformFileSummaryAgentCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TerraformFileSummaryAgentCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'directory_path': 'sample_value',
        'output_file_path': 'sample_value'
    }
    try:
        TerraformFileSummaryAgentCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
