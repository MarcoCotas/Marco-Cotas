def main():
    item_counts = {}

    while True:
        try:
            item = input().upper()
            if item in item_counts:
                item_counts[item] += 1
            else:
                item_counts[item] = 1
                item_counts = dict(sorted(item_counts.items()))
           
        except EOFError:
            for item, count in item_counts.items():
                print(f"{count} {item}")

            break
main()
