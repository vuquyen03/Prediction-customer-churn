Có thể mô tả một quá trình giải quyết bài toán machine learning như sau :

	+ Phân tích dữ liệu
	+ Thử các mô hình (thử có định hướng sau khi giả định về tính chất dữ liệu, hoặc thử tất cả các phương pháp có thể)
	+ Finetune lại mô hình để tìm ra các tham số tốt nhất
	+ Đánh giá kết quả
	+ Quay lại bước 1 nếu kết quả đánh giá không tốt =))
Tất cả các thao tác trên bản chất là xoay quanh để giải quyết vấn đề giữa bias và variance (bias-variance trade off).

# Introduction
Churn prediction is one of the most popular Big Data use cases in business. It consists of detecting customers who are likely to cancel a subscription to a service.

This project is a binary classification problem. If we focus on company goals, actually our problem is losing customers. In this situation the company needs to find churned customer in other words the customers that we will lose. Thus, the company will avoid losing profit and revenue.
		

# Preprocessing (Data Cleaning)
	+ Remove columns with many missing values including `"HandsetPrice", "MaritalStatus", "AgeHH2"`
	+ Remove columns with a single unique value
	+ Remove unnecessary dât fields including `"CustomerID", "ServiceArea"`
	+ The median is the middlemost value. It’s better to use the median value for imputation in the case of outliers.

# Data analysis
When we analyze our data, we see that our dataset was imbalanced. The majority class, "Not churn"(0) has around 71.2% and the minority class "Churn" (1) is around 28,8%

We use KDE for some attributes having null values. KDE (kernel density estimator) is a statical method using for PDF (Probability Density Function). The KDE diagram is often used to describe the distribution of a variable and helps us understand how that variable is distributed across its entire range of values. It provides an overall view of the shape of the distribution and allows us to identify important features of the distribution such as skewness, kurtosis, and spread.

## OUTLIER DETECTION
We choose upper_replace_value equal to 3 and lower_replace_value = -3 when finding outlier because with large dataset 99.7% of values lie between -3 and 3 standard deviations and normal distribution is symmetric around the mean

A z-score is used in many real-life applications, such as medical evaluations, test scoring, business decision-making, and investing and trading opportunity measurements
	+Khi dữ liệu có phân phối chuẩn (normal distribution) và không bị outlier quá nhiều, thì phương pháp Z-score có thể được sử dụng để xác định outlier
	+Phương pháp IQR thường được sử dụng để xác định outlier trong trường hợp dữ liệu có phân phối không chuẩn, bao gồm cả dữ liệu có đuôi dài hay bimodal distribution

Why 1.5 times IQR? Why not 1 or 2 or any other number?

# TRAINING MODEL

We recognize that in file csv, we have imbalanced data ("Churn", "Not churn"). So we have some methods to deal with that problem

	Step 1: Undersampling or Oversampling

	Step 2: We tried to predict and analyzed Customer Loss with classification algorithms.
		+ Decision tree
		+ Random forests
		+ Adaboost (should not be complex, typically highly biased classifiers)
		+ XGBoost

We use 2 models related to Boosting - Adaboost, XGboost
Boosting tries to minimal bias --> increase variance (because of bias-variance tradeoff)

A random forest is simply a collection of decision trees whose results are aggregated into one final result.
Decision Tree có xu hướng overfitting khi tập dữ liệu lớn, còn Random Forest có khả năng giảm thiểu overfitting bằng cách kết hợp nhiều cây quyết định độc lập
Precision (positive) = TP/(TP+FP)
Recall Score = TP / (FN + TP)
F1-score = 2 * (precision * recall) / (precision + recall)

The ROC curve illustrates how well a model can distinguish between positive and negative samples across different decision thresholds. A perfect model would have an ROC curve that passes through the upper left corner of the graph, indicating both high sensitivity and high specificity

# Precision Recall Curve
One of the best methods for tuning a model for a business need is through the precision recall curve. This shows the precision-recall tradeoff for different thresholds. Depending on the business requirement, we can change the threshold for classifying a positive example to alter the balance of true positives, false positives, false negatives, and true negatives. There will always be a tradeoff between precision and recall, but we can try to find the right balance by visually and quantitatively assessing the model.

Để đánh giá hiệu suất của mô hình trên tập dữ liệu mới, chúng ta nên sử dụng tập kiểm tra được chọn ngẫu nhiên bằng hàm train_test_split.

# Discussion

# Conclusion