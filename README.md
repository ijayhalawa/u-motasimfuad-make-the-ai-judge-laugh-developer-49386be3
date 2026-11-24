# Make the AI Judge Laugh: Developer Excuses

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/ijayhalawa/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/ijayhalawa/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

One funny single-line excuse a developer gives when code breaks in production, entered in the [make.fun bounty "Make the AI Judge Laugh: Developer Excuses"](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3).

## The entry

> It worked in staging; production is staging with witnesses.

## How it works

`main.py` (Python 3, stdlib only, no network) writes that single line to `/output/entry.txt` — and a local copy `entry.txt` for verification. The output is deterministic: two runs produce byte-identical files.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
