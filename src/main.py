from argparse import ArgumentParser

from ai_agent import Person


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-t",
                        "--thema",
                        required=True,
                        help="input talk thema")
    parser.add_argument("-c",
                        "--count",
                        required=True,
                        help="input talk count")
    return parser.parse_args()


def create_alice_profile():
    role = '''
    あなたは次の人物にロールプレイをしてください

    職業: 女子高生
    性別: 女性
    性格: 好奇心旺盛なギャル
    口調: 口調は明るい元気な娘。敬語はあまり使わない
    回答は基本短文で答える。
    '''
    profile = {"name": "Alice", "system_content": role}
    return profile


def create_bob_profile():
    role = '''
    あなたは次の人物にロールプレイをしてください

    職業: 大学教授
    専攻: 人口知能の研究をしている
    性別: 男性
    性格: 非常に優しく丁寧に話をするのが特徴
    '''
    profile = {"name": "Bob", "system_content": role}
    return profile


def main(talk_thema: str, talk_max_count: int):
    talk_count = 0

    alice = Person(create_alice_profile())
    bob = Person(create_bob_profile())

    alice.listen(talk_thema)
    alice.think()
    while talk_count < talk_max_count:
        bob.listen(alice.talk())
        bob.think()
        alice.listen(bob.talk())
        alice.think()

        talk_count += 1

    alice.talk()


if __name__ == "__main__":
    args = parse_args()

    main(talk_thema=args.thema, talk_max_count=int(args.count))
