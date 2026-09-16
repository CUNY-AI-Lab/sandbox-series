# Gateway model check

Checked 16 September 2026 at 18:42 UTC through a public, unauthenticated request to [Gateway catalog](https://tools.ailab.gc.cuny.edu/v1/catalog). HTTP 200 returned 60 offerings. Selected entries carry a specification check timestamp of 2026-09-16T09:45:33.400Z.

| Catalog display name | Canonical model ID | Provider |
| --- | --- | --- |
| Gemma 4 26B A4B IT | `gemma-4-26b-a4b-it` | `workers-ai` |
| Qwen3 30B A3b fp8 | `qwen3-30b-a3b-fp8` | `workers-ai` |
| Mistral Large 3 | `mistral-large-3-675b-instruct` | `bedrock-mantle` |

Gemma 4 E4B was absent from this catalog. The A4B and A3B identifiers describe active parameters in larger models; they do not establish total model sizes of 4B and 3B. Use catalog names in workshop materials.

## Selector tags

[Current Open WebUI deployment instructions](https://github.com/CUNY-AI-Lab/cail-openwebui-deploy/blob/main/README.md#L129-L147) assign the visible `gateway` tag to Gateway models and `legacy` to retained direct-provider models. Gateway IDs are unprefixed; direct OpenRouter IDs additionally use `legacy-openrouter`, as documented in [connection configuration](https://github.com/CUNY-AI-Lab/cail-openwebui-deploy/blob/main/README.md#L281-L289). README content was checked through GitHub at blob `5314f2627ee64e2a4de221ca8f9efb2a71ecf305`.

The [public registry](https://ailab.gc.cuny.edu/models/) links to this catalog as its model source. The local registry implementation at `/Users/milwright/Projects/dev/cail-website-models-pagination/src/scripts/model-availability.ts` also reads that endpoint. Its checkout predates the current catalog and is not authority for current offerings.

## Verification boundary

Native Firefox inspection on 16 September confirmed that model selector displays a **Gateway** filter. Gemma 4 26B A4B IT was selected through that filter and captured with selector open. Those captures show selection and visibility; no Gemma request was submitted for them.

Mistral Large 3 was then selected through the same Gateway filter. The unchanged workshop prompt was submitted once in a new chat.

> The car wash is 50 meters from me. Should I walk or take the car? Explain your reasoning.

Its first response recommended walking. The authentic screenshot captured at 14:46:36 EDT shows Mistral Large 3, the complete question and response, and a generation label of 237 tokens and 17.60 seconds. The operator reported no regeneration, follow-up, or added instructions to elicit that recommendation. Screenshot pixels independently confirm the question, model label, timing label, and walking recommendation. These observations describe this response and do not establish typical timing or behavior.

No Qwen request was submitted during this check. Qwen3 30B A3b fp8 is verified as a catalog entry, not as a completed live generation. Final screenshot crops and annotations are recorded in [screenshot provenance](../screenshot-sources.json).
