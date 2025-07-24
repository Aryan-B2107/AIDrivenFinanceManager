This module does the job of analyzing past user behavior and presenting insights.

Development Roadmap:
Build models to store summarized financial data (optional; can be computed live).
Create chart and stats endpoints:
Monthly expense by category
Year-over-year comparison
Savings trend
Budget vs Actual

Add logic for generating reviews:
Monthly: “You spent 25% more on food this month”
Weekly: “Good job saving 15% of your income”
Add recommendation engine:
Suggest new budget allocations based on past behavior.
Recommend savings plans for large upcoming purchases.
Hook into finance module as a data source.

Optional: Cache insights using Redis for faster access.