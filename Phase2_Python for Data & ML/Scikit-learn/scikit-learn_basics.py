from sklearn import tree

# Step 1: Collect Data
# Features: [weight (grams), color (0 = red, 1 = orange)]
features = [
    [150, 0],  # Apple
    [170, 0],  # Apple
    [130, 1],  # Orange
    [120, 1],  # Orange
]
labels = ["apple", "apple", "orange", "orange"]

# Step 2: Train a model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# Step 3: Predict!
weight=int(input("Enter the weight of the fruit in grams: "))
color=int(input("Enter 0 if the fruit is red in color and enter 1 if the fruit is orange in colour: "))
prediction=clf.predict([[weight,color]])
if color==0 or 1:
    print(f"The fruit is {prediction[0]}")
else:
    print("Invalid color code!")  