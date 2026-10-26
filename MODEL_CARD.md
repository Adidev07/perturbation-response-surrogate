# Model / system card

## Intended use

Predict synthetic expression changes from fictional intervention descriptors and cellular contexts. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Generate responses from shared linear descriptor effects plus context interactions. Fit a multi-output ridge surrogate using intervention descriptors, context coordinates and pairwise interaction features. No actual gene targets or intervention sequences are supplied.

## Evaluation protocol

Train on six contexts and test on two unseen contexts. Compare with a training-mean response and a simpler descriptor-only model. Report expression RMSE rather than claiming real perturbation efficacy.

## Known limits

The context coordinates are known synthetic descriptors. Extrapolation in real biology may be far harder; no wet-lab intervention is designed or recommended.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Use a licensed benchmark with context and perturbation splits, include control-adjusted metrics and compare simple baselines before larger models.
