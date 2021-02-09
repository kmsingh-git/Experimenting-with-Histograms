# Experimenting-with-Histograms
Try different bin sizes and limits to see if that alters inference of the same dataset

## Experiment 1:
Generate data using two different distributions, say A = N(40,10) and B = N(60,10). Then try to use certain bins to hide the differences (in the trivial case just use one bin from min(data) to max(data), both histograms will have the same shape).

In this case, we would have demonstrated that even if the data comes from different data generating processes (or that variable A's measurements really are different from B's measurements like guy height vs girl height in a class), we can hide that using certain bin sizes.

## Experiment 2:
Generate data using the same distribution. Then try to use certain bins to make it seem like there is a 'significant' difference in the histograms of the 2 variables.

In this case, we would have demonstrated that data from the same data generating process can be made to look different, by using certain bin sizes.

### TODO
- ~~Make a histogram faceted by variable~~
- ~~Make bins as a variable~~
- Make it using Dash components
- Make an input field for user to specify bins
- Connect input field with graph using Dash

- Have fun with the experimentation

- Share results in network (LinkedIn, Twitter) and maybe create a write-up for Medium

### Bonus features
- Explore cumulative histograms

### Weird stuff
- When creating Histogram using `go.Bar` instead of `go.Histogram`, getting slightly different results. Had to use `go.Bar` because `go.Histogram` doesn't allow bins of varying sizes I think -_- (here `go` refers to `graph_objects` in `plotly`)
