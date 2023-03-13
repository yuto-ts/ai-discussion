import os
from os.path import join, dirname
from dotenv import load_dotenv
import openai
import json
import time
from pprint import pprint

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Person:

    def __init__(self, profile: dict) -> None:

        openai.api_key = os.environ.get("API_KEY")
        self.use_openai_model = "gpt-3.5-turbo"

        self.name = profile["name"]
        self.listen_text = ""
        self.response = ""

        print(f"SETUP {self.name}")

        self.personality = self._create_personality(profile)

        print("SETUP COMPLETE")
        print(
            "---------------------------------------------------------------------"
        )

    def _create_personality(self, profile: dict):
        personality = {
            "memories": [{
                "role": "system",
                "content": profile["system_content"]
            }]
        }
        return personality

    def _send_message_to_llm(self, message: str) -> str:

        messages = self.personality["memories"]

        [{"role": "user", "content": message}]
        response = openai.ChatCompletion.create(model=self.use_openai_model,
                                                messages=messages)
        return response["choices"][0]["message"]["content"]

    def listen(self, text: str):
        self.personality["memories"].append({
            "role": "user",
            "content": text,
        })
        self.listen_text = text

    def think(self):
        # print("THINKING...")
        self.response = self._send_message_to_llm(self.listen_text)

    def talk(self) -> str:
        self.personality["memories"].append({
            "role": "assistant",
            "content": self.response,
        })
        print(f"{self.name}: {self.response}\n")
        return self.response
