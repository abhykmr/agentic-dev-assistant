from agents.dev_agent import create_agent


def main():

    agent = create_agent()   # IMPORTANT: parentheses

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            break

        response = agent.run(user_input)

        print("\nAgent:", response)


if __name__ == "__main__":
    main()