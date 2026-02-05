# Social-Media-Growth-Analysis-Threads-and-TikTok-
This project analyzes user growth data from two major social media platforms: Threads and TikTok. The goal is to distinguish between real, long-term growth and temporary "success bubble”

##  Executive Summary

This project analyzes two years of simulated user data from **TikTok** and **Threads** to distinguish sustainable growth from temporary "success bubbles". Using Spearman correlation analysis, the study found that TikTok's growth is sustainable, while Threads exhibited classic bubble patterns.

**Key Findings:**

* 
**TikTok:** High engagement correlation (0.92), 85% organic traffic, and a low churn rate (-0.15).


* 
**Threads:** High churn correlation (-0.70) and 60% paid acquisition.


* 
**Threshold for Success:** Platforms with 75-90% organic growth and strong engagement correlations (>0.85) typically achieve long-term success.



##  Dataset Description

The project analyzes daily timeline data for Threads and TikTok to identify the difference between real growth and temporary hype.

### Data Columns

* 
`date`: Daily timeline of the data.


* 
`dau`: Daily Active Users (main growth metric).


* 
`avg_session_duration_min`: Average time spent per session.


* 
`churn_rate`: Percentage of users who stop using the app.


* 
`organic_traffic_pct`: Percentage of users joining naturally.


* 
`algorithm_score` / `twitter_volatility_index`: Internal and external growth factors.



##  Project Goals

* 
**Analyze Engagement:** Determine if high DAU is supported by real time spent on the app.


* 
**Evaluate Sustainability:** Measure the role of organic traffic versus heavy advertising.


* 
**Identify Risks:** Understand how churn rates and external factors create "success bubbles".



##  Exploratory Data Analysis (EDA)

Spearman Correlation was used to measure the strength and direction of relationships between numeric metrics.

### Threads Analysis: The "Success Bubble"

* 
**Engagement Gap:** A huge spike in DAU at launch did not correlate with a significant increase in session duration, indicating users were not truly engaged.


* 
**Marketing-Driven:** A massive gap between Total DAU and Organic DAU reveals that growth was artificially inflated by external promotion.


* 
**The Death Spiral:** High churn created a "leaky bucket" effect where users left as fast as they joined.


* 
**Competitor Impact:** Competitor (Twitter/X) instability was a minor factor; the real issue was a lack of product value.



### TikTok Analysis: Sustainable Growth

* 
**Healthy Growth:** TikTok shows very strong positive correlations across all key engagement metrics, such as DAU vs. Session Duration (0.92).


* 
**Organic Discovery:** 75-90% of growth is organic, driven by user discovery and word-of-mouth rather than paid ads.


* 
**Smart Algorithm:** Improvements in algorithm efficiency (0.89 correlation with DAU) directly drive massive, sustainable growth.



## 🛠 The "Bubble Warning System" Framework

A data-driven framework developed to detect unsustainable growth in real-time.

| Signal | Metric | Warning Threshold |
| --- | --- | --- |
| **1. Organic Gap Test** | Total DAU vs. Organic DAU | Gap exceeds 30% for >14 days 

 |
| **2. Engagement-Growth Sync** | Correlation: Session Duration & DAU | Correlation drops below 0.80 for 3 weeks 

 |
| **3. Churn Acceleration** | Rate of change in churn | Churn increases by >5% week-over-week 

 |

##  Limitations & Future Research

* 
**Data Source:** This analysis uses simulated datasets modeled on industry trends from Business of Apps, Statista, and Similarweb.


* 
**Future Work:** Validating the Warning System on more platforms, integrating sentiment analysis, and developing predictive ML models.
