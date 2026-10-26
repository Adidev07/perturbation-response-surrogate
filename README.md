# Context-Held-Out Perturbation Response

Predict synthetic expression changes from fictional intervention descriptors and cellular contexts.

**Category:** Biology / ML

**Execution:** Actual local algorithm or workflow; no external model service required.

## Run

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
python -m unittest discover -v
```

Open `results/report.html` after running. Python 3.10+ is required. Use `--help` for input and seed options.

## Architecture

```mermaid
flowchart LR
  A[CLI and input] --> B[Domain pipeline]
  B --> C[Validation or evaluation]
  C --> D[JSON and HTML report]
```

## Algorithm

Generate responses from shared linear descriptor effects plus context interactions. Fit a multi-output ridge surrogate using intervention descriptors, context coordinates and pairwise interaction features. No actual gene targets or intervention sequences are supplied.

## Evaluation

Train on six contexts and test on two unseen contexts. Compare with a training-mean response and a simpler descriptor-only model. Report expression RMSE rather than claiming real perturbation efficacy.

## Limitations

The context coordinates are known synthetic descriptors. Extrapolation in real biology may be far harder; no wet-lab intervention is designed or recommended.

## Documentation

- [PDF project guide](PROJECT_GUIDE.pdf)
- [Editable guide](GUIDE.md)
- [Model and system card](MODEL_CARD.md)
- [Measured results](results/metrics.json)
- [Test output](TEST_RESULTS.txt)

## Extend it

Use a licensed benchmark with context and perturbation splits, include control-adjusted metrics and compare simple baselines before larger models.

AI-assisted educational project with synthetic data. Review, customize and explain your own contribution accurately. MIT license.

## Biology scope and current relevance

Default inputs are synthetic or project-authored. No clinical deployment or wet-lab validation is claimed. See [research context](RESEARCH_CONTEXT.md) and [data provenance](DATA_PROVENANCE.md).

- [Benchmarking algorithms for generalizable single-cell perturbation response prediction](https://www.nature.com/articles/s41592-025-02980-0) (2025/2026)
- [Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines](https://www.nature.com/articles/s41592-025-02772-6) (2025)
