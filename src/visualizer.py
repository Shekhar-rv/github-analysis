from d3heatmap import d3heatmap as d3
from os import makedirs, path
import pandas as pd


# The dataframe contains more columns then rows. Adjust the size and color differently.
df = pd.read_csv('/github_analysis/src/data/csv/repo_commits.csv')

# Make the directory
viz_dir = '/github_analysis/src/data/viz'
makedirs(viz_dir, exist_ok=True)

# Create heatmap
paths = d3.matrix(
    df,
    fontsize=10,
    title='Github Commits',
    description='Heatmap showing daily commits on Github repositories',
    path=path.join(viz_dir, 'd3_matrix.html'),
    width=1000,
    height=1200,
    cmap='interpolateGreens',
    vmin=0,
    vmax=4,
    showfig=True
)