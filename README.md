# Experimenting-with-Histograms
Try different bin sizes and limits to see if that alters inference of the same dataset

## Experiment 1:
I generate data using two different distributions, say A = N(40,10) and B = N(60,10). Then try to use certain bins to hide the differences (in the trivial case just use one bin from min(data) to max(data), both histograms will have the same shape).

## Experiment 2:
I generate data using the same distribution. Then try to use certain bins to make it seem like there is a 'significant' difference in the histograms of the 2 variables.

### TODO 02/06/2021
- Make a histogram faceted by variable, with bins as a variable
- Make it using Dash components
- Make an input field for user to specify bins
- Connect input field with graph using Dash

- Have fun with the experimentation
