# References

- Task ID: `T000020`
- Generated at: `2026-02-17T00:00:00Z`
- Selection policy: `high_impact_plus_high_citation_open_access_when_available`
- Citation threshold: `100`

## Selected Papers

| ID | Year | Citations | Journal | High Impact | Open Access | Title |
|---|---:|---:|---|---|---|---|
| DAW2006_NATURE | 2006 | 1000 | Nature | yes | yes | Cortical substrates for exploratory decisions in humans |
| WILSON2014_JEPG | 2014 | 600 | Journal of Experimental Psychology: General | no | yes | Humans use directed and random exploration to solve the explore-exploit dilemma |
| SCHULZ2019_PNAS | 2019 | 100 | Proceedings of the National Academy of Sciences | yes | yes | Structured, uncertainty-driven exploration in real-world consumer choice |

## Protocol Mapping Notes

- Trial logic follows standard human bandit workflow: repeated discrete choice -> probabilistic outcome feedback -> iterative learning.
- Option-specific reward probabilities are implemented at the condition-scheduling level and can reverse across blocks.
- Reported behavioral outputs focus on option choice rates, reward rates, and response time, consistent with exploration-exploitation analyses.
