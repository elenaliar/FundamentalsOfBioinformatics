# Genetic Mutation Impact Prediction

Predicting the functional impact of genetic mutations is essential for understanding disease mechanisms and developing therapeutic strategies. Accurate tools are needed to distinguish pathogenic from benign variants to guide clinical and research efforts.

This study, as part of the course Fundamentals of Bioinformatics at the Vu Amsterdam, compares the accuracy of three commonly used prediction tools—**PolyPhen-2**, **SIFT**, and a **BLOSUM62-based baseline model**—in predicting the functional effect of genetic mutations. Using receiver operating characteristic (ROC) plots, we evaluated the predictive performance of each tool by calculating the AUC for three datasets of varying sizes and publication dates. The tools were benchmarked against ClinVar annotations to assess their ability to classify mutations as either pathogenic or benign.

**Key findings**:
- **PolyPhen-2** consistently demonstrated the highest accuracy across datasets.
- **SIFT** performed slightly below PolyPhen-2 but still showed strong predictive power.
- The **baseline model**, while functional, had AUC values close to random classification.

These results highlight the importance of advanced computational tools for genetic variant classification. Future research could integrate additional data sources to further improve prediction accuracy.

---

## 🔧 How to Run the Project

1. **Set up the Python environment and install dependencies**  
   - Make the setup script executable and run it:
     ```bash
     chmod +x setup.sh
     ./setup.sh
     ```

2. **Activate the virtual environment** (if not automatically activated):  
   ```bash
   source .venv/bin/activate
   ```

3. **Run the baseline model script**

   ```bash
   python3 skeleton_script_baseline_model.py data/vep/HGVS_2020_small_VEP_baseline.tsv data/BLOSUM62.txt output/output_baseline_scores.tsv
   ```
   
4. **Generate ROC plots for individual prediction tools**
   Run this script for each of the tools (SIFT, PolyPhen-2, and the baseline model).

  ```bash
  python3 skeleton_script_create_roc_plot.py -ibench data/HGVS_2020_benchmark.tsv -ipred data/vep/HGVS_2020_small_polyphen_scores.tsv -o          output/ROCplot_HGVS_2020_small_polyphen_test.png -color
  ```

5. **Create a combined ROC plot**
   This overlays the ROC curves of all three methods into one figure:
  ```bash
  python3 skeleton_script_roc_plot_tsv.py \
  -itsv output/ROCplot_HGVS_2020_small_sift_test_xy.tsv \
  -itsv output/ROCplot_HGVS_2020_small_polyphen_test_xy.tsv \
  -itsv output/ROCplot_HGVS_2020_small_baseline_test_xy.tsv \
  -o output/ROCplot_comparison.png
  ```


   
