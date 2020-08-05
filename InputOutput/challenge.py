with open("tables.txt", 'w') as sample_file:
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i} times {j} is {i * j}", file=sample_file)
        print("-" * 20, file=sample_file)

# for i in range(1, 13):
#     for j in range(1, 13):
#         print(f"{i} times {j} is {i * j}")
#     print()
