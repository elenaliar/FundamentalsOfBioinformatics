## FoB project

## Group : 25


## How to setup project:

1. Create python env and install dependencies contained in rquirements.txt (run in terminal):

`chmod +x setup.sh`

1.1 If venv was not automatically activated, activate venv

`source .venv/bin/activate`

2. Run **skeleton_script_baseline_model.py**

`python3 data/vep/HGVS_2020_small_VEP_baseline.tsv","data/BLOSUM62.txt","output/output_baseline_scores.tsv"`

2. Run **skeleton_script_create_roc_plot.py** / Run this code for sift, polyphen and baseline scores you should obtain three graphs (ROC curves)



`python3 skeleton_script_create_roc_plot.py -ibench data/HGVS_2020_benchmark.tsv -ipred data/vep/HGVS_2020_small_polyphen_scores.tsv -o output/ROCplot_HGVS_2020_small_polyphen_test.png  -color`

3. Run **skeleton_script_roc_plot.py** (Obtain figure with 3 methods in same figure)

`python3 skeleton_script_roc_plot_tsv.py -itsv output/ROCplot_HGVS_2020_small_sift_test_xy.tsv -itsv output/ROCplot_HGVS_2020_small_polyphen_test_xy.tsv -itsv output/ROCplot_HGVS_2020_small_baseline_test_xy.tsv -o output/ROCplot_comparison.png `




