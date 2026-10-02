# Sustainable Growth and Launch Hype: an Exploratory Simulation Study

**Team:** Echo — Gheid Abdulkarim Abomaghara (analysis, metrics, problem solving), Rasha Abdulhameed Naji (data collection, cleaning), Elaf Hamed Alhajj (presentation, visualization)  
**Platforms:** Threads and TikTok  
**Status:** Educational exploratory analysis, not a peer-reviewed publication

## Research question

How do engagement, organic traffic and churn move alongside daily active users in two simulated growth trajectories? Can their associations motivate a future framework for distinguishing sustained growth from temporary launch hype?

## Materials and method

Two simulated datasets contain 1,005 raw rows each and deliberate quality issues. Threads includes a Twitter/X volatility index; TikTok includes an algorithm efficiency score. These are simulated explanatory variables, not official company measurements.

1. Remove duplicates, parse mixed dates, discard invalid dates and sort chronologically.
2. Drop missing Threads observations; median-impute missing TikTok DAU/churn.
3. Retain original assumptions: absolute negative churn and positive-mean replacement of non-positive DAU.
4. Calculate Spearman correlations between numeric metrics and DAU.
5. Visualize total DAU and an illustrative organic DAU proxy, with additional heatmaps and scatter plots in the notebook.

Run `python analysis.py` to reproduce [summary.json](../results/summary.json), correlation tables and the chart. Restart/run all notebook cells for the detailed original exploration.

## Interpretation

The original study frames Threads as a spike-and-decline scenario and TikTok as a growing scenario. The chart shows the included simulated trajectories. Coefficients describe association; they do not prove causal effects of engagement, advertising, algorithms or competitor instability.

![Simulated growth trajectories](../results/growth-comparison.png)

## Proposed warning framework

The original notes propose monitoring the organic gap, engagement-growth synchronization and churn acceleration. Thresholds remain hypotheses: no validation set, forecasting evaluation or working real-time warning system is included.

## Limitations and future work

- Simulated data cannot establish actual platform business performance.
- Calendar periods and scales differ; this is not a controlled comparison.
- Shared time trends and autocorrelation may inflate relationships.
- Acquisition percentages do not directly measure active-user retention; organic DAU is a proxy.
- Cleaning and imputation decisions can affect coefficients.
- Original approximate numerical claims should not replace recomputed values.
- The original Word study provides industry reference URLs, but no simulation generator is supplied.

Future work: sourced observations, a documented generator, cleaning sensitivity analysis, controls for time trends and warning-rule tests on held-out periods.

## Study history

[Original Word study](echo-study-original.docx) and [original 19-slide presentation](echo-presentation-original.pptx) are the supplied Echo team deliverables, preserved unchanged. [Original study notes](original-study-notes.md) preserve the previous README. This Markdown document describes the reproducible repository analysis. Original document figures may differ from the recomputed results; they are not independently validated platform statistics.

## الملخص العربي

تستكشف الدراسة علاقة المستخدمين النشطين يوميًا بالتفاعل والزيارات العضوية ومعدل المغادرة في بيانات محاكاة لمنصتي Threads وTikTok. تشمل تنظيف البيانات وارتباط Spearman وعرض مسارات النمو. مؤشر تقلب Twitter/X عامل خارجي في بيانات Threads. النتائج وصفية وتعليمية، ولا تثبت أداء المنصات الفعلي أو علاقات سببية. إطار التحذير من فقاعات النمو مقترح بحثي يحتاج إلى اختبار مستقل.
