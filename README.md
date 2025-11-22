# SMS Spam Detection – Static Demo

This repository now contains only the SMS spam detection web demo found in `PROJECT@/`. The page bundles a trained logistic-regression model (`model_data.js`) and a Tailwind-based UI (`index.html`) so you can score SMS snippets entirely client-side.

## Folder Layout
- `PROJECT@/index.html` – interactive UI plus inference logic.
- `PROJECT@/model_data.js` – exported vocabulary, coefficients, intercept, and stop words.
- `PROJECT@/SMSSpamCollection` – original dataset reference (see included README for license info).
- `PROJECT@/result pics/` – confusion matrices and experiment artifacts.
- `.github/workflows/pages.yml` – publishes the static site.

## Live Demo (GitHub Pages)
Every push to `main` triggers the **Deploy SMS Spam UI** workflow, which uploads `PROJECT@/` and deploys to GitHub Pages.

- **URL:** https://nagaraj0000b.github.io/sms-spam-detection/
- To redeploy, push commits or rerun the workflow from GitHub → Actions.
- Watch the run logs under `Deploy SMS Spam UI`; the resulting link appears in the job summary.

## Local Preview
You can open `PROJECT@/index.html` directly in a browser—no backend is required because inference happens with the embedded model weights.

## Dataset Notice
`PROJECT@/readme` describes the original SMS Spam Collection corpus and its attribution requirements. Please review it if you plan to reuse the dataset.

## Project Overview
- **Goal:** Predict a continuous value (e.g., salary) based on input features using a linear model.
- **Techniques Used:** Simple linear regression, data visualization, model evaluation.
- **Files:**
	- `predctionOfSalary.py`: Main code for linear regression.
	- `salary_data.csv`: Dataset used for training and testing.

## How to Run
1. Open `predctionOfSalary.py`.
2. Ensure `salary_data.csv` is in the same directory.
3. Run the script to train and test the linear regression model.

## Key Concepts
- Fitting a line to data points
- Calculating coefficients
- Making predictions
- Evaluating model performance

---
This project is a simple introduction to machine learning and linear regression. More advanced topics will be covered in future projects.
