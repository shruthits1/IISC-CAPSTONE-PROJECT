# Project 4
Domain: Financial Services
Techniques: NLP, Conversational AI, ML, LLMs
## Title: Personal AI Financial Advisor for Retail Clients

### Overview and Problem Statement:
Retail clients often lack affordable and accessible personalized financial advice, leading to challenges in goal-based financial planning, insurance advisory, and portfolio management.This project focuses on developing a conversational AI system powered by LLMs to address
these issues. The system will provide tailored financial recommendations, bridging the financial literacy gap and empowering users to make informed decisions.

### Specific Challenges:
-  Handling diverse user demographics and financial goals.
-  Integrating real-time financial market data into conversational AI.
-  Ensuring regulatory compliance and data security.

### Data Description:
#### Financial Planning Dataset:
- Includes user demographics, financial goals, income, expenditure, and portfolio details.
○ Source: Simulated datasets or publicly available financial datasets (e.g.,Kaggle, UCI Repository).
(https://www.kaggle.com/datasets/bukolafatunde/personal-finance/data)
(https://www.kaggle.com/datasets/abhilashayagyaseni/personal-financedataset/data)
#### Conversational Data:
- Pre-trained datasets like Microsoft Dialogue Corpus fine-tuned for financial use cases.
○ Source: (https://github.com/emilyallaway/zero-shotstance/tree/master/data)
#### Insurance and Financial Products Dataset:
- Coverage options, premiums, real-time stock prices, and market trends (https://www.kaggle.com/datasets/mrmorj/insurancerecommendation/data. 
- Insurance Dataset: (https://github.com/AntonUBC/Prudential-Life-InsuranceAssessment/tree/master/data/data)
The Description of each variable in the dataset is given below.
Id- A unique identifier associated with an application; Product_Info_1-7- A set of normalized variables relating to the product applied for; Ins_Age- Normalized age of applicant; Ht- Normalized height of applicant; Wt- Normalized weight of applicant;
BMI- Normalized BMI of applicant; Employment_Info_1-6- A set of normalized variables relating to the employment history of the applicant; InsuredInfo_1-6- A set of normalized variables providing information about the applicant; Insurance_History_1-9- A set of normalized variables relating to the insurance history of the applicant; Family_Hist_1-5- A set of normalized variables relating to the family history of the applicant; Medical_History_1-41- A set of normalized variables relating to the medical history of the applicant; Medical_Keyword_1-48- A set of dummy variables relating to the presence of/absence of a medical keyword being associated with the application; Response- This is the target variable, an ordinal variable relating to the final decision associated with an application.
#### Alpha Vantage Financial Market Data:  
Alpha Vantage is a provider of financial market data APIs that offer real-time and historical data for various financial instruments such as stock prices, technical indicators, sector performance, exchange rates, and more. This data should be utilized to train and fine-tune the Large Language Model (LLM). Real-time financial data and market news and trends should be incorporated to provide current and accurate financial advice.
○ Source: Alpha Vantage (https://www.alphavantage.co/)

### Methodology:
- Extract user demographics, financial goals, income, and portfolio details; clean and normalize datasets.
-  Fine-tune pre-trained LLMs using financial dialogue datasets to understand queries like "How can I save for retirement?" or "Should I invest in bonds?"
-  Train ML models (e.g., Random Forest, XGBoost) to provide goal-based financial advice and insurance recommendations.
-  Incorporate real-time market data from Alpha Vantage for contextual recommendations.
-  Build a mobile-friendly conversational AI tool with personalized goal planning and portfolio analysis features. 

### Project Deliverables:
1. A conversational AI system capable of engaging retail clients with financial advisory discussions.
2. Goal-planning recommendations based on user profiles and inputs.
3. A portfolio analysis tool with actionable suggestions for re-alignment.
4. Integration of insurance advisory into the conversational system.
   
### Applications:
This project democratizes financial advisory services, enabling personalized financial planning, portfolio optimization, and insurance recommendations at scale.

### References:
-  "Integrating Modern Conversational AI Architectures in FinTech: Advancements,
Applications, and Challenges." (https://www.ijert.org/research/integrating-modernconversational-ai-architectures-in-fintech-advancements-applications-andchallenges-IJERTV13IS070017.pdf)
-  "AI-Driven Financial Analysis: Exploring ChatGPT’s Capabilities and Challenges."
(https://www.researchgate.net/publication/380873806_AIDriven_Financial_Analysis_Exploring_ChatGPT's_Capabilities_and_Challenges) 
