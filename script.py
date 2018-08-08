import sys
import turicreate as tc

print("[1] Boosted decision tree\n"
      "[2] Decision tree\n"
      "[3] Nearest neighbour\n")

try:
    num = int(input("Select ML Algorithm: "))

    if not num or num < 1 or num > 3:
        print("\nError: Please select a number between 1 to 3.")
        sys.exit(1)


    data =  tc.SFrame('dataset.csv')
    train_data, test_data = data.random_split(0.8)

    if num == 1:
        model = tc.boosted_trees_classifier.create(train_data, target='Result', max_iterations=2, max_depth = 3)
    elif num == 2:
        model = tc.decision_tree_classifier.create(train_data, target='Result')
    else:
        model = tc.nearest_neighbor_classifier.create(train_data, target='Result')

    predictions = model.classify(test_data)
    results = model.evaluate(test_data)


    print("\n\n\n>>> Accuracy         : %s" % results['accuracy'])

except ValueError:
    print("\nError: Please select a number between 1 to 3.")
    sys.exit(1)
