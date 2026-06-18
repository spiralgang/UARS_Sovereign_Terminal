#!/usr/bin/env python3
"""
NVIDIA AI Bridge for Termux
Utilizing build.nvidia.com free endpoint for coding assistance.
"""
import os
import requests
import json
import sys

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "YOUR_FREE_NVIDIA_API_KEY")
NVIDIA_URL = "https://integrate.api.nvidia.com/v1/chat/completions"

def solve_coding_problem(query):
    headers = {
        "Authorization": f"Bearer {NVIDIA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "nvidia/llama-3.1-405b-instruct",
        "messages": [
            {"role": "system", "content": "You are a Sovereign Coding AI. Provide optimized, secure, and compliant code solutions."},
            {"role": "user", "content": query}
        ],
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024
    }

    response = requests.post(NVIDIA_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(solve_coding_problem(" ".join(sys.argv[1:])))
    else:
        for line in sys.stdin:
            print(solve_coding_problem(line.strip()))
