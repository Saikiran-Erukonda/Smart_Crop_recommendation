# **🌱:Smart Crop recommendation system🌱.**
 
 **Enhancing crop selectivity based on assessing the conditions suitable for the crop. 
Independent features**
- N
- P
- K
- temperature
- humidity
- ph
- rainfall

Dependent feature
- label (crop)
### Models and their performance Metrics
| Metrics  | Logical_Regression | Decision Tree |
|----------|--------------------|---------------|
| Precision | 0.963636 |0.986111 |
| Accuracy | 0.963636 |0.986364 |
| F1 Score | 0.963636  |0.986364 |
| Recall   |0.963636  |0.987287 |

+ Here, Decision Tree model is performing better than Logistic regression model in predicting the suitable crop. Hence, we need to proceed with Decision Tree Model.

### **Steps to run Smart Crop Recommendation System -- run a Interactive Dashboard**

1. Once you download whole repository. Extract the folder `Smart_Crop_recommendation` from Zip file.

2. Open command prompt. Navigate to the above mentioned folder.

3. Run below command
   ``` bash
   streamlit run streamlit_app.py
   ```
   Note : make sure you have this streamlit library in your PC. The way to install it is shown below.
   ``` bash
   !pip install streamlit
   ```
4. An interactive Dashboard will be displayed in your default web browser. Open the web browser, monitor the input parameters and observe the suitable Crop which can be grown in those environmental conditions. 
