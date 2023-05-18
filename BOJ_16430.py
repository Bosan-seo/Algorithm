# 백준_16430번

def jerry_and_tom(A, B):
    return f"{B-A} {B}"


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(jerry_and_tom(A, B))