# case_study1_tractor
Estimate the pricing of used tractors


## Overview
The goal of this case study is to predict the sale price of a particular piece
of heavy equipment
at auction based on it's usage, equipment type, and configuration.
The data is sourced from auction result postings and includes information
on usage and equipment configurations.
One restriction we had was that we need to use regressions only
(Linear/Logistic regression, Regularizations (Lasso, Ridge)).

## Data
There are 52 features and 400,000 observations in the data set.
Cleaning was done to account for missing and improperly entered data.
Columns with too many NaNs were removed from our analysis.

Features that are not useful for predicting the tractor price include Data source, transmission, blade extension, engine horsepower, hydraulics, drive system, usage band.

## Model and analysis
We used linear regression which seems to give the best result.
We initially dummified the Model ID column (categorical) which yielded 5000 extra columns. We achieved R-square of 0.84. Therefore, we can say that the Model-ID is a strong predictor. Hoewever, due to large # of columns we faced with a computational limitation since the results are due by the end of the day. Therefore, we did not include the dummified Model-ID columns.

The Final features we used to predict the sale price are
1. YearMade,
2. MachineHoursCurrentMeter.
3. Age(SaleYear-YearMade)
4. ProductGroup (dummified -- total 6 cols)
5. ProductSize (dummified -- total 5 cols)

WE obtained the Rsquared value of 0.36.
