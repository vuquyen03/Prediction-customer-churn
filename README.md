# Applied_stat
We recognize that in file csv, we have imbalanced data ("Churn", "Not churn"). So we have some methods to deal with that problem
	Method 1: Undersampling or Oversampling

	Method 2: Using machine learning models like
		+ Decision tree
		+ Random forests
		+ ExtraTreesClassifier
		+ SVMs
		+ KNN
		+ Naive Bayes
		+ LightGBM


LightGBM is fast, distributed, high performance gradient boosting framework based on decision tree algorithm. It can lead to overfitting if it has too many layers. LightGBM enables to efficiently handle large and imbalanced datasets with many features.

# OUTLITER DETECTION
We choose upper_replace_value equal to 3 and lower_replace_value = -3 when finding outlier because with large dataset 99.7% of values lie between -3 and 3 standard deviations and normal distribution is symmetric around the mean

	A z-score is used in many real-life applications, such as medical evaluations, test scoring, business decision-making, and investing and trading opportunity measurements
	+ Khi dữ liệu có phân phối chuẩn (normal distribution) và không bị outlier quá nhiều, thì phương pháp Z-score có thể được sử dụng để xác định outlier
	+ Phương pháp IQR thường được sử dụng để xác định outlier trong trường hợp dữ liệu có phân phối không chuẩn, bao gồm cả dữ liệu có đuôi dài hay bimodal distribution

Why 1.5 times IQR? Why not 1 or 2 or any other number?

# TRAINING MODEL
We tried to predict and analyzed Customer Loss with classification algorithms. Logistic Regression, DecisionTree, Random Forest, AdaBoostClassifier, KNN, Gaussian Naive Bayes, XGBOOST, Gradient Boost, LightGBM algorithms was used

A random forest is simply a collection of decision trees whose results are aggregated into one final result.
Decision Tree có xu hướng overfitting khi tập dữ liệu lớn, còn Random Forest có khả năng giảm thiểu overfitting bằng cách kết hợp nhiều cây quyết định độc lập

# Model reviews
`classification_report`

Precision (positive) = TP/(TP+FP)
Recall Score = TP / (FN + TP)
F1-score = 2 * (precision * recall) / (precision + recall)

The ROC curve illustrates how well a model can distinguish between positive and negative samples across different decision thresholds. A perfect model would have an ROC curve that passes through the upper left corner of the graph, indicating both high sensitivity and high specificity
