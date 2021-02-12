# Experimenting-with-Histograms
Try different bin sizes and limits to see if that alters inference of the same dataset
[Link to Dash webapp hosted on Heroku](https://experimenting-with-histograms.herokuapp.com/)

## Experiment 1:
Generate data using two different distributions, say A = N(40,10) and B = N(60,10). Then try to use certain bins to hide the differences (in the trivial case just use one bin from min(data) to max(data), both histograms will have the same shape).

In this case, we would have demonstrated that even if the data comes from different data generating processes (or that variable A's measurements really are different from B's measurements like guy height vs girl height in a class), we can hide that using certain bin sizes.

## Experiment 2:
Generate data using the same distribution. Then try to use certain bins to make it seem like there is a 'significant' difference in the histograms of the 2 variables.

In this case, we would have demonstrated that data from the same data generating process can be made to look different, by using certain bin sizes.

### TODO
- ~~Make a histogram faceted by variable~~
- ~~Make bins as a variable~~
- ~~Make it using Dash components~~
  - ~~Allow two modes, one of the type [1,34,67,100], the other specifies `start`, `end`, `stepsize` (which is easier to specify if you want uniform bins)~~
- ~~Make an input field for user to specify bins~~
- ~~Connect input field with graph using Dash~~
  - ~~Make a Submit button instead and have that trigger the update graph callback~~
- ~~Deploy on Heroku~~
- Make better ticks on x axes
- Change hover data to show intervals instead of middle points
- Update style
  - Align input fields together
  - Add personal signature in the app
  - Maybe add links to Socials (IG, LinkedIn, Twitter, Github)

- Have fun with the experimentation

- Share results in network (LinkedIn, Twitter) and maybe create a write-up for Medium

### Bonus features
- Explore cumulative histograms
- Allow user to upload data, and even more bonus - allow them to persist some amount of data? Maybe have dynamic storage and allow them to pay for it? Just the cost of storage, I can potentially pay for the server?
  - Other than this, there's no need for a server. I can just host a simple web page on Github that allows User to interact with it
- Do different types of Histograms, and allow the user to toggle different options
  - Stacked barchart/histogram
  - Grouped barchart/histogram
  - Marimekko chart
  - Overlapped barchart/histogram (different colors for different traces)
- Use separate virtual env for this project to maintain dependencies

### Weird stuff
- When creating Histogram using `go.Bar` instead of `go.Histogram`, getting slightly different results. Had to use `go.Bar` because `go.Histogram` doesn't allow bins of varying sizes I think -_- (here `go` refers to `graph_objects` in `plotly`) 
