import evaluate


def main():
    print("Input expression.")

    expression = input(">>> ")
    answer = evaluate.evaluate(expression)

    print(f"Answer: {answer:g}")


if __name__ == "__main__":
    main()
