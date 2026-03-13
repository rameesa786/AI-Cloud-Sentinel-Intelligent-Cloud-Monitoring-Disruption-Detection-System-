import json
import os


def verify_output():

    input_path = "../tasks/input_data.json"
    expected_path = "../tasks/expected_output.json"

    if not os.path.exists(input_path):
        return "FAIL: input_data.json not found"

    if not os.path.exists(expected_path):
        return "FAIL: expected_output.json not found"

    with open(input_path) as f:
        input_data = json.load(f)

    with open(expected_path) as f:
        expected_data = json.load(f)

    if input_data["task"] != expected_data["task"]:
        return "FAIL: task mismatch"

    return "PASS: evaluation successful"


if __name__ == "__main__":
    print(verify_output())
