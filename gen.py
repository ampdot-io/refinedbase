#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#     "requests",
#     "fire",
#     "boto3",
#     "cuid2",
# ]
# ///

import requests, fire, boto3
from cuid2 import cuid_wrapper

new_cuid = cuid_wrapper()

def main(prefix: str, max_tokens, prompt="", n=10, times=1000, port=5001):
    data = {"prompt": "", "n": 10, "max_tokens": max_tokens, "temperature": 0, "top_p": 0}
    for i in range(times):
        response = requests.post(f"http://localhost:{port}/v1/completions", json=data)
        with open(f'{prefix}-{new_cuid()}.json', 'wb') as f:
            f.write(response.content)


fire.Fire(main)
