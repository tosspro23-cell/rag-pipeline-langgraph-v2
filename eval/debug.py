def print_results(results):
    print("\n=== RETRIEVAL RESULTS ===")
    for i, doc in enumerate(results["documents"][0], 1):
        print(f"\n[{i}]")
        print(doc[:500])
    print("\n========================\n")
